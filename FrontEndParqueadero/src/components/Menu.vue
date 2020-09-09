<template>
  <div id="menu">
    <div class="field">
      <div class="control">
        <h1>Menu de navegación</h1>
      </div>
    </div>
    <aside class="menu">
      <nav>
        <ul>
          <li>
            <a :id="adminUser" v-on:click="loadview(id)">Administrar usuarios</a>
          </li>
          <li>Administrar Parqueaderos</li>
          <li>Actualizar datos</li>
          <li>Salir</li>
        </ul>
      </nav>
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
      message: "Menu",
      menu: [],
      id: "0",
    };
  },
  methods: {
    getMenu() {
      this.$axios
        .get("MainServlet/getMenu")
        .then((response) => {
          console.log(response.data);
          response.data.array.forEach(element => {
            
          });
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
          this.cleanMessages();
        });
    },
    loadview(id) {
      console.log(id);
      switch (id) {
        case "adminUser":
          this.$router.push("/signup");
          break;
        default:
          break;
      }
    },
  },
  created() {
    getMenu();
    console.log("Menu.vue");
  },
};
</script>
<style>
</style>