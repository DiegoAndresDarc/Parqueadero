<template>
  <div class="payment">
    <div class="content">
      <div class="field">
        <div class="control">
          <form @submit.prevent="makePayments" autocomplete="off">
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label"
                  >Archivo csv con la información de los pagos</label
                >
              </div>
              <div class="field-body">
                <div class="file has-name">
                  <label class="file-label">
                    <input
                      class="file-input"
                      type="file"
                      accept=".csv"
                      @change="getFile"
                      required
                    />
                    <span class="file-cta">
                      <span class="file-icon">
                        <i class="mdi mdi-upload"></i>
                      </span>
                      <span class="file-label">Escoge un archivo</span>
                    </span>
                    <span class="file-name">
                      {{ nombreArchivoPagos }}
                    </span>
                  </label>
                </div>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <button class="button is-fullwidth is-link">
                  Subir archivo de pagos
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
      <div class="field">
        <div class="control">
          <p>
            Recuerde que el archivo <b>.csv</b> debe tener los siguientes campos
            separados por punto y coma:<br />
            <b
              ><i
                >Número de identificación del propietario del parqueadero;Código
                de identificación del parquedero;Fecha de pago(YYYY-MM-DD);Hora
                de pago(HH:MM:ss) Formato 24 Horas</i
              ></b
            >
          </p>
        </div>
      </div>
      <div class="field" v-if="error">
        <div class="control">
          <h3>Los siguientes registros tuvieron error al procesarse:</h3>
          <p v-for="(registro, index) in registrosErrorneos" v-bind:key="index">
            Usuario:{{ registro.usuario }} --- Parqueadero:{{
              registro.parqueadero
            }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "multiplePayment",
  data() {
    return {
      mssg: "Los pagos se han realizado con éxito",
      nombreArchivoPagos: "",
      archivo: "",
      error: false,
      registrosErrorneos: [],
    };
  },
  methods: {
    getFile(event) {
      this.archivo = event.target.files[0];
      this.nombreArchivoPagos = this.archivo.name;
    },
    makePayments() {
      if (!this.nombreArchivoPagos.length) {
        alert("Debe escoger un archivo");
        return;
      }
      var url =
        jsonInfo.url_server + jsonInfo.name_app + "/admin/uploadFile.php";
      const formData = new FormData();
      formData.append(this.nombreArchivoPagos, this.archivo);
      this.$axios
        .post(url, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          if (response.data == true) {
            alert(this.mssg);
            this.archivo = "";
            this.nombreArchivoPagos = "";
          } else {
            this.error = true;
            this.registrosErrorneos = response.data;
          }
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