<template>
  <div class="parking">
    <div class="content">
      <form @submit.prevent.once="addParking" autocomplete="off">
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Código único de identificación</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  type="text"
                  class="input"
                  placeholder="Código único de identificación"
                  v-model="info.codigo"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Área en metros cuadrados</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  type="number"
                  class="input"
                  placeholder="Área"
                  v-model="info.area"
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
            <label class="label">Peso admitido</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  type="number"
                  class="input"
                  placeholder="Peso admitido"
                  v-model="info.peso_admitido"
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
            <label class="label">Ejes admitidos</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  type="number"
                  class="input"
                  placeholder="Ejes admitidos"
                  v-model="info.ejes_admitidos"
                  min="0"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Admite carros</label>
          </div>
          <div class="field-body">
            <div class="field is-narrow">
              <div class="control">
                <input type="checkbox" v-model="info.admite_carro" />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label"> Admite motos</label>
          </div>
          <div class="field-body">
            <div class="field is-narrow">
              <div class="control">
                <input type="checkbox" v-model="info.admite_moto" />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label"> Admite bicicletas</label>
          </div>
          <div class="field-body">
            <div class="field is-narrow">
              <div class="control">
                <label class="label">
                  <input type="checkbox" v-model="info.admite_bicicleta" />
                </label>
              </div>
            </div>
          </div>
        </div>
        <div class="field">
          <div class="control">
            <button class="button is-link is-fullwidth">
              Añadir Parqueadero
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "addParking",
  data() {
    return {
      mssg: "Parqueadero añadido con éxito",
      info: {
        id_copropiedad: "",
        codigo: "",
        area: "",
        peso_admitido: "",
        ejes_admitidos: "",
        admite_carro: "",
        admite_moto: "",
        admite_bicicleta: "",
      },
    };
  },
  methods: {
    addParking() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/insert.php";
      this.id_copropiedad = this.$session.get("id_coprop");
      this.info.tabla = "parqueadero";
      this.info.admite_carro = this.info.admite_carro == true ? "1" : "0";
      this.info.admite_moto = this.info.admite_moto == true ? "1" : "0";
      this.info.admite_bicicleta =
        this.info.admite_bicicleta == true ? "1" : "0";
      this.info.id_copropiedad = this.id_copropiedad;
      console.log(this.info);
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

<style scoped>
.label {
  color: black;
}
</style>