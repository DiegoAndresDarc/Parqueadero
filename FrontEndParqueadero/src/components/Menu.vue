<template>
  <div id="menuview" class="navuser">
    <div class="field">
      <div class="control">
        <h1>{{message}}</h1>
      </div>
    </div>
    <aside class="menu-aside">
      <ul class="menu-list">
        <li v-for="item in menu" v-bind:key="item.id_menu">
          <a
            :id="item.id_menu"
            v-if="!item.id_padre"
            v-on:click="!item.tiene_hijos==='0'?loadview(item):item.id_padre=item.id_padre"
          >{{item.nombre}}</a>
          <transition type="slide">
            <ul class="submenu-list child">
              <li v-for="subitem in loadSubmenu(item.id_menu)" v-bind:key="subitem.id_menu">
                <a :id="subitem.id_menu" v-on:click="loadview(subitem)">{{subitem.nombre}}</a>
              </li>
            </ul>
          </transition>
        </li>
        <li>
          <a v-on:click="logout">Salir</a>
        </li>
      </ul>
    </aside>
  </div>
</template>
<script>
import Login from "./Login.vue";
export default {
  name: "menu",
  components: {
    login: Login,
  },
  data() {
    return {
      userData: {
        nombres: "",
        apellidos: "",
        usuario: "R",
      },
      message: "Menu de navegación",
      menu: [],
      submenu: [],
      LoggedIn: false,
    };
  },
  methods: {
    loginInfo(response) {
      //this.message += response.nombres + " " + response.apellidos;
      this.userData = JSON.parse(JSON.stringify(response));
    },
    loadMenu() {
      this.menu = [];
      this.$axios
        .get("MainServlet/getMenu")
        .then((response) => {
          this.menu = response.data;
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
          //this.cleanMessages();
        });
    },
    loadSubmenu(id) {
      return this.menu.filter(function (item) {
        return item.id_padre == id;
      });
    },
    loadview(item) {
      const routerpath = "/" + item.nombre.replace(" ", "-");
      if (this.$route.path !== routerpath) {
        this.$router.push({
          path: routerpath+"/"+this.userData.usuario,
          params: { user_type: this.userData.usuario },
        });
      }
    },
    logout() {
      this.$axios
        .get("MainServlet/logout")
        .then((response) => {
          this.$emit("app:LoggedIn", false);
          this.$router.push("/");
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  created() {
    this.$bus.$on("userData", this.loginInfo);
    this.loadMenu();
    console.log("Menu.vue");
  },
};
</script>
<style>
#menu-aside a {
  color: black;
  font-weight: bold;
}
#menu-aside a.router-link-exact-active {
  color: green;
}
</style>