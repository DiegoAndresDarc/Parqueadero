<template>
  <div id="menu" class="navuser">
    <div class="field">
      <div class="control">
        <h1>{{message}}</h1>
      </div>
    </div>
    <aside class="menu">
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
      message: "Menu de navegación",
      menu: [],
      submenu: [],
      LoggedIn: false,
    };
  },
  methods: {
    checkSession() {
      this.$axios
        .get("MainServlet/checkSession")
        .then((response) => {
          this.LoggedIn = response.data != null ? true : false;
          if (this.LoggedIn) {
            this.loadMenu();
          } else {
            this.$router.push("/login");
          }
        })
        .catch((e) => {
          console.log(e);
          this.LoggedIn = false;
          this.$router.push("/login");
        });
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
      console.log(this.menu);
    },
    loadSubmenu(id) {
      return this.menu.filter(function (item) {
        return item.id_padre == id;
      });
    },
    loadview(item) {
      this.$router.push("/" + item.nombre.replace(" ", "-"));
      console.log(item.nombre.replace(" ", "-"));
      //this.$router.push("/signup");
    },
    logout() {
      this.$axios
        .get("MainServlet/logout")
        .then((response) => {
          this.LoggedIn = false;
          this.$router.push("/");
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  created() {
    this.checkSession();
    console.log("Menu.vue");
  },
};
</script>
<style>
</style>