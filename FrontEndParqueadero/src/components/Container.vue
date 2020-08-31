<template>
  <div id="container">
    <div class="content-container">
      <Motion :value="offset" tag="div">
        <div
          class="motion"
          slot-scope="props"
          :style="{ transform: `translateX(${props.value}px)` }"
        >
          <menu></menu>
        </div>
      </Motion>
    </div>
  </div>
</template>
<script>
import Menu from "./Menu.vue";
export default {
  name: "container",
  components: {
    menu: Menu,
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
      this.showMenu();
    console.log("Container.vue");
  },
};
</script>
<style>
</style>