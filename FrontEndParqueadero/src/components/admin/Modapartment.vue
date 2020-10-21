<template>
  <div class="mod-apartment">
    <div class="content">
      <div class="field">
        <div class="control">
          <form @submit.prevent="selApartment" autocomplete="off">
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label"
                  >Seleccione el apartamento a modificar</label
                >
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
                <button class="button is-link is-fullwidth">Modificar</button>
              </div>
            </div>
          </form>
        </div>
      </div>
      <div class="field" v-show="seleccionado">
        <div class="control">
          <form
            @submit.prevent.once="modApartment"
            autocomplete="off"
            name="form"
          >
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label">Bloque/Interior al cual pertenece</label>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <input
                      class="input"
                      type="text"
                      placeholder="Bloque/Interior al cual pertenece"
                      v-model="apartamentoSeleccionado.bloque"
                      required
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label">Número/nombre del apartamento</label>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <input
                      class="input is-medium"
                      type="text"
                      placeholder="Número/nombre del apartamento"
                      v-model="apartamentoSeleccionado.apartamento"
                      required
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <button class="button is-fullwidth is-link">Aceptar</button>
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
  name: "modApartment",
  data() {
    return {
      mssg: "Apartamento modificado con éxito",
      selapto: "Seleccione un apartamento",
      apartamentos: [],
      apartamentoSeleccionado: {},
      seleccionado: false,
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
    selApartment() {
      this.seleccionado = true;
    },
    modApartment() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/update.php";
      this.apartamentoSeleccionado.tabla = "apartamento";
      this.apartamentoSeleccionado.bloque = this.apartamentoSeleccionado.bloque.toUpperCase();
      this.apartamentoSeleccionado.apartamento = this.apartamentoSeleccionado.apartamento.toUpperCase();
      this.$axios
        .post(url, this.apartamentoSeleccionado)
        .then((response) => {
          if (response.data == true) alert(this.mssg);
          this.seleccionado = false;
          this.apartamentoSeleccionado = {};
          this.loadApartments();
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
    this.loadApartments();
  },
};
</script>

<style>
</style>