<template>
  <div class="conf-params">
    <div class="content-conf-params">
      <form @submit.prevent.once="confParams" autocomplete="off">
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Peso máximo para vehículos</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="number"
                  placeholder="Peso máximo permitido"
                  id="peso_maximo"
                  v-model="info.peso_maximo"
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
            <label class="label">Ejes máximos para vehículos</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="number"
                  placeholder="Ejes máximos permitidos"
                  id="ejes_maximos"
                  v-model="info.ejes_maximos"
                  min="0"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Día de la semana para arqueo de la caja</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input is-medium"
                  type="number"
                  placeholder="Día de arqueo de la caja"
                  id="dia_arqueo"
                  v-model="info.dia_arqueo"
                  min="1"
                  max="7"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label"
              >Día de la semana para envíar alertas (Notificaciones)</label
            >
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input is-medium"
                  type="number"
                  placeholder="Día de alertas"
                  id="dia_alertas"
                  v-model="info.dia_alertas"
                  min="1"
                  max="7"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label"
              >Cantidad de parqueaderos de carros para residentes</label
            >
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input is-medium"
                  type="number"
                  placeholder="Cantidad de parqueaderos de carros para residentes"
                  id="n_parqueaderos_carro"
                  v-model="info.n_parqueaderos_carro"
                  min="0"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label"
              >Cantidad de parqueaderos de motos para residentes</label
            >
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input is-medium"
                  type="number"
                  placeholder="Cantidad de parqueaderos de motos para residentes"
                  id="n_parqueaderos_moto"
                  v-model="info.n_parqueaderos_moto"
                  min="0"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label"
              >Cantidad de parqueaderos de bicicletas para residentes</label
            >
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input is-medium"
                  type="number"
                  placeholder="Cantidad de parqueaderos de bicicletas para residentes"
                  id="n_parqueaderos_bicicleta"
                  v-model="info.n_parqueaderos_bicicleta"
                  min="0"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label"
              >Cantidad de parqueaderos de carros para visitantes</label
            >
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input is-medium"
                  type="number"
                  placeholder="Cantidad de parqueaderos de carros para visitantes"
                  id="n_parqueaderos_carro_vis"
                  v-model="info.n_parqueaderos_carro_vis"
                  min="0"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label"
              >Cantidad de parqueaderos de motos para visitantes</label
            >
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input is-medium"
                  type="number"
                  placeholder="Cantidad de parqueaderos de motos para visitantes"
                  id="n_parqueaderos_motos_vis"
                  v-model="info.n_parqueaderos_moto_vis"
                  min="0"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label"
              >Cantidad de parqueaderos de bicicletas para visitantes</label
            >
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input is-medium"
                  type="number"
                  placeholder="Cantidad de parqueaderos de bicicletas para visitantes"
                  id="n_parqueaderos_bicicleta"
                  v-model="info.n_parqueaderos_bicicleta_vis"
                  min="0"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Tipo de periodo pago para visitantes</label>
          </div>
          <div class="field-body">
            <div class="field is-narrow">
              <div class="control">
                <div class="select">
                  <select v-model="info.tipo_pago_visitante">
                    <option>SEGUNDO</option>
                    <option>MINUTO</option>
                    <option>HORA</option>
                    <option>DIA</option>
                    <option>SEMANA</option>
                    <option>MES</option>
                    <option>AÑO</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label"
              >Valor del pago para el periodo seleccionado</label
            >
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input is-medium"
                  type="number"
                  placeholder="Valor del pago para el periodo seleccionado"
                  id="valor_pago_visitante"
                  v-model="info.valor_pago_visitante"
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
            <label class="label"
              >Tiempo de gracia antes de iniciar a cobrar a los
              visitantes</label
            >
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input is-medium"
                  type="number"
                  placeholder="Tiempo de gracia antes de iniciar a cobrar a los visitantes"
                  id="tiempo_gracia"
                  v-model="info.tiempo_gracia"
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
            <label class="label">Encabezado para los recibos de pago</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <textarea
                  class="textarea"
                  placeholder="Encabezado para los recibos generados"
                  id="encabezado_recibo"
                  v-model="info.encabezado_recibo"
                  maxlength="512"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label"
              >Texto de responsabilidad por parte de la Copropiedad</label
            >
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <textarea
                  class="textarea"
                  placeholder="Texto de responsabilidad por parte de la Copropiedad"
                  id="texto_responsabilidad"
                  v-model="info.texto_responsabilidad"
                  maxlength="512"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Pie de página de los recibos de pago</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <textarea
                  class="textarea"
                  placeholder="Pie de página de los recibos de pago"
                  id="pie_pagina_recibo"
                  v-model="info.pie_pagina_recibo"
                  maxlength="512"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field">
          <div class="control">
            <button class="button is-link is-fullwidth">Configurar</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "ConfParams",
  data() {
    return {
      mssg: "Copropiedad/Conjunto residencial configurado con éxito",
      info: {
        id_copropiedad: "",
        peso_maximo: "",
        ejes_maximos: "",
        dia_arqueo: "",
        dia_alertas: "",
        n_parqueaderos_carro: "",
        n_parqueaderos_moto: "",
        n_parqueaderos_bicicleta: "",
        n_parqueaderos_carro_vis: "",
        n_parqueaderos_moto_vis: "",
        n_parqueaderos_bicicleta_vis: "",
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
    confParams() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/insert.php";
      this.info.id_copropiedad = this.$session.get("id_coprop");
      this.info.tabla = "configuraciones";
      this.info.encabezado_recibo = this.info.encabezado_recibo.toUpperCase();
      this.info.texto_responsabilidad = this.info.texto_responsabilidad.toUpperCase();
      this.info.pie_pagina_recibo = this.info.pie_pagina_recibo.toUpperCase();
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
  created() {
    console.log("ConfParams.vue");
  },
};
</script>

<style>
.label {
  color: black;
}
</style>