<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: "app",
  components: {},
  data() {
    return {
      LoggedIn: false,
    };
  },
  methods: {
    logout() {
      this.$$axios
        .get("MainServlet/logout")
        .then((response) => {
          this.LoggedIn = false;
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  created() {
    console.log("App.vue");
  },
};
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
