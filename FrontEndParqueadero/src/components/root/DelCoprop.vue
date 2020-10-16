<template>
  <div class="delcoprop">
    <div class="content-delcoprop">
      <div class="field">
        <div class="control">
          <form @submit.prevent.once="delCoprop" autocomplete="off">
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label"
                  >Seleccione la copropiedad a eliminar</label
                >
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <div class="select is-fullwidth">
                      <select v-model="copropSeleccionada">
                        <option>{{ selectCoprop }}</option>
                        <option
                          v-for="coprop in coprops"
                          :value="coprop"
                          v-bind:key="coprop.id"
                        >
                          {{ coprop.nombre }}
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
    </div>
  </div>
</template>
<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "DelCoprop",
  data() {
    return {
      mssg: "Copropiedad eliminada con exito",
      coprops: [],
      copropSeleccionada: {},
      selectCoprop: "Seleccione una copropiedad...",
    };
  },
  methods: {
    loadCoprops() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      this.coprops = [];
      var requestObject = {
        tabla: "copropiedad",
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          this.coprops = response.data;
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
    },
    selCoprop() {
      this.seleccionado = true;
      console.log(this.copropSeleccionada);
    },
    delCoprop() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/delete.php";
      this.seleccionado = true;
      console.log(this.copropSeleccionada);
      var requestObject = {
        tabla: "copropiedad",
        id: this.copropSeleccionada.id,
      };
      this.$axios
        .post(url, requestObject)
        .then((response) => {
          alert(this.mssg);
          this.loadCoprops();
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
    this.loadCoprops();
    console.log("DelCoprop.vue");
  },
};
</script>

<style>
</style>