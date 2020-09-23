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
          if (!this.LoggedIn) {
            if (this.$route.path !== "/login") {
              this.$router.replace("/login");
            }
          }
        })
        .catch((e) => {
          console.log(e);
          this.LoggedIn = false;
          if (this.$route.path !== "/login") {
            this.$router.replace("/login");
          }
        });
    },
    logout() {
      this.$axios
        .get("MainServlet/logout")
        .then((response) => {
          this.$router.replace("/login");
        })
        .catch((e) => {
          console.log(e);
        });
      this.LoggedIn = false;
      localStorage.removeItem(usuario);
      localStorage.removeItem(nombres);
      localStorage.removeItem(apellidos);
    },
  },
  created() {
    this.checkSession();
    this.$bus.$on("checkSession", this.checkSession);
    this.$bus.$on("logout", this.logout);
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
