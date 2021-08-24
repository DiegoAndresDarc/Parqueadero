<template>
  <div class="turn">
    <div class="content">
      <div class="field" v-if="turno_iniciado">
        <div class="control">
          <h2>Ya se ha iniciado la jornada laboral</h2>
        </div>
      </div>
      <div class="field" v-else>
        <div class="control">
          <div class="field is-horizontal">
            <div class="field-label">
              <label class="label"
                >El dinero con el que debe iniciar su turno es de:</label
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
                @click="startTurn"
              >
                Iniciar turno
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
  name: "startTurn",
  data() {
    return {
      mssg: "Jornada laboral iniciada",
      dinero: 0,
      dineroVisual: "0",
      turno_iniciado: false,
    };
  },
  methods: {
    getCash() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/guard/getCash.php";
      this.$axios
        .get(url)
        .then((response) => {
          if (response.data.length) {
            this.dinero = parseFloat(response.data[0].dinero_final);
            this.dineroVisual = Number(this.dinero).toLocaleString();
          }
        })
        .catch((e) => {
          console.log(e);
        });
    },
    startTurn() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/insert.php";
      var info = {
        tabla: "turno",
        id_usuario: this.$session.get("id"),
        dinero_inicial: this.dinero,
      };
      var date = new Date();
      info.fecha_entrada =
        date.getFullYear() + "/" + (date.getMonth() + 1) + "/" + date.getDate();
      info.hora_entrada =
        date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
      this.$axios
        .post(url, info)
        .then((response) => {
          if (response.data == true) {
            alert(this.mssg);
            this.$session.set("dinero", this.dinero);
            this.turno_iniciado = true;
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
    } else this.getCash();
  },
};
</script>

<style>
</style>