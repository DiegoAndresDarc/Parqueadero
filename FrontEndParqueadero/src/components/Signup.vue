<template>
  <div class="signup">
    <div class="box clogin content-signup">
      <h1>Registro</h1>
      <div class="field">
        <form @submit.prevent.once="signup()" autocomplete="off">
          <div class="control">
            <label class="label">Tipo y número de documento</label>
          </div>
          <div class="field has-addons">
            <div class="control">
              <div class="select">
                <select v-model="tipo_doc">
                  <option>CC</option>
                  <option>CE</option>
                </select>
              </div>
            </div>
            <div class="control">
              <input
                class="input is-expanded"
                type="number"
                placeholder="numero de documento"
                id="identificacion"
                required
              />
            </div>
          </div>
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
            <label class="label">Apellidos</label>
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
            <label class="label">Usuario</label>
            <div class="control">
              <input
                class="input is-medium"
                type="text"
                placeholder="Usuario"
                id="usuario"
                autocomplete="off"
                required
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Contraseña</label>
            <div class="control">
              <input
                class="input is-medium"
                type="password"
                placeholder="Contraseña"
                id="password"
                autocomplete="new-password"
                required
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Dirección de correo electrónico</label>
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
            <label class="label">Número de teléfono fijo</label>
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
            <label class="label">Número de teléfono celular</label>
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
              <button class="button is-colorcustom" type="submit">Registro</button>
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
            class="button is-colorcustom"
            v-on:click="cancelar"
          >Cancelar</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import * as crypto from "crypto-js";
export default {
  name: "signup",
  components: {},
  data() {
    return {
      mssg: "Registro exitoso",
      error: false,
      tipo_doc: "CC",
      tipo_usr: "C",
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
      const txtidentificacion = document.getElementById("identificacion");
      var responseObject = {
        tabla: "usuario",
        nombres: txtnombres.value.toUpperCase(),
        apellidos: txtapellidos.value.toUpperCase(),
        usuario: txtusuario.value,
        password: crypto.SHA512(txtpassword.value).toString(),
        email: txtemail.value.toUpperCase(),
        telefono: txttelefono.value,
        celular: txtcelular.value,
        identificacion: txtidentificacion.value,
        tipo_identificacion: this.tipo_doc,
        tipo_usuario: this.tipo_usr,
      };
      console.log(responseObject);
      this.$axios
        .post("MainServlet/signup", responseObject)
        .then((response) => {
          this.$router.push("/login");
          console.log("registro");
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
          this.cleanMessages();
        });
    },
    cancelar(event) {
      //Limpiar la pantalla
      this.$router.push("/login");
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
.label {
  text-align: left;
}
</style>