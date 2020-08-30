<template>
  <div id="app">
    <transition name="component-fade" mode="out-in">
      <login @login:loginInfo="login" v-if="!loggedIn"></login>
      <container v-else></container>
    </transition>
  </div>
</template>

<script>
import Login from "./Login";
import Container from "./Container";
export default {
  name: "app",
  components: {
    login: Login,
    container: Container
  },
  data() {
    return {
      LoggedIn: false,
    };
  },
  methods: {
    login(response) {
      this.LoggedIn = true;
    },
    checkSession() {
      this.$axios
        .get("MainServlet/checkSession")
        .then((response) => {
          this.LoggedIn = response.data != null ? true : false;
        })
        .catch((e) => {
          console.log(e);
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
  color: #2c3e50;
  margin-top: 60px;
}
</style>
