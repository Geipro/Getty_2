import Vue from 'vue'
import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import router from './router'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
// 아래는 3자리마다 , 넣어주는 정규표현식
Vue.filter("makeComma", val =>{
  return String(val).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
