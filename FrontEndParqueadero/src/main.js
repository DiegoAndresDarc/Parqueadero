import Vue from 'vue'
import router from './router/router'
import App from './components/App.vue'
import axios from 'axios'

Vue.prototype.$axios = axios;

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
