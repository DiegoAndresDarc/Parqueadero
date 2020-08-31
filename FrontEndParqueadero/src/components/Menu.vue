<template>
  <div id="menu">
    <aside>
      <nav>
        <h1>Menu de navegación</h1>
        <ul>
          <li>Administrar usuarios</li>
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