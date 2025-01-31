<script>
import NavBar from '../components/NavBar.vue'
import get from '../api/api.js'

let arr = get

console.log(arr)


export default {
  name: 'App',
  components: {
    Nav: NavBar
  },
  methods: {
    reposition_top(id, data) {
      document.getElementById(id).style.top = data;
    }
  }
}
</script>

<template>

  <!DOCTYPE html>
  <html lang="en" data-theme="dark">
  <head>
    <meta charset="UTF-8">
    <title>ПВББ Карта</title>
    <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css"
    >
  </head>
  <body>

  <Nav name="" />

  <h1 class="py-4"></h1>

  <div class="columns purple-background">
    <div class="column is-1"></div>
    <div class="column is-3">

      <div class="title is-1 has-text-centered pb-3">Добрий день, Артём</div>

      <div class="title is-1 has-text-centered pb-6">1222.05
        <svg class="pl-2" xmlns="http://www.w3.org/2000/svg" height="40px" viewBox="0 -960 960 960" width="40px"
             fill="#8C1AF6">
          <path d="M560-440q-50 0-85-35t-35-85q0-50 35-85t85-35q50 0 85 35t35 85q0 50-35 85t-85 35ZM280-320q-33 0-56.5-23.5T200-400v-320q0-33 23.5-56.5T280-800h560q33 0 56.5 23.5T920-720v320q0 33-23.5 56.5T840-320H280Zm80-80h400q0-33 23.5-56.5T840-480v-160q-33 0-56.5-23.5T760-720H360q0 33-23.5 56.5T280-640v160q33 0 56.5 23.5T360-400Zm440 240H120q-33 0-56.5-23.5T40-240v-440h80v440h680v80ZM280-400v-320 320Z"/>
        </svg>
      </div>

      <div class="box" style="width: 20rem;">
        <div class="title is-3 has-text-centered">Кешбек на місяць</div>

        <div>
          <svg class="p-1" style="background-color:#f5ad42; border-radius: 50%;"
               xmlns="http://www.w3.org/2000/svg" height="25px" viewBox="0 -960 960 960" width="25px"
               fill="#000000">
            <path d="m200-553.67 96.67 41Q313.33-546 332-578q18.67-32 40-62l-71.33-14.33L200-553.67ZM350-472l126.67 126.33q52-22.66 101.33-55.66T662-469q77.33-77.33 115.83-162.5T816.67-812q-95.34.33-180.67 38.83-85.33 38.5-162.67 115.84-34.66 34.66-67.66 84Q372.67-524 350-472Zm212-85.67q-21-21-21-51.83t21-51.83q21-21 52-21t52 21q21 21 21 51.83t-21 51.83q-21 21-52 21t-52-21Zm-3.67 362.34L659-296l-14.33-71.33q-30 21.33-62 39.83t-65.34 35.17l41 97ZM880-875.67q12.33 131-30.5 243.84Q806.67-519 706-418.33q-.67.66-1.33 1.33-.67.67-1.34 1.33l21.34 106.34Q728-292.67 723-277q-5 15.67-17 27.67L536-78.67l-84.67-197.66L281-446.67 83.33-531.33l170.34-170q12-12 27.83-17 15.83-5 32.5-1.67l106.33 21.33q.67-.66 1.34-1 .66-.33 1.33-1 100.67-100.66 213.33-144Q749-888 880-875.67Zm-728.33 552q35-35 85.5-35.5t85.5 34.5q35 35 34.5 85.5t-35.5 85.5q-25.67 25.67-81.5 43-55.84 17.34-162.84 32Q92-185.67 109-241.83q17-56.17 42.67-81.84Zm47 47.34Q186-263 175.33-232.83q-10.66 30.16-17.33 72.5 42.33-6.67 72.5-17.17 30.17-10.5 43.5-23.17 16.67-15.33 17.33-38Q292-261.33 276-278q-16.67-16-39.33-15.5-22.67.5-38 17.17Z"/>
          </svg>
          21% на ракетне топливо
        </div>

        <div class="pt-2">
          <svg class="p-1" style="background-color:#f5dd42; border-radius: 50%;"
               xmlns="http://www.w3.org/2000/svg" height="25px" viewBox="0 -960 960 960" width="25px"
               fill="#000000">
            <path d="m382-80-18.67-126.67q-17-6.33-34.83-16.66-17.83-10.34-32.17-21.67L178-192.33 79.33-365l106.34-78.67q-1.67-8.33-2-18.16-.34-9.84-.34-18.17 0-8.33.34-18.17.33-9.83 2-18.16L79.33-595 178-767.67 296.33-715q14.34-11.33 32.34-21.67 18-10.33 34.66-16L382-880h196l18.67 126.67q17 6.33 35.16 16.33 18.17 10 31.84 22L782-767.67 880.67-595l-106.34 77.33q1.67 9 2 18.84.34 9.83.34 18.83 0 9-.34 18.5Q776-452 774-443l106.33 78-98.66 172.67-118-52.67q-14.34 11.33-32 22-17.67 10.67-35 16.33L578-80H382Zm55.33-66.67h85l14-110q32.34-8 60.84-24.5T649-321l103.67 44.33 39.66-70.66L701-415q4.33-16 6.67-32.17Q710-463.33 710-480q0-16.67-2-32.83-2-16.17-7-32.17l91.33-67.67-39.66-70.66L649-638.67q-22.67-25-50.83-41.83-28.17-16.83-61.84-22.83l-13.66-110h-85l-14 110q-33 7.33-61.5 23.83T311-639l-103.67-44.33-39.66 70.66L259-545.33Q254.67-529 252.33-513 250-497 250-480q0 16.67 2.33 32.67 2.34 16 6.67 32.33l-91.33 67.67 39.66 70.66L311-321.33q23.33 23.66 51.83 40.16 28.5 16.5 60.84 24.5l13.66 110Zm43.34-200q55.33 0 94.33-39T614-480q0-55.33-39-94.33t-94.33-39q-55.67 0-94.5 39-38.84 39-38.84 94.33t38.84 94.33q38.83 39 94.5 39ZM480-480Z"/>
          </svg>
          0.000001% на цепь для бензопіли Kross WXT-1080 XX Germany
        </div>
        <div class="pt-2">
          <svg class="p-1" style="background-color:#757cfd; border-radius: 50%;"
               xmlns="http://www.w3.org/2000/svg" height="25px" viewBox="0 -960 960 960" width="25px"
               fill="#000000">
            <path d="M499.33-92q-78.66 0-146-39Q286-170 246-238.67L114.67-465l10-10q6.66-6.67 15.83-7.67t16.83 4.34L332-362.67V-750q0-4.33 3.36-8.17Q338.72-762 344-762q4.33 0 8.17 3.83Q356-754.33 356-750v433L144-459.33l122.67 206.66q35.66 63.34 97.7 100Q426.4-116 499.33-116q109.99 0 187.33-76.33Q764-268.67 764-379v-357q0-4.33 3.36-8.17Q770.72-748 776-748q4.33 0 8.17 3.83Q788-740.33 788-736v357q0 119.87-84.19 203.44Q619.63-92 499.33-92Zm-23-416v-322q0-4.33 3.71-8.17 3.7-3.83 8.33-3.83 5.3 0 8.63 3.83 3.33 3.84 3.33 8.17v322h-24Zm144.34 0v-282q0-4.33 3.7-8.17 3.7-3.83 8.33-3.83 5.3 0 8.63 3.83 3.34 3.84 3.34 8.17v282h-24ZM454.33-312.33Z"/>
          </svg>
          51% на ренген правого мізинца
        </div>
      </div>
    </div>
    <div class="column is-one-quarter">
      <div class="box card-background" style="background-color: #bd8c19;" id="repostop"></div>
      <div class="box card-yellow" style="width: 28rem" v-on:mousemove="reposition_top('repostop', '20.7rem')"
           v-on:mouseout="reposition_top('repostop', '19.6rem')">
        <div style="text-align: start; font-size: 2rem" id="">ПВББ</div>
        <div style="text-align: center; font-size: 3rem" class="py-6">
          1488 2281 1234 1111
        </div>
        <div style="font-size: 1rem">User1</div>
      </div>
    </div>


    <div class="column is-1"></div>
    <div class="column is-2">
      <div class="title" style="text-align: center">Завдання на день</div>
      <div class="box">
        <div class="grid">
          <div class="title is-4 p-1"></div>
          <progress class="progress is-success" value="50" max="100">

          </progress>
          1/2
        </div>
      </div>
    </div>
    <div class="column is-1">
      <div class="py-6"></div>
      <div class="py-6"></div>
      <div class="py-6"></div>
      <div class="py-6"></div>
      <div class="py-6"></div>
      <div class="py-6"></div>
      <div class="py-6"></div>
      <div class="py-6"></div>
      <div class="py-6"></div>
    </div>

  </div>
  </body>
  </html>
</template>



<style src="../../style.css">

</style>
