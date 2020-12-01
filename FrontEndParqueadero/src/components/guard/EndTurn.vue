<template>
  <div class="turn">
    <div class="content">
      <div class="field" v-if="!turno_iniciado">
        <div class="control">
          <h2>Aún no se ha iniciado la jornada laboral</h2>
        </div>
      </div>
      <div class="field" v-else>
        <div class="control">
          <div class="field is-horizontal">
            <div class="field-label">
              <label class="label"
                >El dinero con el que debe finalizar su turno es de:</label
              >
            </div>
            <div class="field-body">
              <h3>${{ dineroVisual }} COP</h3>
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button
                type="submit"
                class="button is-link is-fullwidth"
                @click="endTurn"
              >
                Finalizar turno
              </button>
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
  name: "endTurn",
  data() {
    return {
      mssg: "Jornada laboral finalizada",
      turno_iniciado: false,
      dinero: 0,
      dineroVisual: "0",
    };
  },
  methods: {
    endTurn() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/guard/endTurn.php";
      var info = {
        id_usuario: this.$session.get("id"),
        dinero_final: this.$session.get("dinero"),
      };
      var date = new Date();
      info.fecha_salida =
        date.getFullYear() + "/" + (date.getMonth() + 1) + "/" + date.getDate();
      info.hora_salida =
        date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
      this.$axios
        .post(url, info)
        .then((response) => {
          if (response.data == true) {
            alert(this.mssg);
            this.$session.remove("dinero");
            this.turno_iniciado = false;
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
  created() {
    var dinero = this.$session.get("dinero");
    if (dinero != null) {
      this.turno_iniciado = true;
      this.dinero = dinero;
      this.dineroVisual = Number(this.dinero).toLocaleString();
    }
  },
};
</script>

<style>
</style>