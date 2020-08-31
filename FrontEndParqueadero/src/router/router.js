import Vue from 'vue';
import Router from 'vue-router';
import Login from '../components/Login.vue'
import Signup from '../components/Signup.vue'
import Container from '../components/Container.vue'
import RecoverPassword from '../components/RecoverPassword.vue'

Vue.use(Router);

export default new Router({
    routes: [
        { path: '/', name: 'login', component: Login },
        { path: '/signup', component: Signup },
        { path: '/Home', component: Container },
        { path: '/recoverPassword', component: RecoverPassword }
    ]
});
