<template>
  <div id="menuview" class="navuser">
    <div class="field">
      <div class="control">
        <h1 class="menu-label">{{ message }}</h1>
      </div>
    </div>
    <div class="field">
      <div class="control">
        <aside class="menu">
          <ul class="menu-list">
            <li v-for="item in menu" v-bind:key="item.id_menu">
              <a
                :id="item.id_menu"
                v-if="!item.id_padre"
                v-on:click="
                  item.tiene_hijos == 0
                    ? loadview(item)
                    : (item.mostrar = item.mostrar)
                "
              >
                {{ item.nombre }}
                <span class="icon">
                  <i
                    :class="
                      item.tiene_hijos == 0
                        ? 'mdi mdi-chevron-double-left'
                        : 'mdi mdi-chevron-double-down'
                    "
                  ></i>
                </span>
              </a>
              <transition type="slide">
                <ul class="child" v-if="item.mostrar">
                  <li
                    v-for="subitem in loadSubmenu(item.id_menu)"
                    v-bind:key="subitem.id_menu"
                  >
                    <a :id="subitem.id_menu" v-on:click="loadview(subitem)"
                      >{{ subitem.nombre }}
                      <span class="icon icon-menu i-menu">
                        <i class="mdi mdi-point"></i> </span
                    ></a>
                  </li>
                </ul>
              </transition>
            </li>
            <li>
              <a v-on:click="logout"
                >Salir
                <span class="icon icon-menu i-menu">
                  <i class="mdi mdi-exit-to-app"></i> </span
              ></a>
            </li>
          </ul>
        </aside>
      </div>
    </div>
  </div>
</template>
<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "menu",
  components: {},
  data() {
    return {
      message: "",
      menu: [],
      submenu: [],
      LoggedIn: false,
      nombres: "",
      apellidos: "",
      usuario: "",
    };
  },
  methods: {
    loadMenu() {
      this.message = this.nombres + " " + this.apellidos;
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/menu.php";
      this.menu = [];
      var param = {
        tipo_usuario: this.usuario,
      };
      this.$axios
        .get(url, { params: param })
        .then((response) => {
          this.menu = response.data;
          this.menu.forEach((item) => {
            item.mostrar = true;
          });
        })
        .catch((e) => {
          console.log(e);
        });
    },
    loadSubmenu(id) {
      return this.menu.filter(function (item) {
        return item.id_padre == id;
      });
    },
    loadview(item) {
      const routername = item.nombre.replaceAll(" ", "-");
      const routerpath = "/" + routername;
      if (this.$route.path !== routerpath) {
        this.$router.push({
          name: routername,
          params: { usuario: this.usuario },
        });
      }
    },
    logout() {
      this.$bus.$emit("logout", "");
    },
    loadCoprop() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      var requestObject = {
        tabla: "copropiedad",
        id_administrador: this.$session.get("id"),
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          this.$session.set("id_coprop", response.data[0].id);
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  beforeCreate() {
    this.$bus.$emit("checkSession", "");
  },
  created() {
    this.usuario = this.$session.get("user");
    this.nombres = this.$session.get("name");
    this.apellidos = this.$session.get("lastname");
    this.loadMenu();
    if (this.usuario == "A") this.loadCoprop();
  },
};
</script>
<style>
</style>