<template>
  <div id="container">
    <div class="content-container">
      <appmenu></appmenu>
    </div>
  </div>
</template>
<script>
import Menu from "./Menu.vue";
export default {
  name: "container",
  components: {
    appmenu: Menu,
  },
  data() {
    return {
      message: "Container",
      offset: 0,
      offset2: 0,
    };
  },
  methods: {
    showMenu() {
      this.offset = this.offset === 0 ? -260 : 0;
      this.offset2 = this.offset2 === 0 ? 0 : -260;
    },
  },
  created() {
    console.log("Container.vue");
  },
};
</script>
<style>
</style>