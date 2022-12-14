import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import VueCookies from "vue-cookies"
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
// import axios from 'axios'
import './assets/common.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// cookie 사용
Vue.use(VueCookies)

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
