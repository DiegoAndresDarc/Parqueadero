<template>
  <div class="parking">
    <div class="content">
      <div class="field">
        <div class="control">
          <form @submit.prevent="getParkingInfo" autocomplete="off">
            <div class="field is-horizontal">
              <div class="field-label">
                <label class="label"
                  >Seleccione el parqueadero a visualizar</label
                >
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
            <div class="field">
              <div class="control">
                <button class="button is-link is-fullwidth">
                  Visualizar Parqueadero
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
      <div class="field" v-show="selected">
        <div class="control">
          <div class="field is-horizontal">
            <div class="field-label">
              <label class="label">Código del parqueadero</label>
            </div>
            <div class="field-body">
              <div class="field">
                <div class="control">
                  <h2 class="subtitle">{{ parqueaderoSeleccionado.codigo }}</h2>
                </div>
              </div>
            </div>
          </div>
          <div class="field is-horizontal" v-if="usuario.length">
            <div class="field-label">
              <label class="label">Usuario del parqueadero</label>
            </div>
            <div class="field-body">
              <div class="field">
                <div class="control">
                  <h3>{{ usuario.nombres }} {{ usuario.apellidos }}</h3>
                </div>
              </div>
            </div>
          </div>
          <div class="field" v-else>
            <div class="control">
              <label class="label">El parqueadero está disponible</label>
            </div>
          </div>
          <div class="field" v-if="vehiculos.length">
            <label class="label">Vehiculo(s) asignados al parqueadero</label>
            <div class="control">
              <img
                v-for="vehiculo in vehiculos"
                v-bind:key="vehiculo.id"
                :src="vehiculo.foto"
                height="250px"
                width="250px"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "viewInfoParking",
  data() {
    return {
      mssg: "",
      parqueaderos: [],
      parqueaderoSeleccionado: {},
      usuario: {},
      usuarioSeleccionado: {},
      vehiculos: [],
      selected: false,
    };
  },
  methods: {
    getParkingInfo() {
      this.selected = true;
      this.loadUsers();
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
    },
    loadParkings() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      this.parqueaderos = [];
      this.parqueaderoSeleccionado = {};
      var requestObject = {
        tabla: "parqueadero",
        id_copropiedad: this.$session.get("id_coprop"),
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
      this.usuario = {};
      if (this.parqueaderoSeleccionado.id_usuario) {
        var requestObject = {
          tabla: "usuario",
          id: this.parqueaderoSeleccionado.id_usuario,
          tipo_usuario: "R",
        };
        this.$axios
          .get(url, { params: requestObject })
          .then((response) => {
            this.usuario = response.data[0];
            this.loadVehicles();
          })
          .catch((e) => {
            console.log(e);
            this.error = true;
          });
      }
    },
    loadVehicles() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      this.vehiculos = [];
      var requestObject = {
        tabla: "vehiculo",
        id_propietario: this.usuario.id,
        id_parqueadero: this.parqueaderoSeleccionado.id,
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          this.vehiculos = response.data;
          this.vehiculos.forEach((item) => {
            var url = jsonInfo.url_server + jsonInfo.name_app;
            item.soat = item.soat.replace("..", url);
            item.carta_propiedad = item.carta_propiedad.replace("..", url);
            item.foto = item.foto.replace("..", url);
          });
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
    },
  },
  beforeCreate() {
    this.$bus.$emit("checkSession", "");
  },
  created() {
    this.loadParkings();
  },
};
</script>

<style>
</style>