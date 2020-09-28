import Vue from 'vue';
import Router from 'vue-router';
import App from '../components/globals/App.vue'
import Login from '../components/globals/Login.vue'
import Signup from '../components/globals/Signup.vue'
import Container from '../components/globals/Container.vue'
import RecoverPassword from '../components/globals/RecoverPassword.vue'
import AddCoprop from '../components/root/AddCoprop.vue'
import ModCoprop from '../components/root/ModCoprop.vue'
import DelCoprop from '../components/root/DelCoprop.vue'
import Adduser from '../components/globals/Adduser.vue'
import Moduser from '../components/globals/Moduser.vue'
import Deluser from '../components/globals/Deluser.vue'
import ConfParams from '../components/admin/ConfParams.vue'
import ModParams from '../components/admin/ModParams.vue'
Vue.use(Router);

export default new Router({
  base: process.env.BASE_URL,
  mode: 'history',
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
      path: '/home',
      name: 'Home',
      component: Container,
      children: [{
          path: '/Agregar-copropiedad',
          name: 'Agregar-copropiedad',
          component: AddCoprop,
        },
        {
          path: '/Modificar-copropiedad',
          name: 'Modificar-copropiedad',
          component: ModCoprop
        },
        {
          path: '/Eliminar-copropiedad',
          name: 'Eliminar-copropiedad',
          component: DelCoprop
        },
        {
          path: '/Agregar-usuario',
          name: 'Agregar-usuario',
          component: Adduser
        },
        {
          path: '/Modificar-usuario',
          name: 'Modificar-usuario',
          component: Moduser
        },
        {
          path: '/Eliminar-usuario',
          name: 'Eliminar-usuario',
          component: Deluser
        },
        {
          path: '/Configurar-parametros',
          name: 'Configurar-parametros',
          component: ConfParams
        },
        {
          path: '/Modificar-parametros',
          name: 'Modificar-parametros',
          component: ModParams
        }
      ]
    },
    {
      path: '/recoverPassword',
      component: RecoverPassword
    }
  ]
});
