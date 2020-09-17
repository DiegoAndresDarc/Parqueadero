import Vue from 'vue';
import Router from 'vue-router';
import App from '../components/App.vue'
import Login from '../components/Login.vue'
import Signup from '../components/Signup.vue'
import Container from '../components/Container.vue'
import RecoverPassword from '../components/RecoverPassword.vue'
import AddCoprop from '../components/AddCoprop.vue'
import ModCoprop from '../components/ModCoprop.vue'
import DelCoprop from '../components/DelCoprop.vue'
import Adduser from '../components/Adduser.vue'
import Moduser from '../components/Moduser.vue'
import Deluser from '../components/Deluser.vue'

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
      ]
    },
    {
      path: '/recoverPassword',
      component: RecoverPassword
    }
  ]
});
