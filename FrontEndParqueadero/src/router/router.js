import Vue from 'vue';
import Router from 'vue-router';
import App from '../components/App.vue'
import Login from '../components/Login.vue'
import Signup from '../components/Signup.vue'
import Container from '../components/Container.vue'
import RecoverPassword from '../components/RecoverPassword.vue'
import AddCoprop from '../components/AddCoprop.vue'
import ModCoprop from '../components/ModCoprop.vue'
import Adduser from '../components/Adduser.vue'
import Moduser from '../components/Moduser.vue'

Vue.use(Router);

export default new Router({
  base: process.env.BASE_URL,
  routes: [{
      path: '/',
      component: App
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/signup',
      component: Signup
    },
    {
      path: '/Home',
      component: Container,
      children: [{
          path: '/Agregar-copropiedad/:user_type?',
          component: AddCoprop
        },
        {
          path: '/Modificar-copropiedad/:user_type?',
          component: ModCoprop
        },
        {
          path: '/Eliminar-copropiedad/:user_type?',
          component: ModCoprop
        },
        {
          path: '/Agregar-usuario/:user_type?',
          component: Adduser
        },
        {
          path: '/Modificar-usuario/:user_type?',
          component: Moduser
        },
        {
          path: '/Eliminar-usuario/:user_type?',
          component: Moduser
        },
      ]
    },
    {
      path: '/recoverPassword',
      component: RecoverPassword
    }
  ]
});
