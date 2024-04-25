<template>
  <div class="archBox">
    <div class="content">
      <div class="field">
        <div class="control">
          <form @submit.prevent.once="verifyPassword" autocomplete="off">
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label">Digite el usuario administrador</label>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <input
                      type="password"
                      class="input"
                      v-model="adminInfo.usuario"
                      placeholder="usuario del administrador"
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label"
                  >Digite la contraseña del usuario administrador</label
                >
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <input
                      type="password"
                      class="input"
                      v-model="adminInfo.password"
                      placeholder="contraseña del administrador"
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <button type="submit" class="button is-fullwidth is-link">
                  Aceptar
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
      <div class="field" v-if="datosCorrectos">
        <div class="control">
          <h2>Arqueo de caja</h2>
          <div class="field is-horizontal">
            <div class="field-label">
              <label class="label">El dinero que debe ser entregado es:</label>
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
import * as crypto from "crypto-js";
import jsonInfo from "../../assets/info.json";
export default {
  name: "archBox",
  data() {
    return {
      mssg:
        "El arqueo de caja se hizo correctamente.\n El guardia debe iniciar su turno nuevamente",
      adminInfo: {},
      dineroVisual: "0",
      datosCorrectos: false,
    };
  },
  methods: {
    verifyPassword() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/login.php";
      this.adminInfo.password = crypto
        .SHA512(this.adminInfo.password)
        .toString();
      this.$axios
        .get(url, {
          params: this.adminInfo,
        })
        .then((response) => {
          if (response.status === 200 && response.data.length) {
            this.datosCorrectos = true;
          } else {
            alert("Usuario o contraseña incorrectos");
            this.adminInfo = {};
          }
        })
        .catch((e) => {
          console.log(e);
          this.adminInfo = {};
        });
    },
    endTurn() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/guard/endTurn.php";
      var info = {
        id_usuario: this.$session.get("id"),
        dinero_final: "0",
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
            this.datosCorrectos = false;
            this.adminInfo = {};
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