<template>
  <div class="delcoprop">
    <div class="content-delcoprop">
      <div class="field">
        <div class="control">
          <form @submit.prevent.once="delCoprop" autocomplete="off">
            <div class="field">
              <label class="label">Seleccione la copropiedad a eliminar</label>
              <div class="control">
                <div class="select">
                  <select v-model="copropSeleccionada">
                    <option>{{selectCoprop}}</option>
                    <option
                      v-for="coprop in coprops"
                      :value="coprop"
                      v-bind:key="coprop.id"
                    >{{coprop.nombre}}</option>
                  </select>
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
      this.coprops = [];
      this.$axios
        .get("MainServlet/getCoprops")
        .then((response) => {
          this.coprops = response.data;
          console.log(this.coprops);
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
      this.seleccionado = true;
      console.log(this.copropSeleccionada);
      var requestObject = {
        tabla: "copropiedad",
        id: this.copropSeleccionada.id,
      };
      this.$axios
        .post("MainServlet/delete", requestObject)
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
  created() {
    this.loadCoprops();
    console.log("DelCoprop.vue");
  },
};
</script>

<style>
</style>