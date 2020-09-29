<template>
  <div id="menuview" class="navuser">
    <div class="field">
      <div class="control">
        <h1>{{ message }}</h1>
      </div>
    </div>
    <aside class="menu-aside">
      <ul class="menu-list">
        <li v-for="item in menu" v-bind:key="item.id_menu">
          <a
            :id="item.id_menu"
            v-if="!item.id_padre"
            v-on:click="
              item.tiene_hijos === '0'
                ? loadview(item)
                : item.mostrar === '0'
                ? (item.mostrar = '1')
                : (item.mostrar = '0')
            "
          >
            {{ item.nombre }}
            <span class="icon icon-menu i-menu">
              <i
                :class="
                  item.tiene_hijos === '0'
                    ? 'mdi mdi-chevron-double-left'
                    : 'mdi mdi-chevron-double-down'
                "
              ></i>
            </span>
          </a>
          <transition type="slide">
            <ul class="submenu-list child" v-if="item.mostrar === '1'">
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
      mostrar: false,
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
      const routername = item.nombre.replace(" ", "-");
      const routerpath = "/" + routername;
      if (this.$route.path !== routerpath) {
        this.$router.push({
          name: routername,
          params: { usuario: this.usuario },
        });
      }
      mostrar = false;
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
    console.log("Menu.vue");
  },
};
</script>
<style>
.navuser h1 {
  font-weight: bold;
  color: black;
}
.navuser {
  background: salmon;
}
.menu-aside {
  z-index: 1000;
  max-width: 1000px;
  width: 100%;
  margin: 10px auto;
}

.menu-list {
  list-style: none;
}
.menu-list li {
  display: inline-block;
  position: relative;
}
.menu-list li:hover .child {
  display: block;
}
.menu-list li a {
  color: black;
  font-weight: bold;
  display: block;
  text-decoration: none;
  padding: 10px;
}

.child {
  display: none;
}

.child li {
  display: block;
  overflow: hidden;
  border-bottom: 1px solid rgba(0, 0, 0, 1);
}

.child li a {
  display: block;
  text-decoration: none;
  padding: 10px;
}

@media screen and (max-width: 800px) {
  .menu-aside {
    width: 80%;
    height: calc(100% - 80px);
    position: fixed;
    left: 0;
    margin: 0;
    overflow: scroll;
  }

  .menu-list li:hover .child {
    display: none;
  }
  .menu-list li {
    display: block;
    border-bottom: 1px solid rgba(0, 0, 0, 1);
  }

  .menu-list li a {
    display: block;
  }

  .child {
    width: 100%;
    position: relative;
  }

  .child li a {
    margin-left: 20px;
  }
}
</style>