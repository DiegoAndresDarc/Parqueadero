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
export default {
  name: 'app',
  components: {
    login:Login
  },
  data () {
    return {
      LoggedIn: false
    };
  },
  methods: {
    login(response) {
      this.LoggedIn = true;
    },
    async checkSession() {
      const response = await this.$axios.get("MainServlet/checkSession");
      this.LoggedIn = response.data != null ? true : false;
      console.log(response.data)
    },
    async logout(){
      const logout = await this.$$axios.get("MainServlet/logout");
      this.LoggedIn = false;
    }
  },
  created() {
    this.checkSession();
    console.log("App.vue");
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
