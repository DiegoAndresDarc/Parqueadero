<template>
  <div class="adduser">
    <div class="content">
      <form @submit.prevent="addUser" autocomplete="off">
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Tipo y número de documento</label>
          </div>
          <div class="field-body">
            <div class="control is-narrow">
              <div class="select">
                <select v-model="tipo_doc">
                  <option>CC</option>
                  <option>CE</option>
                </select>
              </div>
            </div>
            <div class="field">
              <input
                class="input is-expanded is-fullwidth"
                type="number"
                placeholder="numero de documento"
                v-model="info.identificacion"
                required
              />
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Nombres Completos</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="text"
                  placeholder="Nombres"
                  v-model="info.nombres"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Apellidos</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="text"
                  placeholder="Apellidos"
                  v-model="info.apellidos"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Dirección de correo electrónico</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="email"
                  placeholder="Correo electrónico"
                  v-model="info.email"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Número de teléfono fijo</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="tel"
                  pattern="[0-9]{7}"
                  title="Un número de telefono fijo tiene una longitud de 7 digitos con números entre 0 y 9"
                  placeholder="telefono fijo"
                  v-model="info.telefono"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Número de teléfono celular</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="tel"
                  pattern="[3]{1}[0-9]{9}"
                  title="Un número de celular en Colombia inicia con el número 3 y tiene una longitud de 10 digitos con números entre 0 y 9"
                  placeholder="celular"
                  v-model="info.celular"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Tipo de usuario</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <div class="select is-fullwidth">
                  <select v-model="tipo_usr">
                    <option v-if="root_admin === 'R'">Administrador</option>
                    <option v-if="root_admin === 'A'">Residente</option>
                    <option v-if="root_admin === 'A'">
                      Guardia de seguridad
                    </option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal" v-if="tipo_usr !== 'Residente'">
          <div class="field-label is-normal">
            <label class="label">Usuario</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="text"
                  placeholder="Usuario"
                  v-model="info.usuario"
                  autocomplete="off"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal" v-if="tipo_usr !== 'Residente'">
          <div class="field-label is-normal">
            <label class="label">Contraseña</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="password"
                  placeholder="Contraseña"
                  v-model="info.password"
                  autocomplete="new-password"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal" v-if="root_admin === 'R'">
          <div class="field-label is-normal">
            <label class="label"
              >Seleccione la copropiedad al cual pertenece</label
            >
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <div class="select is-fullwidth">
                  <select v-model="copropSeleccionada">
                    <option
                      v-for="copropiedad in copropiedades"
                      :value="copropiedad"
                      v-bind:key="copropiedad.id"
                    >
                      {{ copropiedad.nombre }}
                    </option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div
          class="field is-horizontal"
          v-if="root_admin === 'A' && tipo_usr === 'Residente'"
        >
          <div class="field-label is-normal" v-if="apartamentos.length > 0">
            <label class="label"
              >Seleccione el apartamento al cual pertenece</label
            >
          </div>
          <div class="field-body" v-if="apartamentos.length > 0">
            <div class="field">
              <div class="control">
                <div class="select is-fullwidth">
                  <select v-model="apartSeleccionado">
                    <option
                      v-for="apto in apartamentos"
                      :value="apto"
                      v-bind:key="apto.id"
                    >
                      {{ apto.bloque }} | {{ apto.apartamento }}
                    </option>
                  </select>
                </div>
              </div>
            </div>
          </div>
          <div v-else>
            <p class="help is-danger is-medium field-body">
              Todavía no existen apartamentos en la copropiedad
            </p>
          </div>
        </div>
        <div class="field">
          <div class="control">
            <button class="button is-link is-fullwidth">Agregar usuario</button>
          </div>
        </div>
      </form>
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
      info: {},
      id_copropiedad: "",
      apartamentos: [],
      apartSeleccionado: {},
      copropiedades: [],
      copropSeleccionada: {},
    };
  },
  methods: {
    loadCoprops() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      this.copropiedades = [];
      this.copropSeleccionada = {};
      var requestObject = {
        tabla: "copropiedad",
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          this.copropiedades = response.data;
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
    },
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
      if (this.info.usuario && this.info.password) {
        this.info.password = crypto.SHA512(this.info.password).toString();
      }
      this.info.email = this.info.email.toUpperCase();
      this.info.tipo_usuario = this.tipo_usr.charAt(0);
      this.info.tipo_identificacion = this.tipo_doc;
      if (this.root_admin == "A") {
        this.info.id_copropiedad = this.id_copropiedad;
      } else {
        this.info.id_copropiedad = this.copropSeleccionada.id;
      }
      if (this.apartSeleccionado.length) {
        this.info.id_apartamento = this.apartSeleccionado.id_copropiedad;
      }
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
    if (this.root_admin == "R") {
      this.loadCoprops();
    } else {
      this.loadApartments();
    }
  },
};
</script>
<style scoped>
.label {
  color: black;
}
</style>