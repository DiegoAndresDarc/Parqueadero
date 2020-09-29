<template>
  <div class="adduser">
    <div class="content-adduser">
      <div class="field">
        <form @submit.prevent.once="addUser" autocomplete="off">
          <div class="field">
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
                  v-model="info.identificacion"
                  required
                />
              </div>
            </div>
          </div>
          <div class="field">
            <label class="label">Nombres Completos</label>
            <div class="control">
              <input
                class="input is-medium"
                type="text"
                placeholder="Nombres"
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
                v-model="info.password"
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
                v-model="info.celular"
                required
              />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <label class="label">Tipo de usuario</label>
            </div>
            <div class="field">
              <div class="control">
                <div class="select">
                  <select v-model="tipo_usr">
                    <option v-if="root_admin === 'R'">Administrador</option>
                    <option>Cliente</option>
                    <option>Guardia de seguridad</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
          <div class="field" v-if="apartamentos.length">
            <label class="label"
              >Seleccione el apartamento al cual pertenece</label
            >
            <div class="control">
              <div class="select">
                <select v-model="apartSeleccionado">
                  <option>{{ selectApart }}</option>
                  <option
                    v-for="apto in apartamentos"
                    :value="apto"
                    v-bind:key="apto.id"
                  >
                    {{ apto.bloque }} | {{apto.apartamento}}
                  </option>
                </select>
              </div>
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-link is-fullwidth">
                Agregar usuario
              </button>
            </div>
          </div>
        </form>
      </div>
      <div class="field">
        <div class="control">
          <transition name="slide">
            <p v-if="error" class="help is-danger is-medium">
              Hubo un error en la comunicación con el servidor. Si persiste, por
              favor pongase en contacto con el administrador de la página
            </p>
          </transition>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import * as crypto from "crypto-js";
import jsonInfo from "../../assets/info.json";
export default {
  name: "addUser",
  components: {},
  data() {
    return {
      error: false,
      mssg: "Registro exitoso",
      tipo_doc: "CC",
      tipo_usr: "Cliente",
      root_admin: "",
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
      },
      id_copropiedad: "",
      apartamentos: [],
      apartSeleccionado: {},
      selectApart: "Seleccione un apartamento...",
    };
  },
  methods: {
    loadApartments() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      this.id_copropiedad = this.$session.get("id_coprop");
      this.apartamentos = [];
      this.apartSeleccionado = {};
      var requestObject = {
        tabla: "apartamento",
        id_copropiedad: this.id_copropiedad,
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          this.apartamentos = response.data;
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
    },
    addUser() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/insert.php";
      this.info.tabla = "usuario";
      this.info.nombres = this.info.nombres.toUpperCase();
      this.info.apellidos = this.info.apellidos.toUpperCase();
      this.info.password = crypto.SHA512(this.info.password).toString();
      this.info.email = this.info.email.toUpperCase();
      this.info.tipo_usuario = this.tipo_usr.charAt(0);
      this.info.tipo_identificacion = this.tipo_doc;
      if (this.root_admin == "A") {
        this.info.id_copropiedad = this.id_copropiedad;
      }
      if (this.apartSeleccionado.length) {
        this.info.id_apartamento = this.apartSeleccionado.id_copropiedad;
      }
      console.log(this.info);
      this.$axios
        .post(url, this.info)
        .then((response) => {
          if (response.data == true) alert(this.mssg);
          this.info = {};
         this.apartSeleccionado = {};
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
          this.cleanMessages();
        });
    },
  },
  beforeCreate() {
    this.$bus.$emit("checkSession", "");
  },
  created() {
    this.root_admin = this.$session.get("user");
    this.loadApartments();
    console.log("Adduser.vue");
  },
};
</script>
<style>
</style>