<template>
  <div class="visit">
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
          <form @submit.prevent="getParking" autocomplete="off">
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
      <div class="field" v-show="disponible">
        <div class="control">
          <form @submit.prevent="goInVisit" autocomplete="off">
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label"
                  >Nombre completo del responsable del vehículo</label
                >
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <input
                      class="input"
                      type="text"
                      placeholder="nombre completo de la persona responsable del vehiculo"
                      v-model="info.nombre_responsable"
                      required
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label">Marca del vehículo</label>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <input
                      class="input"
                      type="text"
                      placeholder="marca del vehículo"
                      v-model="info.marca"
                      required
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label">Tipo de vehículo</label>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <div class="select is-fullwidth">
                      <select v-model="info.tipo_vehiculo">
                        <option>CARRO</option>
                        <option>MOTO</option>
                        <option>BICICLETA</option>
                      </select>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label" for="color">Color del vehículo</label>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <input
                      id="color"
                      class="input"
                      type="text"
                      placeholder="color del vehículo"
                      v-model="info.color"
                      required
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label">Foto del vehiculo</label>
              </div>
              <div class="field-body">
                <div class="file has-name">
                  <label class="file-label">
                    <input
                      class="file-input"
                      type="file"
                      accept=".jpeg"
                      @change="getVehicleImg"
                      required
                    />
                    <span class="file-cta">
                      <span class="file-icon">
                        <i class="mdi mdi-upload"></i>
                      </span>
                      <span class="file-label">Escoge un archivo</span>
                    </span>
                    <span class="file-name">
                      {{ nombreImagenVehiculo }}
                    </span>
                  </label>
                </div>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <button type="submit" class="button is-link is-fullwidth">
                  Dar entrada a visitante
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "goInVisit",
  data() {
    return {
      mssg: "Entrada de visitante exitosa",
      dinero: 0,
      turno_iniciado: false,
      codigo_barras: "",
      parqueadero: {},
      disponible: false,
      imagenVehiculo: "",
      nombreImagenVehiculo: "",
      info: {},
    };
  },
  methods: {
    getParking() {
      this.loadParking();
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
          if (this.parqueadero.tipo === "VISITANTE") {
            if (
              this.parqueadero.esta_libre == 1 &&
              this.parqueadero.esta_asignado == 0
            )
              this.disponible = true;
            else {
              alert("El parqueadero escogido no está disponible");
              this.disponible = false;
            }
          } else {
            this.disponible = false;
            alert(
              "El parqueadero escogido se utilizada para residentes del conjunto."
            );
          }
        })
        .catch((e) => {
          console.log(e);
        });
    },
    getVehicleImg(event) {
      var file = event.target.files[0];
      this.nombreImagenVehiculo = file.name;
      var reader = new FileReader();
      var app = this;
      reader.onloadend = function (e) {
        if (e.target.readyState == FileReader.DONE) {
          const b64 = e.target.result.split(",")[1];
          app.imagenVehiculo = b64;
        }
      };
      reader.readAsDataURL(file);
    },
    goInVisit() {
      var url =
        jsonInfo.url_server + jsonInfo.name_app + "/admin/insertVehicle.php";
      this.info.tabla = "registro_visitantes";
      this.info.visitante = "";
      this.info.nombre_responsable = this.info.nombre_responsable.toUpperCase();
      this.info.id_parqueadero = this.parqueadero.id;
      this.info.marca = this.info.marca.toUpperCase();
      this.info.color = this.info.color.toUpperCase();
      if (this.nombreImagenVehiculo) this.info.foto = this.imagenVehiculo;
      var date = new Date();
      this.info.fecha_entrada =
        date.getFullYear() + "/" + date.getMonth() + "/" + date.getDate();
      this.info.hora_entrada =
        date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
      console.log(this.info);
      this.$axios
        .post(url, this.info)
        .then((response) => {
          console.log(response.data);
          if (response.data == true) {
            alert(this.mssg);
            this.updateParking();
            this.disponible = false;
            window.print();
          }
          this.info = {};
          this.nombreImagenVehiculo = "";
        })
        .catch((e) => {
          console.log(e);
        });
    },
    updateParking() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/update.php";
      this.parqueadero.tabla = "parqueadero";
      this.parqueadero.esta_libre = 0;
      this.parqueadero.esta_asignado = 1;
      delete this.parqueadero.id_usario;
      console.log(this.parqueadero);
      this.$axios
        .post(url, this.parqueadero)
        .then((response) => {
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
    if (this.$session.get("dinero") >= 0) {
      this.turno_iniciado = true;
    }
  },
};
</script>

<style>
</style>