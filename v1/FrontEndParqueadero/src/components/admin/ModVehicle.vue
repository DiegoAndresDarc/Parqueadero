<template>
  <div class="vehicle">
    <div class="content">
      <div class="field">
        <div class="control">
          <form @submit.prevent="selVehicle" autocomplete="off">
            <div class="field is-horizontal">
              <div class="field-label">
                <label class="label"
                  >Seleccione el propietario del vehículo</label
                >
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
                <label class="label">Seleccione el vehículo</label>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <div class="select is-fullwidth">
                      <select v-model="vehiculoSeleccionado">
                        <option
                          v-for="vehiculo in vehiculos"
                          v-bind:key="vehiculo.id"
                          :value="vehiculo"
                        >
                          {{ vehiculo.tipo }} {{ vehiculo.marca }}
                          {{ vehiculo.modelo }} {{ vehiculo.color }}
                        </option>
                      </select>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <button class="button is-link is-fullwidth">Modificar</button>
              </div>
            </div>
          </form>
        </div>
      </div>
      <div class="field" v-show="selectedVehicle">
        <div class="control">
          <form @submit.prevent="modVehicle" autocomplete="off">
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
                      v-model="vehiculoSeleccionado.marca"
                      required
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label">Modelo del vehículo</label>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <input
                      class="input"
                      type="text"
                      placeholder="modelo del vehículo"
                      v-model="vehiculoSeleccionado.modelo"
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
                      <select v-model="vehiculoSeleccionado.tipo">
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
                <label class="label">Color del vehículo</label>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <input
                      class="input"
                      type="text"
                      placeholder="color del vehículo"
                      v-model="vehiculoSeleccionado.color"
                      required
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label">Peso del vehículo</label>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <input
                      class="input"
                      type="number"
                      placeholder="peso del vehículo"
                      v-model="vehiculoSeleccionado.peso"
                      min="0"
                      step="any"
                      required
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label">Número de ejes del vehículo</label>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <input
                      class="input"
                      type="number"
                      placeholder="número de ejes del vehículo"
                      v-model="vehiculoSeleccionado.numero_ejes"
                      min="0"
                      required
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label" for="color">Placa del vehículo</label>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <input
                      id="placa"
                      class="input"
                      type="text"
                      placeholder="placa del vehículo"
                      v-model="vehiculoSeleccionado.placa"
                      required
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label">
                <label class="label">Fecha de vencimiento del SOAT</label>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <input
                      class="input"
                      type="date"
                      placeholder="fecha de vencimiento del SOAT del vehículo"
                      v-model="vehiculoSeleccionado.fecha_vencimiento_soat"
                      required
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label">Soporte en formato pdf del SOAT</label>
              </div>
              <div class="field-body">
                <div class="file has-name">
                  <label class="file-label">
                    <input
                      class="file-input"
                      type="file"
                      accept=".pdf"
                      @change="getSOAT"
                    />
                    <span class="file-cta">
                      <span class="file-icon">
                        <i class="mdi mdi-upload"></i>
                      </span>
                      <span class="file-label">Escoge un archivo</span>
                    </span>
                    <span class="file-name">
                      {{ nombreArchivoSoat }}
                    </span>
                  </label>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label">
                <label class="label"
                  >Soporte en formato pdf de la carta de propiedad</label
                >
              </div>
              <div class="field-body">
                <div class="file">
                  <label class="file-label">
                    <input
                      class="file-input"
                      type="file"
                      accept=".pdf"
                      @change="getOwnerShip"
                    />
                    <span class="file-cta">
                      <span class="file-icon">
                        <i class="mdi mdi-upload"></i>
                      </span>
                      <span class="file-label">Escoge un archivo</span>
                    </span>
                    <span class="file-name">
                      {{ nombreArchivoCartaPropiedad }}
                    </span>
                  </label>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label">
                <label class="label">Foto/Imagen del vehículo</label>
              </div>
              <div class="field-body">
                <div class="file">
                  <label class="file-label">
                    <input
                      class="file-input"
                      type="file"
                      accept=".jpeg"
                      @change="getVehicleImg"
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
                <button class="button is-link is-fullwidth">Aceptar</button>
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
  name: "modVehicle",
  data() {
    return {
      mssg: "Vehiculo modificado con éxito",
      selectedVehicle: false,
      usuarios: [],
      usuarioSeleccionado: {},
      vehiculos: [],
      vehiculoSeleccionado: {},
      soat: "",
      cartaPropiedad: "",
      imagenVehiculo: "",
      nombreArchivoSoat: "",
      nombreArchivoCartaPropiedad: "",
      nombreImagenVehiculo: "",
    };
  },
  methods: {
    modVehicle() {
      var url =
        jsonInfo.url_server + jsonInfo.name_app + "/admin/modVehicle.php";
      this.vehiculoSeleccionado.tabla = "vehiculo";
      this.vehiculoSeleccionado.marca = this.vehiculoSeleccionado.marca.toUpperCase();
      this.vehiculoSeleccionado.modelo = this.vehiculoSeleccionado.modelo.toUpperCase();
      this.vehiculoSeleccionado.color = this.vehiculoSeleccionado.color.toUpperCase();
      this.vehiculoSeleccionado.placa = this.vehiculoSeleccionado.placa.toUpperCase();
      if (this.soat) this.vehiculoSeleccionado.soat = this.soat;
      if (this.cartaPropiedad)
        this.invehiculoSeleccionadofo.carta_propiedad = this.cartaPropiedad;
      if (this.imagenVehiculo)
        this.vehiculoSeleccionado.foto = this.imagenVehiculo;
      this.$axios
        .post(url, this.vehiculoSeleccionado)
        .then((response) => {
          if (response.data == true) alert(this.mssg);
          this.vehiculoSeleccionado = {};
          this.nombreArchivoSoat = "";
          this.nombreArchivoCartaPropiedad = "";
          this.nombreImagenVehiculo = "";
          this.selectedVehicle = false;
          console.log(response.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    selVehicle() {
      this.selectedVehicle = true;
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
        });
    },
    loadVehicles() {
      var url =
        jsonInfo.url_server + jsonInfo.name_app + "/admin/getUserVehicles.php";
      this.vehiculoSeleccionado = {};
      this.vehiculos = [];
      var requestObject = {
        id_propietario: this.usuarioSeleccionado.id,
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          this.vehiculos = response.data;
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
    },
    getSOAT(event) {
      var file = event.target.files[0];
      this.nombreArchivoSoat = file.name;
      var app = this;
      var reader = new FileReader();
      reader.onloadend = function (e) {
        if (e.target.readyState == FileReader.DONE) {
          const b64 = e.target.result.split(",")[1];
          app.soat = b64;
        }
      };
      reader.readAsDataURL(file);
    },
    getOwnerShip(event) {
      var file = event.target.files[0];
      this.nombreArchivoCartaPropiedad = file.name;
      var reader = new FileReader();
      var app = this;
      reader.onloadend = function (e) {
        if (e.target.readyState == FileReader.DONE) {
          const b64 = e.target.result.split(",")[1];
          app.cartaPropiedad = b64;
        }
      };
      reader.readAsDataURL(file);
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
  },
  watch: {
    usuarioSeleccionado(newValue) {
      if (newValue.id) this.loadVehicles();
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