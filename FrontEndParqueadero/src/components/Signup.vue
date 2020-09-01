<template>
  <div class="signup">
    <div class="content-signup">
      <h1>Registro</h1>
      <div class="field">
        <form @submit.prevent="signup()" autocomplete="off">
          <div class="field">
            <label class="label">Nombres Completos</label>
            <div class="control">
              <input
                class="input is-medium"
                type="text"
                placeholder="Nombres"
                id="nombres"
                required
              />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <input
                class="input is-medium"
                type="text"
                placeholder="Apellidos"
                id="apellidos"
                required
              />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <input
                class="input is-medium"
                type="text"
                placeholder="Usuario"
                id="usuario"
                required
              />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <input
                class="input is-medium"
                type="password"
                placeholder="Contraseña"
                id="password"
                required
              />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <input
                class="input is-medium"
                type="email"
                placeholder="Correo electrónico"
                id="email"
                required
              />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <input
                class="input is-medium"
                type="tel"
                pattern="[0-9]{7}"
                title="Un número de telefono fijo tiene una longitud de 7 digitos con números entre 0 y 9"
                placeholder="telefono fijo"
                id="telefono"
                required
              />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <input
                class="input is-medium"
                type="tel"
                pattern="[3]{1}[0-9]{9}"
                title="Un número de celular en Colombia inicia con el número 3 y tiene una longitud de 10 digitos con números entre 0 y 9"
                placeholder="celular"
                id="celular"
                required
              />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-link is-fullwidth is-medium" type="submit">Registro</button>
            </div>
          </div>
        </form>
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
          <button
            class="button is-fullwidth is-medium is-link is-light"
            v-on:click="cancelar"
          >Cancelar</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "signup",
  components: {},
  data() {
    return {
      mssg: "Registro exitoso",
      error: false
    };
  },
  methods: {
    signup() {
      const txtnombres = document.getElementById("nombres");
      const txtapellidos = document.getElementById("apellidos");
      const txtusuario = document.getElementById("usuario");
      const txtpassword = document.getElementById("password");
      const txtemail = document.getElementById("email");
      const txttelefono = document.getElementById("telefono");
      const txtcelular = document.getElementById("celular");
      var responseObject = {
        nombres: txtnombres.value,
        apellidos: txtapellidos.value,
        usuario: txtusuario.value,
        password: txtpassword.value,
        email: txtemail.value,
        telefono: txttelefono.value,
        celular: txtcelular.value,
      };
      console.log(responseObject);
      this.$axios
        .post("MainServlet/signup", responseObject)
        .then((response) => {
          if (response) {
            var loginInfo = {
              response: response.data,
            };
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
      console.log("registro");
    },
    cancelar(event) {
      //Limpiar la pantalla
      this.$router.push("/");
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
    console.log("Sigup.vue");
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