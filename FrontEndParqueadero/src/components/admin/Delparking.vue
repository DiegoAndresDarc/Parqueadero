<template>
  <div class="parking">
    <div class="content">
      <form @submit.prevent.once="delParking" autocomplete="off">
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label is-expanded"
              >Seleccione el parqueadero a eliminar</label
            >
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control is-expanded">
                <div class="select is-fullwidth">
                  <select v-model="parqueaderoSeleccionado">
                    <option>{{ selprk }}</option>
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
  name: "delParking",
  data() {
    return {
      mssg: "Parqueadero eliminado con éxito",
      selprk: "Seleccione un parqueadero...",
      parqueaderos: [],
      parqueaderoSeleccionado: {},
      idCopropiedad: "",
    };
  },
  methods: {
    loadParkings() {
      this.idCopropiedad = this.$session.get("id_coprop");
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      this.parqueaderos = [];
      this.parqueaderoSeleccionado = {};
      var requestObject = {
        tabla: "parqueadero",
        id_copropiedad: this.idCopropiedad,
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
    delParking() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/delete.php";
      var requestObject = {
        tabla: "parqueadero",
        id: this.parqueaderoSeleccionado.id,
      };
      this.$axios
        .post(url, requestObject)
        .then((response) => {
          if (response.data == true) alert(this.mssg);
          this.loadParkings();
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