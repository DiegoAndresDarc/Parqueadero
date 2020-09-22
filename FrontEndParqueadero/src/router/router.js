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
      props: {
        nombres: "",
        apellidos: "",
        usuario: "",
      },
      children: [{
          path: '/Agregar-copropiedad',
          name: 'Agregar-copropiedad',
          props: {
            root_admin: false
          },
          component: AddCoprop,
        },
        {
          path: '/Modificar-copropiedad',
          name: 'Modificar-copropiedad',
          props: {
            root_admin: false
          },
          component: ModCoprop
        },
        {
          path: '/Eliminar-copropiedad',
          name: 'Eliminar-copropiedad',
          props: {
            root_admin: false
          },
          component: DelCoprop
        },
        {
          path: '/Agregar-usuario',
          name: 'Agregar-usuario',
          props: {
            root_admin: false
          },
          component: Adduser
        },
        {
          path: '/Modificar-usuario',
          name: 'Modificar-usuario',
          props: {
            root_admin: false
          },
          component: Moduser
        },
        {
          path: '/Eliminar-usuario',
          name: 'Eliminar-usuario',
          props: {
            root_admin: false
          },
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
