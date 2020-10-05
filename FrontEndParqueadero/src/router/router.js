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
import Addapartment from '../components/admin/Addapartment.vue'
import Modapartment from '../components/admin/Modapartment.vue'
import Delapartment from '../components/admin/Delapartment.vue'
import Addparking from '../components/admin/Addparking.vue'
import Modparking from '../components/admin/Modparking.vue'
import Delparking from '../components/admin/Delparking.vue'
import Setparking from '../components/admin/Setparking.vue'
import Removeparking from '../components/admin/Removeparking.vue'
import ModPrincipalData from '../components/client/ModPrincipalData.vue'
import ModPassword from '../components/client/ModPassword.vue'
import ViewInfoMyParkings from '../components/client/ViewInfoMyParkings.vue'
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
        },
        {
          path: '/Agregar-apartamento',
          name: 'Agregar-apartamento',
          component: Addapartment
        },
        {
          path: '/Modificar-apartamento',
          name: 'Modificar-apartamento',
          component: Modapartment
        },
        {
          path: '/Eliminar-apartamento',
          name: 'Eliminar-apartamento',
          component: Delapartment
        },
        {
          path: '/Agregar-parqueadero',
          name: 'Agregar-parqueadero',
          component: Addparking
        },
        {
          path: '/Modificar-parqueadero',
          name: 'Modificar-parqueadero',
          component: Modparking
        },
        {
          path: '/Eliminar-parqueadero',
          name: 'Eliminar-parqueadero',
          component: Delparking
        },,
        {
          path: '/Dar-un-parqueadero',
          name: 'Dar-un-parqueadero',
          component: Setparking
        },,
        {
          path: '/Quitar-un-parqueadero',
          name: 'Quitar-un-parqueadero',
          component: Removeparking
        },
        {
          path: '/Modificar-datos-principales',
          name: 'Modificar-datos-principales',
          component: ModPrincipalData
        },
        {
          path: '/Modificar-contraseña',
          name: 'Modificar-contraseña',
          component: ModPassword
        },
        {
          path: '/Visualizar-datos-de-mis-parqueaderos',
          name: 'Visualizar-datos-de-mis-parqueaderos',
          component: ViewInfoMyParkings
        }
      ]
    },
    {
      path: '/recoverPassword',
      component: RecoverPassword
    }
  ]
});
