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
          <div class="field is-horizontal">
            <div class="field-label">
              <label class="label">Código del parqueadero</label>
            </div>
            <div class="field-body">
              <div class="field">
                <div class="control">
                  <h2 class="subtitle">{{ parqueadero.codigo }}</h2>
                </div>
              </div>
            </div>
          </div>
          <div class="field is-horizontal">
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
          <div class="field">
            <label class="label">Vehiculo(s) asignados al parqueadero</label>
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
                        @click.once="goInVehicle(vehiculo)"
                      >
                        Dar entrada
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
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
  name: "goInVehicle",
  data() {
    return {
      mssg: "La entrada del vehiculo ha sido exitosa",
      fecha: "",
      codigo_barras: "",
      vehiculos: [],
      usuario: {},
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
    goInVehicle(vehiculo) {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/insert.php";
      var info = {
        id_vehiculo: vehiculo.id,
        tabla: "registro_uso",
      };
      var date = new Date();
      info.fecha_ingreso =
        date.getFullYear() + "/" + (date.getMonth() + 1) + "/" + date.getDate();
      info.hora_ingreso =
        date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
      this.$axios
        .post(url, info)
        .then((response) => {
          if (response.data == true) alert(this.mssg);
          this.selected = false;
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
          this.loadUsers();
        })
        .catch((e) => {
          console.log(e);
        });
    },
    loadUsers() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      this.usuario = {};
      var requestObject = {
        tabla: "usuario",
        id: this.parqueadero.id_usuario,
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
    },
    loadVehicles() {
      var url =
        jsonInfo.url_server +
        jsonInfo.name_app +
        "/admin/getVehiclesInParking.php";
      this.vehiculos = [];
      var requestObject = {
        id_propietario: this.usuario.id,
        id_parqueadero: this.parqueadero.id,
        fecha_ingreso: "",
        hora_ingreso: "",
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
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
    if (this.$session.get("dinero") != null) {
      this.turno_iniciado = true;
    }
  },
};
</script>

<style>
</style>