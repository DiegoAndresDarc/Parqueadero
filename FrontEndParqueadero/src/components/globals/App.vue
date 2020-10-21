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
      if (!this.$session.exists()) {
        if (this.$route.path !== "/login") {
          this.$router.replace("/login");
        }
      }
    },
    logout() {
      this.$session.destroy();
      this.LoggedIn = false;
      this.$router.replace("/login");
    },
  },
  created() {
    this.checkSession();
    this.$bus.$on("checkSession", this.checkSession);
    this.$bus.$on("logout", this.logout);
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
