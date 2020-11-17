<template>
  <div class="payment">
    <div class="content">
      <form @submit.prevent="singlePayment" autocomplete="off">
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Seleccione el usuario que paga</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <div class="select is-fullwidth">
                  <select v-model="usuarioSeleccionado">
                    <option
                      v-for="usuario in usuarios"
                      v-bind:key="usuario.id"
                      :value="usuario"
                    >
                      {{ usuario.nombres }} {{ usuario.apellidos }}
                    </option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal" v-if="usuarioSeleccionado.id">
          <div class="field-label">
            <label class="label">Seleccione el parqueadero que paga</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <div class="select is-fullwidth">
                  <select v-model="parqueaderoSeleccionado">
                    <option
                      v-for="parqueadero in parqueaderos"
                      v-bind:key="parqueadero.id"
                      :value="parqueadero"
                    >
                      {{ parqueadero.codigo }}
                    </option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="field">
          <div class="control">
            <button class="button is-link is-fullwidth">Realizar pago</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "singlePayment",
  data() {
    return {
      mssg: "Pago registrado con éxito",
      usuarios: [],
      usuarioSeleccionado: {},
      parqueaderos: [],
      parqueaderoSeleccionado: {},
    };
  },
  methods: {
    singlePayment() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/insert.php";
      var requestObject = {
        tabla: "pagos",
        id_usuario: this.usuarioSeleccionado.id,
        id_parqueadero: this.parqueaderoSeleccionado.id,
      };
      var date = new Date();
      requestObject.fecha_pago =
        date.getFullYear() + "/" + date.getMonth() + "/" + date.getDate();
      requestObject.hora_pago =
        date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
      this.$axios
        .post(url, requestObject)
        .then((response) => {
          if (response.data == true) {
            alert(this.mssg);
            this.usuarioSeleccionado={};
          }
        })
        .catch((e) => {
          console.log(e);
        });
    },
    loadUsers() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      this.usuarioSeleccionado = {};
      this.usuarios = [];
      var requestObject = {
        tabla: "usuario",
        id_copropiedad: this.$session.get("id_coprop"),
        tipo_usuario: "R",
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          this.usuarios = response.data;
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
    },
    loadParkings() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      this.parqueaderos = [];
      this.parqueaderoSeleccionado = {};
      var requestObject = {
        tabla: "parqueadero",
        id_usuario: this.usuarioSeleccionado.id,
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          this.parqueaderos = response.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  watch: {
    usuarioSeleccionado(newValue) {
      if (newValue.id) this.loadParkings();
    },
  },
  beforeCreate() {
    this.$bus.$emit("checkSession", "");
  },
  created() {
    this.loadUsers();
  },
};
</script>

<style>
</style>