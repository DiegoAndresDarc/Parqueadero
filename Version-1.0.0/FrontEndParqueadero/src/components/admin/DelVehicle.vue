<template>
  <div class="vehicle">
    <div class="content">
      <form @submit.prevent="delVehicle" autocomplete="off">
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
            <button class="button is-link is-fullwidth">Eliminar</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "delVehicle",
  data() {
    return {
      mssg: "Vehiculo eliminado con éxito",
      usuarios: [],
      usuarioSeleccionado: {},
      vehiculos: [],
      vehiculoSeleccionado: {},
    };
  },
  methods: {
    delVehicle() {
      var url =
        jsonInfo.url_server + jsonInfo.name_app + "/admin/delVehicle.php";
      this.vehiculoSeleccionado.tabla = "vehiculo";
      this.$axios
        .post(url, this.vehiculoSeleccionado)
        .then((response) => {
          if (response.data == true) alert(this.mssg);
          this.vehiculoSeleccionado = {};
          this.loadVehicles();
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