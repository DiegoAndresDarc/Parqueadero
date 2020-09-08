<template>
  <div id="app">
    <router-view />
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
    checkSession() {
      this.$axios
        .get("MainServlet/checkSession")
        .then((response) => {
          this.LoggedIn = response.data != null ? true : false;
          if (this.LoggedIn) {
            this.$router.push("/Home");
          } else {
            this.$router.push("/login");
          }
        })
        .catch((e) => {
          console.log(e);
          this.LoggedIn = false;
          this.$router.push("/login");
        });
    },
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
    this.checkSession();
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
  color: #502c4e;
  margin-top: 60px;
}
</style>
