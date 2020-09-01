<template>
  <div class="login">
    <div class="content-login">
      <div class="box clogin">
        <div class="field">
          <form @submit.prevent="loginUser()" autocomplete="off" name="form">
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
            <div class="field">
              <div class="control">
                <transition name="slide">
                  <p
                    v-if="invalidData"
                    class="help is-danger is-medium"
                  >Usuario o contraseña incorrectos</p>
                </transition>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <transition name="slide">
                  <p
                    v-if="error"
                    class="help is-danger is-medium"
                  >Hubo un error en la comunicación con el servidor. Si persiste, por favor pongase en contacto con el administrador de la página</p>
                </transition>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <button class="button is-info is-fullwidth is-medium">Iniciar Sesión</button>
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
              <router-link to="/recoverPassword">Recuperar contraseña</router-link>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Container from "./Container";
export default {
  name: "login",
  components: {
    container: Container,
  },
  data() {
    return {
      error: false,
      LoggedIn: false,
      invalidData: false,
    };
  },
  methods: {
    checkSession() {
      this.$axios
        .get("MainServlet/checkSession")
        .then((response) => {
          this.LoggedIn = response.data != null ? true : false;
        })
        .catch((e) => {
          console.log(e);
          this.LoggedIn = false;
        });
    },
    loginUser() {
      console.log("metodo de login");
      var responseObject = {
        usuario: document.getElementById("usuario").value,
        password: document.getElementById("password").value,
      };
      console.log(responseObject);
      this.$axios
        .post("MainServlet/login", responseObject)
        .then((response) => {
          if (response) {
            var loginInfo = {
              response: response.data,
            };
            this.$emit("login:loginInfo", loginInfo);
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
      //this.$router.push("/Home");
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
    this.checkSession();
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