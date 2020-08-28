<template>
  <div>
    <div class="content-login">
      <div class="box login">
        <div class="field">
          <form @submit.prevent="login()" autocomplete="off" name="form">
            <h1 class="subtitle has-text-link is-size-3">Incio de Sesión</h1>
            <div class="field">
              <div class="control has-icons-left">
                <input
                  class="input is-medium"
                  type="text"
                  placeholder="Usuario"
                  id="usuario"
                  required
                />
                <span class="icon is-small is-left">
                  <i class="mdi mdi-account"></i>
                </span>
              </div>
            </div>
            <div class="field">
              <div class="control has-icons-left">
                <input
                  class="input is-medium"
                  type="password"
                  placeholder="Contraseña"
                  id="password"
                  required
                />
                <span class="icon is-small is-left">
                  <i class="mdi mdi-lock"></i>
                </span>
              </div>
            </div>
            <transition name="slide">
              <p v-if="error" class="help is-danger">Datos incorrectos</p>
            </transition>
            <div class="control">
              <button class="button is-info is-fullwidth is-medium">Iniciar Sesión</button>
            </div>
          </form>
        </div>
        <div class="field">
          <div class="control">
            <p>
              ¿No tienes una cuenta?
              <a href="#">Crear cuenta</a>
            </p>
          </div>
        </div>
        <div class="field">
          <div class="control">
            <p>
              ¿Olvidaste la contraseña?
              <a href="#">Recuperar contraseña</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "login",
  components: {},
  data() {
    return {
      error: false,
    };
  },
  methods: {
    async login() {
      console.log("metodo de login");
      var responseObject = {
        usuario: document.getElementById("usuario").value,
        password: document.getElementById("password").value,
      };
      console.log(responseObject);
      const response = await this.$axios.post(
        "MainServlet/login",
        responseObject
      );
      if (response) {
        var loginInfo = {
          response: response.data,
        };
        this.$emit("login:loginInfo", loginInfo);
      } else {
        this.error = true;
        this.cleanMgsError();
      }
      //console.log(forms);
    },
    cleanMgsError() {
      this.seg = 0;
      setInterval(() => {
        this.seg += 1;
        if (this.seg === 3) {
          this.error = false;
        }
      }, 2000);
    },
  },
  created() {
    console.log("Login.vue");
  },
};
</script>
<style>
h1,
h2 {
  font-weight: normal;
}
a {
  color: #42b983;
}
.input {
  background-color: #fff;
  border-color: none;
  box-shadow: none;
  max-width: 100%;
  width: 100%;
}
</style>