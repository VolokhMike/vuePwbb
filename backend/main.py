from flask_bcrypt import Bcrypt
from smtplib import SMTP
from flask import Flask, request, jsonify, make_response
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
bcrypt = Bcrypt(app)


@app.post('/register')
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    try:
        register(username, hashed_password)
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.post('/set-cookie')
def set_cookie():
    try:
        data = request.get_json()
        if not data or 'user_id' not in data:
            return jsonify({'error': 'Missing user_id'}), 400

        response = make_response(jsonify({
            'message': 'Cookie set successfully'
        }))

        # Устанавливаем cookie с различными параметрами безопасности
        response.set_cookie(
            'user_id',  # название cookie
            str(data['user_id']),  # значение
            max_age=86400,  # время жизни в секундах (24 часа)
            secure=True,  # только для HTTPS
            httponly=True,  # недоступно для JavaScript
            samesite='Strict',  # защита от CSRF атак
            path='/'  # путь, где доступен cookie
        )
        return response

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Получение cookie
@app.get('/get-cookie')
def get_cookie():
    try:
        user_id = request.cookies.get('user_id')

        if not user_id:
            return jsonify({'error': 'Cookie not found'}), 404

        return jsonify({
            'user_id': user_id
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.post('/delete-cookie')
def delete_cookie():
    try:
        response = make_response(jsonify({
            'message': 'Cookie deleted successfully'
        }))

        response.delete_cookie('user_id')

        return response

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.post('/set-multiple-cookies')
def set_multiple_cookies():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        response = make_response(jsonify({
            'message': 'Cookies set successfully'
        }))

        for key, value in data.items():
            response.set_cookie(
                key,
                str(value),
                max_age=86400,
                secure=True,
                httponly=True,
                samesite='Strict'
            )

        return response

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.get('/get-all-cookies')
def get_all_cookies():
    try:
        return jsonify(dict(request.cookies))

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(port=1312, debug=True)
