<template>
  <div class="addaptm">
    <div class="content-aptm">
      <form @submit.prevent.once="addApartm" autocomplete="off" name="form">
        <div class="field">
          <label class="label">Bloque/Interior al cual pertenece</label>
          <div class="control">
            <input
              class="input is-medium"
              type="text"
              placeholder="Bloque/Interior al cual pertenece"
              v-model="info.bloque"
              required
            />
          </div>
        </div>
        <div class="field">
          <label class="label">Número/nombre del apartamento</label>
          <div class="control">
            <input
              class="input is-medium"
              type="text"
              placeholder="Número/nombre del apartamento"
              v-model="info.apartamento"
              required
            />
          </div>
        </div>
        <div class="field">
          <div class="control">
            <button class="button is-colorcustom">Añadir Apartamento</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "addApartment",
  data() {
    return {
      mssg: "Apartamento añadido con éxito",
      info: {
        tabla: "",
        bloque: "",
        apartamento: "",
        id_copropiedad: "",
      },
      id_copropiedad: "",
    };
  },
  methods: {
    addApartm() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/insert.php";
      this.id_copropiedad = this.$session.get("id_coprop");
      this.info.tabla = "apartamento";
      this.info.bloque = this.info.bloque.toUpperCase();
      this.info.apartamento = this.info.apartamento.toUpperCase();
      this.info.id_copropiedad = this.id_copropiedad;
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
  },
  beforeCreate() {
    this.$bus.$emit("checkSession", "");
  },
  created() {},
};
</script>

<style>
</style>