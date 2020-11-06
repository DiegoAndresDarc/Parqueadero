<template>
  <div class="parking">
    <div class="content">
      <div class="field" v-if="!disponibilidad">
        <div class="control">
          <h1 class="title">
            No existe más disponibilidad para agregar parqueaderos de acuerdo a
            las configuraciones realizadas.
          </h1>
        </div>
      </div>
      <div class="field" v-else>
        <div class="control">
          <div class="field">
            <div class="control">
              <form @submit.prevent="addParking" autocomplete="off">
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
                        <input
                          type="checkbox"
                          v-model="info.admite_carro"
                          v-if="
                            cantidad.copropiedad[0].n_parqueaderos_carro > 0 ||
                            cantidad.copropiedad[0].n_parqueaderos_carro_vis > 0
                          "
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
                          v-model="info.admite_moto"
                          v-if="
                            cantidad.copropiedad[0].n_parqueaderos_moto > 0 ||
                            cantidad.copropiedad[0].n_parqueaderos_moto_vis > 0
                          "
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
                            v-model="info.admite_bicicleta"
                            v-if="
                              cantidad.copropiedad[0].n_parqueaderos_bicicleta >
                                0 ||
                              cantidad.copropiedad[0]
                                .n_parqueaderos_bicicleta_vis > 0
                            "
                          />
                        </label>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="field is-horizontal">
                  <div class="field-label is-normal">
                    <label class="label">Parqueadero para uso de</label>
                  </div>
                  <div class="field-body">
                    <div class="field is-narrow">
                      <div class="control">
                        <div class="select">
                          <select v-model="info.tipo">
                            <option
                              v-if="
                                cantidad.copropiedad[0].n_parqueaderos_carro >
                                  0 ||
                                cantidad.copropiedad[0].n_parqueaderos_moto >
                                  0 ||
                                cantidad.copropiedad[0]
                                  .n_parqueaderos_bicicleta > 0
                              "
                            >
                              RESIDENTE
                            </option>
                            <option
                              v-if="
                                cantidad.copropiedad[0]
                                  .n_parqueaderos_carro_vis > 0 ||
                                cantidad.copropiedad[0]
                                  .n_parqueaderos_moto_vis > 0 ||
                                cantidad.copropiedad[0]
                                  .n_parqueaderos_bicicleta_vis > 0
                              "
                            >
                              VISITANTE
                            </option>
                          </select>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="field is-horizontal">
                  <div class="field-label is-normal">
                    <label class="label">Código de barras</label>
                  </div>
                  <div class="field-body">
                    <div class="field">
                      <div class="control">
                        <input
                          type="text"
                          class="input"
                          placeholder="Codigo de barras"
                          v-model="info.codigo_barras"
                          min="0"
                          required
                        />
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
          <div class="field">
            <div class="control">
              <table class="table is-fullwidth is-bordered is-striped">
                <thead>
                  <tr>
                    <th>Tipo de parqueadero</th>
                    <th>Cantidad restante</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Carro para residentes</td>
                    <td>
                      {{ cantidad.copropiedad[0].n_parqueaderos_carro }}
                    </td>
                  </tr>
                  <tr>
                    <td>Moto para residentes</td>
                    <td>
                      {{ cantidad.copropiedad[0].n_parqueaderos_moto }}
                    </td>
                  </tr>
                  <tr>
                    <td>Bicicleta para residentes</td>
                    <td>
                      {{ cantidad.copropiedad[0].n_parqueaderos_bicicleta }}
                    </td>
                  </tr>
                  <tr>
                    <td>Carro para visitantes</td>
                    <td>
                      {{ cantidad.copropiedad[0].n_parqueaderos_carro_vis }}
                    </td>
                  </tr>
                  <tr>
                    <td>Moto para visitantes</td>
                    <td>
                      {{ cantidad.copropiedad[0].n_parqueaderos_moto_vis }}
                    </td>
                  </tr>
                  <tr>
                    <td>Bicicleta para visitantes</td>
                    <td>
                      {{ cantidad.copropiedad[0].n_parqueaderos_bicicleta_vis }}
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
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
      info: {},
      cantidad: {},
      disponibilidad: true,
    };
  },
  methods: {
    addParking() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/insert.php";
      this.id_copropiedad = this.$session.get("id_coprop");
      this.info.tabla = "parqueadero";
      if (this.info.admite_carro) {
        if (this.info.tipo === "RESIDENTE") {
          this.cantidad.copropiedad[0].n_parqueaderos_carro--;
        } else {
          this.cantidad.copropiedad[0].n_parqueaderos_carro_vis--;
        }
      }
      this.info.admite_carro = this.info.admite_carro == true ? "1" : "0";
      if (this.info.admite_moto) {
        if (this.info.tipo === "RESIDENTE") {
          this.cantidad.copropiedad[0].n_parqueaderos_moto--;
        } else {
          this.cantidad.copropiedad[0].n_parqueaderos_moto_vis--;
        }
      }
      this.info.admite_moto = this.info.admite_moto == true ? "1" : "0";
      if (this.info.admite_bicicleta) {
        if (this.info.tipo === "RESIDENTE") {
          this.cantidad.copropiedad[0].n_parqueaderos_bicicleta--;
        } else {
          this.cantidad.copropiedad[0].n_parqueaderos_bicicleta_vis--;
        }
      }
      this.info.admite_bicicleta =
        this.info.admite_bicicleta == true ? "1" : "0";
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
      this.checkAmount();
    },
    checkAmount() {
      if (
        this.cantidad.copropiedad[0].n_parqueaderos_carro <= 0 &&
        this.cantidad.copropiedad[0].n_parqueaderos_carro_vis <= 0 &&
        this.cantidad.copropiedad[0].n_parqueaderos_moto <= 0 &&
        this.cantidad.copropiedad[0].n_parqueaderos_moto_vis <= 0 &&
        this.cantidad.copropiedad[0].n_parqueaderos_bicicleta <= 0 &&
        this.cantidad.copropiedad[0].n_parqueaderos_bicicleta_vis <= 0
      ) {
        this.disponibilidad = false;
      }
    },
    loadParkingsAmount() {
      var url =
        jsonInfo.url_server + jsonInfo.name_app + "/admin/parkingsAmount.php";
      var requestObject = {
        id_copropiedad: this.$session.get("id_coprop"),
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          this.cantidad = response.data;
          this.cantidad.copropiedad[0].n_parqueaderos_carro -= this.cantidad.parqueaderos[0].CANTIDAD;
          this.cantidad.copropiedad[0].n_parqueaderos_moto -= this.cantidad.parqueaderos[1].CANTIDAD;
          this.cantidad.copropiedad[0].n_parqueaderos_bicicleta -= this.cantidad.parqueaderos[2].CANTIDAD;
          this.cantidad.copropiedad[0].n_parqueaderos_carro_vis -= this.cantidad.parqueaderos[3].CANTIDAD;
          this.cantidad.copropiedad[0].n_parqueaderos_moto_vis -= this.cantidad.parqueaderos[4].CANTIDAD;
          this.cantidad.copropiedad[0].n_parqueaderos_bicicleta_vis -= this.cantidad.parqueaderos[5].CANTIDAD;
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
    this.loadParkingsAmount();
  },
};
</script>

<style scoped>
.label {
  color: black;
}
</style>