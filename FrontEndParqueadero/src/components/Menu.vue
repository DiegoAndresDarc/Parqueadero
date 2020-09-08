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
export default {
  name: "menu",
  components: {},
  data() {
    return {
      message: "Menu",
      menu: [],
      id: "0",
    };
  },
  methods: {
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
    console.log("Menu.vue");
  },
};
</script>
<style>
</style>