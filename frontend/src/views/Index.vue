<script>
import NavBar from '../components/NavBar.vue'


export default {
  name: 'IndexMain',
  components: {
    Nav: NavBar,
  }
}
</script>

<template>
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <title></title>
    <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css"
    >
  </head>
  <body>
  <Nav/>
  <div class="fixed-grid has-9-cols">
    <div class="grid">
      <div class="cell is-col-start-3"><h1 class="title is-1" style="text-align: center">ПВББ</h1>
        <h2 class="subtitle is-6" style="text-align: center; font-family: fantasy">Банк больших бобров</h2></div>
      <div class="cell is-col-start-8">
        <a class="icon-text pt-5">
                    <span class="icon">
                        <svg xmlns="http://www.w3.org/2000/svg" height="40px" viewBox="0 -960 960 960" width="40px"
                             fill="#8C1AF6"><path
                            d="M48.67-117.67v-129.82q0-40.91 22.11-76.48Q92.9-359.55 131-378q65-30 132.5-46.5T396.67-441q29.33 0 73.33 5.5t75.67 13.5L455-331.67q-15.26-2.66-29.8-3.33-14.53-.67-28.53-.67-58.85 0-109.76 12.67-50.91 12.67-105.34 35.83-14.44 7.12-21.34 18.84-6.9 11.73-6.9 25v21H428l104.67 104.66h-484Zm597.66-2-149-149.66L553-324l93.33 93.33L855.67-440 912-385.33 646.33-119.67Zm-249.8-376q-78.47 0-129.83-51.36-51.37-51.36-51.37-129.83 0-78.47 51.37-129.81Q318.06-858 396.53-858q78.47 0 130.3 51.33 51.84 51.34 51.84 129.81t-51.84 129.83q-51.83 51.36-130.3 51.36ZM428-222.33Zm-31.48-378q32.81 0 54.81-21.89 22-21.88 22-54.74 0-33.14-21.85-54.76-21.85-21.61-54.67-21.61-32.81 0-54.81 21.7-22 21.71-22 54.32 0 33.03 21.85 55 21.85 21.98 54.67 21.98Zm.15-76.67Z"/></svg>
                    </span>
          <span class="purple-text title is-5">Вход</span>
        </a>
      </div>
      <div class="cell is-col-start-9">
        <a class="icon-text pt-5">
                    <span class="icon">
                        <svg xmlns="http://www.w3.org/2000/svg" height="40px" viewBox="0 -960 960 960" width="40px"
                             fill="#8C1AF6"><path
                            d="M218.16-134.33q-34.83 0-59.33-24.5t-24.5-59.33q0-34.82 24.5-59 24.5-24.17 59.33-24.17 34.82 0 59 24.17 24.17 24.18 24.17 59 0 34.83-24.17 59.33-24.18 24.5-59 24.5Zm0-262.67q-34.83 0-59.33-24.04-24.5-24.03-24.5-58.66 0-34.63 24.5-58.97Q183.33-563 218.16-563q34.82 0 59 24.04 24.17 24.03 24.17 58.66 0 34.63-24.17 58.97-24.18 24.33-59 24.33Zm0-261.67q-34.83 0-59.33-24.17-24.5-24.18-24.5-59 0-34.83 24.5-59.33t59.33-24.5q34.82 0 59 24.5 24.17 24.5 24.17 59.33 0 34.82-24.17 59-24.18 24.17-59 24.17Zm262.14 0q-34.63 0-58.97-24.17-24.33-24.18-24.33-59 0-34.83 24.04-59.33 24.03-24.5 58.66-24.5 34.63 0 58.97 24.5Q563-776.67 563-741.84q0 34.82-24.04 59-24.03 24.17-58.66 24.17Zm261.54 0q-34.82 0-59-24.17-24.17-24.18-24.17-59 0-34.83 24.17-59.33 24.18-24.5 59-24.5 34.83 0 59.33 24.5t24.5 59.33q0 34.82-24.5 59-24.5 24.17-59.33 24.17ZM480.24-397q-34.57 0-58.91-24.09Q397-445.19 397-479.76t24.09-58.91Q445.19-563 479.76-563t58.91 24.09Q563-514.81 563-480.24t-24.09 58.91Q514.81-397 480.24-397Zm35.09 262.67v-146.34L741-505.33q11.33-12.18 25.33-17.26 14-5.08 28.67-5.08 14.67 0 28.88 5.67 14.22 5.67 25.45 17.67l37 37q10.9 11.44 16.62 25.44 5.72 13.99 5.72 27.98 0 15.32-5.84 29.12Q897-371 885.73-359L661.67-134.33H515.33ZM832-414l-37-37 37 37ZM592-211h38l117.67-118.51-18-19.08-19-18.08L592-249.16V-211Zm137.67-137.67-19-18 37 37-18-19Z"/></svg>
                    </span>
          <span class="purple-text title is-5">Регистрация</span>
        </a>
      </div>
    </div>
  </div>


  <div class="fixed-grid has-10-cols purple-background pt-5">
    <div class="grid">

      <div class="cell is-col-start-3">
        <div class="box card-anim" style="width: 28rem">
          <div style="text-align: start; font-size: 2rem">ПВББ</div>
          <div style="text-align: center; font-size: 3rem" class="py-6">1111 2222 3333 4444
          </div>
          <div style="font-size: 1rem">User1</div>
        </div>
        <h2 class="subtitle is-4" style="text-align: center; font-family: fantasy">Твоя карта - Твой выбор</h2>
        <div style="text-align: center">Внимание! Валюта ПБ исключительно виртуальная! За ПБ можно
          только покупать внутри сайтовые бонусы
        </div>

        <div class="py-6"></div>
        <svg xmlns="http://www.w3.org/2000/svg" height="200px" viewBox="0 -960 960 960" width="200px"
             fill="#8C1AF6">
          <path
              d="M270-160q-50 0-82-36t-27-85H61l13-60h112q15-18 36.5-28.5T270-380q26 0 47.5 10.5T354-341h198l92-399H186l3-13q5-21 21-34t37-13h472l-39 170h125l114 152-39 197h-80q5 49-27.5 85T690-160q-50 0-82-36t-27-85H380q5 49-27.5 85T270-160Zm364-270h215l6-33-80-107H666l-32 140Zm1-273 9-37-92 399 8-36 34-146 41-180ZM22-437l15-60h220l-15 60H22Zm80-146 15-60h260l-15 60H102Zm168 363q21 0 35.5-15t14.5-35q0-21-14.5-35.5T270-320q-20 0-35 14.5T220-270q0 20 15 35t35 15Zm420 0q21 0 35.5-15t14.5-35q0-21-14.5-35.5T690-320q-20 0-35 14.5T640-270q0 20 15 35t35 15Z"/>
        </svg>
        <div class="subtitle is-3" style="text-align: center; font-family: fantasy">Быстрые переводы без комисии!
        </div>
        <div class="subtitle is-6 pt-3" style="text-align: center">Или все-таки нет!?</div>


      </div>

      <div class="cell is-col-start-7">
        <svg xmlns="http://www.w3.org/2000/svg" height="200px" viewBox="0 -960 960 960" width="200px"
             fill="#8C1AF6">
          <path
              d="M479.88-200Q434-200 402-232.12q-32-32.12-32-78T402.12-388q32.12-32 78-32T558-387.88q32 32.12 32 78T557.88-232q-32.12 32-78 32ZM165-490q18-117 107-193.5T479-760q81 0 149 37t112 99v-136h60v270H530v-60h186q-32-67-95.17-108.5T480-700q-93.55 0-164.77 59.5Q244-581 226-490h-61Z"/>
        </svg>
        <div class="subtitle is-3" style="text-align: center; font-family: fantasy">Большой Кешбек!</div>
        <div class="subtitle is-6" style="text-align: center">Или нет?</div>


        <div class="py-6"></div>
        <div class="py-6"></div>


        <svg xmlns="http://www.w3.org/2000/svg" height="200px" viewBox="0 -960 960 960" width="200px"
             fill="#8C1AF6">
          <path
              d="M180-80q-24 0-42-18t-18-42v-620q0-24 18-42t42-18h65v-60h65v60h340v-60h65v60h65q24 0 42 18t18 42v620q0 24-18 42t-42 18H180Zm0-60h600v-430H180v430Zm0-490h600v-130H180v130Zm0 0v-130 130Zm300 230q-17 0-28.5-11.5T440-440q0-17 11.5-28.5T480-480q17 0 28.5 11.5T520-440q0 17-11.5 28.5T480-400Zm-160 0q-17 0-28.5-11.5T280-440q0-17 11.5-28.5T320-480q17 0 28.5 11.5T360-440q0 17-11.5 28.5T320-400Zm320 0q-17 0-28.5-11.5T600-440q0-17 11.5-28.5T640-480q17 0 28.5 11.5T680-440q0 17-11.5 28.5T640-400ZM480-240q-17 0-28.5-11.5T440-280q0-17 11.5-28.5T480-320q17 0 28.5 11.5T520-280q0 17-11.5 28.5T480-240Zm-160 0q-17 0-28.5-11.5T280-280q0-17 11.5-28.5T320-320q17 0 28.5 11.5T360-280q0 17-11.5 28.5T320-240Zm320 0q-17 0-28.5-11.5T600-280q0-17 11.5-28.5T640-320q17 0 28.5 11.5T680-280q0 17-11.5 28.5T640-240Z"/>
        </svg>
        <div class="subtitle is-4" style="text-align: center; font-family: fantasy">Ежедневные расходы!</div>
        <div class="subtitle is-6" style="text-align: center">Без вашего согласия!</div>
      </div>

    </div>
    <div class="py-6"></div>
    <div class="py-6"></div>
    <div class="py-6"></div>
    <div class="py-6"></div>
  </div>


  </body>
  </html>
</template>

<style src="../../style.css">

</style>