<template>
  <div class="login">
    <div class="head">
      <nav class="navbar"></nav>
    </div>
    <div class="content-login">
      <div class="box clogin">
        <div class="field">
          <form
            @submit.prevent.once="loginUser()"
            autocomplete="off"
            name="form"
          >
            <h1 class="subtitle is-size-3">Incio de Sesión</h1>
            <div class="field">
              <div class="control has-icons-left">
                <input
                  class="input is-medium"
                  type="text"
                  placeholder="Usuario"
                  id="usuario"
                  v-model="info.usuario"
                  autocomplete="off"
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
                  v-model="info.password"
                  autocomplete="new-password"
                  required
                />
                <span class="icon is-small is-left">
                  <i class="mdi mdi-lock"></i>
                </span>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <transition name="slide">
                  <p v-if="invalidData" class="help is-danger is-medium">
                    Usuario o contraseña incorrectos
                  </p>
                </transition>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <transition name="slide">
                  <p v-if="error" class="help is-danger is-medium">
                    Hubo un error en la comunicación con el servidor. Si
                    persiste, por favor pongase en contacto con el administrador
                    de la página
                  </p>
                </transition>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <button class="button is-colorcustom">Iniciar Sesión</button>
              </div>
            </div>
          </form>
        </div>
        <div class="field">
          <div class="control">
            <p>
              ¿No tienes una cuenta?
              <router-link to="/signup">Crear cuenta</router-link>
            </p>
          </div>
        </div>
        <div class="field">
          <div class="control">
            <p>
              ¿Olvidaste la contraseña?
              <router-link to="/recoverPassword"
                >Recuperar contraseña</router-link
              >
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="foot">
      <nav class="navbar"></nav>
    </div>
  </div>
</template>
<script>
import * as crypto from "crypto-js";
export default {
  name: "login",
  components: {},
  data() {
    return {
      error: false,
      LoggedIn: false,
      invalidData: false,
      loginInfo: {},
      info: {
        usuario: "",
        password: "",
      },
    };
  },
  methods: {
    loginUser() {
      this.info.password = crypto.SHA512(this.info.password).toString();
      this.$axios
        .post("MainServlet/login", this.info)
        .then((response) => {
          if (response) {
            var loginInfo = response.data;
            this.$router.replace({ name: "Home" });
            localStorage.nombres = loginInfo.nombres;
            localStorage.apellidos = loginInfo.apellidos;
            localStorage.usuario = loginInfo.usuario;
          } else {
            this.invalidData = true;
            this.cleanMessages();
          }
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
          this.cleanMessages();
        });
    },
    cleanMessages() {
      this.seg = 0;
      setInterval(() => {
        this.seg += 1;
        if (this.seg === 3) {
          this.error = false;
          this.invalidData = false;
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
  text-decoration: underline;
}
.input {
  border-color: none;
  box-shadow: none;
  max-width: 100%;
  width: 100%;
}
</style>