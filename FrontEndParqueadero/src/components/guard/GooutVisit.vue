<template>
  <div class="visit">
    <div class="content">
      <div class="field" v-if="!turno_iniciado">
        <div class="control">
          <h2>
            Para realizar esta función se debe haber iniciado la jornada laboral
          </h2>
        </div>
      </div>
      <div class="field" v-else>
        <div class="control">
          <form @submit.prevent="searchVisit" autocomplete="off">
            <div class="field is-horizontal">
              <div class="field-label">
                <label class="label"
                  >Placa del vehículo, impresa en el recibo</label
                >
              </div>
              <div class="field-body">
                <input class="input" type="text" id="placa" v-model="placa" />
              </div>
            </div>
            <div class="field">
              <div class="control">
                <button class="button is-link is-fullwidth">Buscar</button>
              </div>
            </div>
          </form>
        </div>
      </div>
      <div class="field" v-show="encontrado">
        <div class="field">
          <label class="label">Imagen del vehiculo</label>
          <div class="control">
            <img :src="registro.foto" height="250px" width="250px" />
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Total a pagar</label>
          </div>
          <div class="field-body">
            <h3>${{ total }} COP</h3>
          </div>
        </div>
        <div class="field">
          <div class="control">
            <button
              type="submit"
              class="button is-link is-fullwidth"
              @click="goOutVisit"
            >
              Dar salida
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import jsonInfo from "../../assets/info.json";
import moment from "moment";
export default {
  name: "goOutVisit",
  data() {
    return {
      mssg: "Salida de visitante exitosa",
      registro: {},
      placa: "",
      encontrado: false,
      total: "",
      info: {},
      turno_iniciado: false,
    };
  },
  methods: {
    loadConfs() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      var requestObject = {
        tabla: "configuraciones",
        id_copropiedad: this.$session.get("id_coprop"),
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          if (response.data.length) {
            this.info = response.data[0];
          }
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
    },
    searchVisit() {
      var url =
        jsonInfo.url_server + jsonInfo.name_app + "/guard/findLastVisit.php";
      var requestObject = {
        placa: this.placa,
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          if (response.data.length) {
            this.registro = response.data[0];
            this.calculateTotal();
            var url = jsonInfo.url_server + jsonInfo.name_app;
            this.registro.foto = this.registro.foto.replace("..", url);
            this.encontrado = true;
          } else {
            this.encontrado = false;
            alert("El vehiculo no registró su entrada al parqueadero");
          }
        })
        .catch((e) => {
          console.log(e);
        });
    },
    calculateTotal() {
      var dateMoment = moment(
          this.registro.fecha_entrada + " " + this.registro.hora_entrada,
          "YYYY-MM-DD HH:mm:ss"
        ),
        toDayMoment = moment(),
        diff,
        value;
      switch (this.info.tipo_pago_visitante) {
        case "DIA":
          diff = toDayMoment.diff(dateMoment, "days");
          break;
        case "HORA":
          diff = toDayMoment.diff(dateMoment, "hours");
          break;
        case "MINUTO":
          diff = toDayMoment.diff(dateMoment, "minutes");
          break;
      }
      switch (this.registro.tipo_vehiculo) {
        case "CARRO":
          value = this.info.valor_pago_carro;
          break;
        case "MOTO":
          value = this.info.valor_pago_moto;
          break;
        case "BICICLETA":
          value = this.info.valor_pago_bicicleta;
          break;
      }
      value =
        diff > this.info.tiempo_gracia
          ? value * Math.abs(diff - this.info.tiempo_gracia)
          : 0;
      this.total = Number(value).toLocaleString();
    },
    goOutVisit() {
      var url =
        jsonInfo.url_server + jsonInfo.name_app + "/guard/goOutVisit.php";
      var date = new Date();
      this.registro.fecha_salida =
        date.getFullYear() + "/" + (date.getMonth() + 1) + "/" + date.getDate();
      this.registro.hora_salida =
        date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
      this.$axios
        .post(url, this.registro)
        .then((response) => {
          console.log(response.data);
          if (response.data == true) alert(this.mssg);
          var dinero = this.$session.get("dinero");
          var pago = parseFloat(this.total.replaceAll(".", ""));
          dinero += pago;
          this.$session.set("dinero", dinero);
          this.encontrado = false;
          this.registro = {};
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
    if (this.$session.get("dinero") != null) {
      this.turno_iniciado = true;
      this.loadConfs();
    }
  },
};
</script>

<style>
</style>