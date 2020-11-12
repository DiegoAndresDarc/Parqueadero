<template>
  <div class="guard">
    <div class="content">
      <div class="field" v-if="!turno_iniciado">
        <div class="control">
          <h2>
            Para realizar esta función se debe haber iniciado la jornada laboral
          </h2>
        </div>
      </div>
      <div class="field" v-else>
        <div class="control">
          <form @submit.prevent="viewParkingInfo" autocomplete="off">
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label">Código de barras del parqueadero</label>
              </div>
              <div class="field-body">
                <input
                  class="input"
                  type="password"
                  v-model="codigo_barras"
                  required
                />
              </div>
            </div>
            <div class="field">
              <div class="control">
                <button class="button is-fullwidth is-link">Aceptar</button>
              </div>
            </div>
          </form>
        </div>
      </div>
      <div class="field" v-show="selected">
        <div class="control">
          <div class="field" v-if="vehiculos.length">
            <label class="label">Vehiculo(s) usando el parqueadero</label>
            <div class="control">
              <table class="table is-fullwidth is-bordered is-striped">
                <thead>
                  <tr>
                    <th>Vehiculo</th>
                    <th>Acción</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="vehiculo in vehiculos" v-bind:key="vehiculo.id">
                    <td>
                      <img :src="vehiculo.foto" height="150px" width="150px" />
                    </td>
                    <td style="text-align: center; vertical-align: middle">
                      <button
                        type="submit"
                        class="button is-link is-fullwidth"
                        @click.once="goOutVehicle(vehiculo)"
                      >
                        Dar salida
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div class="field" v-else>
            <div class="control">
              <label class="label"
                >No existen vehiculos usando el parqueadero</label
              >
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
  name: "goOutVehicle",
  data() {
    return {
      mssg: "La salida del vehiculo ha sido exitosa",
      fecha: "",
      codigo_barras: "",
      vehiculos: [],
      parqueadero: {},
      selected: false,
      turno_iniciado: false,
    };
  },
  methods: {
    viewParkingInfo() {
      this.loadParking();
      this.selected = true;
    },
    goOutVehicle(vehiculo) {
      var url =
        jsonInfo.url_server + jsonInfo.name_app + "/admin/goOutVehicle.php";
      var info = {
        id_vehiculo: vehiculo.id,
      };
      var date = new Date();
      info.fecha_salida =
        date.getFullYear() + "/" + date.getMonth() + "/" + date.getDate();
      info.hora_salida =
        date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
      this.$axios
        .post(url, info)
        .then((response) => {
          console.log(response.data);
          if (response.data == true) alert(this.mssg);
          this.selected = false;
          this.vehiculos = [];
        })
        .catch((e) => {
          console.log(e);
        });
    },
    loadParking() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      var requestObject = {
        tabla: "parqueadero",
        codigo_barras: this.codigo_barras,
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          this.parqueadero = response.data[0];
          this.loadVehicles();
        })
        .catch((e) => {
          console.log(e);
        });
    },
    loadVehicles() {
      var url =
        jsonInfo.url_server +
        jsonInfo.name_app +
        "/admin/getVehiclesInParking.php";
      this.vehiculos = [];
      var requestObject = {
        id_parqueadero: this.parqueadero.id,
        fecha_salida: "",
        hora_salida: "",
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          console.log(response.data);
          this.vehiculos = response.data;
          this.vehiculos.forEach((item) => {
            var url = jsonInfo.url_server + jsonInfo.name_app;
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
    if (this.$session.get("dinero") >= 0) {
      this.turno_iniciado = true;
    }
  },
};
</script>

<style>
</style>