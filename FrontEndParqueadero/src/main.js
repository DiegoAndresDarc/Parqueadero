import Vue from 'vue'
import router from './router/router'
import App from './components/globals/App.vue'
import axios from 'axios'
import VueSession from 'vue-session'
import VueResource from 'vue-resource';

var options = {
  persist: false
}
Vue.use(VueSession, options)
Vue.use(VueResource);
Vue.prototype.$axios = axios;
const EventBus = new Vue()
Object.defineProperties(Vue.prototype, {
  $bus: {
    get: function () {
      return EventBus;
    }
  },
});
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})