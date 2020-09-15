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
      name: 'Login',
      component: Login
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup
    },
    {
      path: '/Home/:user_type',
      name: 'Home',
      component: Container,
      props: true,
      children: [{
          path: '/Agregar-copropiedad',
          name: 'Agregar-copropiedad',
          props: true,
          component: AddCoprop,
        },
        {
          path: '/Modificar-copropiedad',
          name: 'Modificar-copropiedad',
          props: true,
          component: ModCoprop
        },
        {
          path: '/Eliminar-copropiedad',
          name: 'Eliminar-copropiedad',
          props: true,
          component: ModCoprop
        },
        {
          path: '/Agregar-usuario',
          name: 'Agregar-usuario',
          props: true,
          component: Adduser
        },
        {
          path: '/Modificar-usuario',
          name: 'Modificar-usuario',
          props: true,
          component: Moduser
        },
        {
          path: '/Eliminar-usuario',
          name: 'Eliminar-usuario',
          props: true,
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
