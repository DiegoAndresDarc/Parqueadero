<template>
  <div class="ticket">
    <p class="centrado">{{ info.encabezado_recibo }}</p>
    <p class="centrado">
      <br /><b class="placa">{{ placa }}</b>
    </p>
    <p class="info">
      <br />Valor por {{ info.tipo_pago_visitante }} para carros: ${{
        info.valor_pago_carro
      }}
    </p>
    <p class="info">
      Valor por {{ info.tipo_pago_visitante }} para motos: ${{
        info.valor_pago_moto
      }}
    </p>
    <p class="info">
      Valor por {{ info.tipo_pago_visitante }} para bicicletas: ${{
        info.valor_pago_bicicleta
      }}
    </p>
    <p class="centrado"><br />{{ info.texto_responsabilidad }}</p>
    <p class="centrado"><br />{{ info.pie_pagina_recibo }}</p>
  </div>
</template>

<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "visitTicket",
  props: {
    placa: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      mssg:
        "Recuerde que debe imprimir el recibo para entregarselo al visitante",
      info: {},
    };
  },
  methods: {
    print() {
      var beforePrint = function () {
      alert(mssg);
      };
      var afterPrint = function () {
        window.close();
      };
      window.onbeforeprint = beforePrint;
      window.onafterprint = afterPrint;
      window.print();
    },
    getData() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      var requestObject = {
        tabla: "configuraciones",
        id_copropiedad: this.$session.get("id_coprop"),
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          this.info = response.data[0];
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
    this.getData();
    console.log(this.placa);
    this.print();
    this.$bus.$on("print", this.print);
  },
};
</script>

<style scoped>
* {
  font-size: 16px;
  font-family: "Arial";
}
.ticket {
  width: 285px;
  max-width: 285px;
  color: black;
}

.centrado {
  text-align: center;
  align-content: center;
}

.info {
  font-size: 12px;
}

.placa {
  font-size: 30px;
}
</style>