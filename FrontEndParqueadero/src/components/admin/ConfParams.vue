<template>
  <div class="conf-params">
    <div class="content-conf-params">
      <form @submit.prevent.once="confParams" autocomplete="off"></form>
    </div>
  </div>
</template>

<script>
export default {
  name: "ConfParams",
  data() {
    return {
      mssg: "Copropiedad/Conjunto residencial configurado con éxito",
      info: {
        peso_maximo: "",
        ejes_maximos: "",
        dia_arqueo: "",
        dia_alertas: "",
        n_parqueaderos_carro: "",
        n_parqueaderos_moto: "",
        n_parqueaderos_carro_vis: "",
        n_parqueaderos_moto_vis: "",
        tipo_pago_visitante: "MINUTO",
        valor_pago_visitante: "",
        tiempo_gracia: "",
        encabezado_recibo: "",
        texto_responsabilidad: "",
        pie_pagina_recibo: "",
      },
    };
  },
  methods: {
    confParams() {},
  },
  beforeCreate(){
      this.$bus.$emit("checkSession", "");
  },
  created() {
    console.log("ConfParams.vue");
  },
};
</script>

<style>
</style>