import axios from 'axios';
function axios_get() {
    axios.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
}
export default {
    axios_get
}