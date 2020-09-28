<template>
  <div class="signup">
    <div class="head">
      <nav class="navbar"></nav>
    </div>
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
                v-model="info.identificacion"
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
                v-model="info.nombres"
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
                v-model="info.apellidos"
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
                v-model="info.usuario"
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
                v-model="info.password"
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
                v-model="info.email"
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
                v-model="info.telefono"
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
                v-model="info.celular"
                required
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Seleccione la copropiedad a la cual pertenece</label>
            <div class="control">
              <div class="select">
                <select v-model="copropSeleccionada">
                  <option>{{selectCoprop}}</option>
                  <option
                    v-for="coprop in coprops"
                    :value="coprop"
                    v-bind:key="coprop.id"
                  >{{coprop.nombre}}</option>
                </select>
              </div>
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-colorcustom">Registro</button>
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
          <button class="button is-colorcustom" v-on:click="cancelar">Cancelar</button>
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
import jsonInfo from "../../assets/info.json";
export default {
  name: "signup",
  components: {},
  data() {
    return {
      mssg: "Registro exitoso",
      error: false,
      tipo_doc: "CC",
      tipo_usr: "C",
      info: {
        tabla: "",
        nombres: "",
        apellidos: "",
        usuario: "",
        password: "",
        email: "",
        telefono: "",
        celular: "",
        identificacion: "",
        tipo_identificacion: "",
        tipo_usuario: "",
        id_copropiedad:"",
      },
      coprops: [],
      copropSeleccionada: {},
      selectCoprop: "Seleccione una copropiedad...",
    };
  },
  methods: {
    loadCoprops() {
      this.copropSeleccionada = {};
      this.coprops = [];
      var requestObject = {
        tabla: "copropiedad",
        signup: "",
      };
      this.$axios
        .post("MainServlet/getInformation", requestObject)
        .then((response) => {
          this.coprops = response.data;
          console.log(this.coprops);
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
    },
    signup() {
      this.info.tabla = "usuario";
      this.info.nombres = this.info.nombres.toUpperCase();
      this.info.apellidos = this.info.apellidos.toUpperCase();
      this.info.password = crypto.SHA512(this.info.password).toString();
      this.info.email = this.info.email.toUpperCase();
      this.info.tipo_usuario = this.tipo_usr;
      this.info.tipo_identificacion = this.tipo_doc;
      this.info.id_copropiedad = this.copropSeleccionada.id;
      console.log(this.info);
      this.$axios
        .post("http://localhost/parqueadero/globals/signup.php", this.info)
        .then((response) => {
          alert(this.mssg);
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
    this.loadCoprops();
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