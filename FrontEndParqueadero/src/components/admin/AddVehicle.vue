<template>
  <div class="vehicle">
    <div class="content">
      <form @submit.prevent="addVehicle" autocomplete="off">
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Seleccione el propietario del vehículo</label>
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
            <label class="label">Modelo del vehículo</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="text"
                  placeholder="modelo del vehículo"
                  v-model="info.modelo"
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
                  <select v-model="info.tipo">
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
            <label class="label">Peso del vehículo</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="number"
                  placeholder="peso del vehículo"
                  v-model="info.peso"
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
                  v-model="info.numero_ejes"
                  min="0"
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
                  v-model="info.fecha_vencimiento_soat"
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
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="file"
                  placeholder=""
                  name="soat"
                  accept=".pdf"
                  @change="getSOAT"
                  required
                />
              </div>
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
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="file"
                  placeholder=""
                  name="carta_propiedad"
                  accept=".pdf"
                  @change="getOwnerShip"
                  required
                />
              </div>
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
</template>

<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "addVehicle",
  data() {
    return {
      mssg: "Vehiculo añadido con éxito",
      info: {},
      usuarios: [],
      usuarioSeleccionado: {},
      soat: "",
      carta_propiedad: "",
    };
  },
  methods: {
    addVehicle() {
      var fileName =
        this.usuarioSeleccionado.id +
        this.info.marca +
        this.info.modelo +
        "_SOAT.pdf";
      this.uploadFile(fileName, this.soat);
      fileName =
        this.usuarioSeleccionado.id +
        this.info.marca +
        this.info.modelo +
        "_OwnerShip.pdf";
      this.uploadFile(fileName, this.carta_propiedad);
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/insert.php";
      this.id_propietario = this.usuarioSeleccionado.id;
      this.info.tabla = "vehiculo";
      this.info.marca = this.info.marca.toUpperCase();
      this.info.modelo = this.info.modelo.toUpperCase();
      console.log(this.info);
      console.log(this.soat);
      console.log(this.carta_propiedad);
      this.$axios
        .post(url, this.info)
        .then((response) => {
          if (response.data == true) alert(this.mssg);
          this.info = {};
        })
        .catch((e) => {
          console.log(e);
        });
    },
    uploadFile(fileName, file) {
      var url =
        jsonInfo.url_server + jsonInfo.name_app + "/admin/uploadFile.php";
      var formData = new FormData();
      formData.append(fileName, file);
      this.$axios
        .post(url, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          console.log(response);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    getSOAT(event) {
      this.soat = event.target.files[0];
    },
    getOwnerShip(event) {
      this.carta_propiedad = event.target.files[0];
    },
    loadUsers() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      this.usuarioSeleccionado = {};
      this.usuarios = [];
      var requestObject = {
        tabla: "usuario",
        id_copropiedad: this.$session.get("id_coprop"),
        tipo_usuario: "C",
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