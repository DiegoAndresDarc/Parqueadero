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
            <a>Administrar usuarios</a>
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
    };
  },
  methods: {},
  created() {
    console.log("Menu.vue");
  },
};
</script>
<style>
</style>