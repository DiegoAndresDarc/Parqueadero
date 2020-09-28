<template>
  <div class="addCoprop">
    <div class="content-addCoprop">
      <div class="field">
        <div class="control">
          <form @submit.prevent.once="agregarCoprop" autocomplete="off">
            <div class="field">
              <div class="control">
                <input
                  class="input is-medium"
                  type="text"
                  placeholder="Nombre"
                  id="name"
                  v-model="info.nombre"
                  required
                />
              </div>
            </div>
            <div class="field">
              <div class="control">
                <input
                  class="input is-medium"
                  type="text"
                  placeholder="Dirección"
                  id="address"
                  v-model="info.direccion"
                  required
                />
              </div>
            </div>
            <div class="field">
              <div class="control">
                <button class="button is-link is-fullwidth">
                  Agregar Copropiedad/Conjunto residencial
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
  name: "AddCoprop",
  components: {},
  data() {
    return {
      message: "Copropiedad añadida con exito",
      info: {
        tabla: "",
        nombre: "",
        direccion: "",
        habilitada: "",
      },
    };
  },
  methods: {
    agregarCoprop() {
      const config = {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      };
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/signup.php";
      this.info.tabla = "copropiedad";
      this.info.nombre = this.info.nombre.toUpperCase();
      this.info.direccion = this.info.direccion.toUpperCase();
      this.info.habilitada = "1";
      this.$axios
        .post(url, this.info)
        .then((response) => {
          console.log(response);
          alert(this.message);
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  created() {
    console.log("AddCoprop.vue");
  },
};
</script>
<style>
</style>