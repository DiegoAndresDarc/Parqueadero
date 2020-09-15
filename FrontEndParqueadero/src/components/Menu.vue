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
export default {
  name: "menu",
  props: {
    nombres: {
      type: String,
      default: "",
    },
    apellidos: {
      type: String,
      default: "",
    },
    usuario: {
      type: String,
      default: "",
    },
  },
  components: {},
  data() {
    return {
      message: "Menu de navegación",
      menu: [],
      submenu: [],
      LoggedIn: false,
    };
  },
  methods: {
    loadMenu() {
      this.message += " " + this.nombres + " " + this.apellidos;
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
      const routername = item.nombre.replace(" ", "-");
      const routerpath = "/" + routername;
      if (this.$route.path !== routerpath) {
        this.$router.push({
          name: routername,
          params: { usuario: this.usuario },
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
    this.usuario = this.$route.params.usuario;
    this.nombres = this.$route.params.nombres;
    this.apellidos = this.$route.params.apellidos;
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