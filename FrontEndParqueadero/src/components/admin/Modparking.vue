<template>
  <div class="parking">
    <div class="content">
      <div class="field">
        <form @submit.prevent.once="selParking" autocomplete="off">
          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label is-expanded"
                >Seleccione el parqueadero a modificar</label
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
              <button class="button is-link is-fullwidth">Modificar</button>
            </div>
          </div>
        </form>
      </div>
      <div class="field" v-show="seleccionado">
        <form @submit.prevent.once="modParking" autocomplete="off">
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
                    v-model="parqueaderoSeleccionado.codigo"
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
                    v-model="parqueaderoSeleccionado.area"
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
                    v-model="parqueaderoSeleccionado.peso_admitido"
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
                    v-model="parqueaderoSeleccionado.ejes_admitidos"
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
                  <input
                    type="checkbox"
                    v-model="parqueaderoSeleccionado.admite_carro"
                  />
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
                  <input
                    type="checkbox"
                    v-model="parqueaderoSeleccionado.admite_moto"
                  />
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
                    <input
                      type="checkbox"
                      v-model="parqueaderoSeleccionado.admite_bicicleta"
                    />
                  </label>
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
  </div>
</template>

<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "modParking",
  data() {
    return {
      mssg: "Parqueadero añadido con éxito",
      selprk: "Seleccione un parqueadero...",
      parqueaderos: [],
      parqueaderoSeleccionado: {},
      idCopropiedad: "",
      seleccionado: false,
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
    selParking() {
      this.seleccionado = true;
    },
    modParking() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/update.php";
      console.log(this.parqueaderoSeleccionado);
      this.parqueaderoSeleccionado.tabla = "parqueadero";
      this.parqueaderoSeleccionado.codigo = this.parqueaderoSeleccionado.codigo.toUpperCase();
      this.parqueaderoSeleccionado.admite_carro =
        this.parqueaderoSeleccionado.admite_carro == true ? "1" : "0";
      this.parqueaderoSeleccionado.admite_moto =
        this.parqueaderoSeleccionado.admite_moto == true ? "1" : "0";
      this.parqueaderoSeleccionado.admite_bicicleta =
        this.parqueaderoSeleccionado.admite_bicicleta == true ? "1" : "0";
      this.$axios
        .post(url, this.parqueaderoSeleccionado)
        .then((response) => {
          if (response.data == true) alert(this.mssg);
          this.loadParkings();
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
      this.seleccionado = false;
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