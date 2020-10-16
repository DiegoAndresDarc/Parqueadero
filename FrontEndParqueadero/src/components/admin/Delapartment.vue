<template>
  <div class="del-apto">
    <div class="content">
      <form @submit.prevent.once="delApartment" autocomplete="off">
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Seleccione el apartamento a eliminar</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <div class="select is-fullwidth">
                  <select v-model="apartamentoSeleccionado">
                    <option>{{ selapto }}</option>
                    <option
                      v-for="apto in apartamentos"
                      :value="apto"
                      v-bind:key="apto.id"
                    >
                      {{ apto.bloque }} | {{ apto.apartamento }}
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
  name: "delApartment",
  data() {
    return {
      mssg: "Apartamento eliminado con éxito",
      selapto: "Seleccione un apartamento...",
      apartamentos: [],
      apartamentoSeleccionado: {},
      id_copropiedad: "",
    };
  },
  methods: {
    loadApartments() {
      this.id_copropiedad = this.$session.get("id_coprop");
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      this.apartamentos = [];
      this.apartSeleccionado = {};
      var requestObject = {
        tabla: "apartamento",
        id_copropiedad: this.id_copropiedad,
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          this.apartamentos = response.data;
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
    },
    delApartment() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/delete.php";
      var requestObject = {
        tabla: "apartamento",
        id: this.apartamentoSeleccionado.id,
      };
      this.$axios
        .post(url, requestObject)
        .then((response) => {
          if (response.data == true) alert(this.mssg);
          this.loadApartments();
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
    this.loadApartments();
    console.log("ModApartment.vue");
  },
};
</script>

<style>
</style>