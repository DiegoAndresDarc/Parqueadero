<template>
  <div class="set-parking">
    <div class="content">
      <form @submit.prevent="setParking" autocomplete="off">
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Seleccione el parqueadero a asignar</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control is-expanded">
                <div class="select is-fullwidth">
                  <select v-model="parqueaderoSeleccionado">
                    <option
                      v-for="parqueadero in parqueaderos"
                      :value="parqueadero"
                      v-bind:key="parqueadero.id"
                    >
                      {{ parqueadero.codigo }}
                    </option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Seleccione el residente</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control is-expanded">
                <div class="select is-fullwidth">
                  <select v-model="usuarioSeleccionado">
                    <option
                      v-for="usuario in usuarios"
                      :value="usuario"
                      v-bind:key="usuario.id"
                    >
                      {{ usuario.nombres }} {{ usuario.apellidos }}
                    </option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="field">
          <div class="control">
            <button class="button is-link is-fullwidth">
              Asignar Parqueadero
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "setParking",
  data() {
    return {
      mssg: "Parqueadero dado con éxito",
      parqueaderos: [],
      parqueaderoSeleccionado: {},
      usuarios: [],
      usuarioSeleccionado: [],
    };
  },
  methods: {
    loadParkings() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      this.parqueaderos = [];
      this.parqueaderoSeleccionado = {};
      var requestObject = {
        tabla: "parqueadero",
        id_copropiedad: this.$session.get("id_coprop"),
        esta_libre: 1,
        esta_asignado: 0,
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
    setParking() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/update.php";
      this.parqueaderoSeleccionado.tabla = "parqueadero";
      this.parqueaderoSeleccionado.id_usuario = this.usuarioSeleccionado.id;
      this.parqueaderoSeleccionado.esta_libre = 0;
      this.parqueaderoSeleccionado.esta_asignado = 1;
      this.$axios
        .post(url, this.parqueaderoSeleccionado)
        .then((response) => {
          if (response.data == true) alert(this.mssg);
          this.loadParkings();
          this.loadUsers();
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  beforeCreate() {
    this.$bus.$emit("checkSession", "");
  },
  created() {
    this.loadParkings();
    this.loadUsers();
  },
};
</script>

<style scope>
.label {
  color: black;
}
</style>