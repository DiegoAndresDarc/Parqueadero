<template>
  <div class="ticket">
    <div class="content">
      <p>{{ info.encabezado_recibo }}</p>
      <p>{{ placa }}</p>
      <p>
        VALOR POR {{ info.tipo_pago_visitante }} PARA CARROS: ${{
          info.valor_pago_carro
        }}
      </p>
      <p>
        VALOR POR {{ info.tipo_pago_visitante }} PARA MOTOS: ${{
          info.valor_pago_moto
        }}
      </p>
      <p>
        VALOR POR {{ info.tipo_pago_visitante }} PARA BICICLETAS: ${{
          info.valor_pago_bicicleta
        }}
      </p>
      <p>{{ info.pie_pagina_recibo }}</p>
    </div>
  </div>
</template>

<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "ticket",
  data() {
    return {
      mssg: "",
      info: {},
      placa: "",
    };
  },
  methods: {
    print(info) {
      this.placa = info.placa;
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
    this.$bus.$on("print:info", this.print);
  },
};
</script>

<style scoped>
.ticket {
  width: 155px;
  max-width: 155px;
}
</style>