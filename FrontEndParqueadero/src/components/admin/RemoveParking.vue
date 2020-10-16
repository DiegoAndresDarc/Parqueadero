<template>
  <div class="set-parking">
    <div class="content">
      <div class="field">
        <div class="control">
          <form @submit.prevent="selUser" autocomplete="off">
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
                  Buscar Parqueaderos
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="field" v-show="seleccionado">
      <div class="control">
        <table class="table is-fullwidth is-bordered is-striped">
          <thead>
            <tr>
              <th>Código</th>
              <th>Acción</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(parqueadero) in parqueaderos" v-bind:key="parqueadero.codigo">
              <td>{{parqueadero.codigo}}</td>
              <td><button type="submit" class="button is-danger" @click="removeParking(parqueadero)">Remover parqueadero</button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "removeParking",
  data() {
    return {
      mssg: "Parqueadero quitado con éxito",
      parqueaderos: [],
      usuarios: [],
      usuarioSeleccionado: [],
      seleccionado: false,
    };
  },
  methods: {
    loadParkings() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/admin/getUserParkings.php";
      this.parqueaderos = [];
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
    loadUsers() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      this.seleccionado = false;
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
    selUser() {
      this.seleccionado = true;
      this.loadParkings();
    },
    removeParking(parqueadero) {
      
      var url = jsonInfo.url_server + jsonInfo.name_app + "/admin/removeParking.php";
      parqueadero.tabla = "parqueadero";
      parqueadero.id_usuario = "";
      parqueadero.esta_libre = 1;
      parqueadero.esta_asignado = 0;
      this.$axios
        .post(url, parqueadero)
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
    this.loadUsers();
  },
};
</script>

<style>
</style>