<template>
  <div class="mod-password">
    <div class="content">
      <form @submit.prevent="modPassword" autocomplete="off">
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Contraseña actual</label>
          </div>
          <div class="field-body">
            <input
              type="password"
              class="input"
              v-model="info.currentPassword"
              required
            />
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Nueva contraseña</label>
          </div>
          <div class="field-body">
            <input
              type="password"
              class="input"
              v-model="info.newPassword"
              required
            />
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Confirmar nueva contraseña</label>
          </div>
          <div class="field-body">
            <input
              type="password"
              :class="
                equalsPassword && confPassword.length
                  ? 'input is-success'
                  : 'input is-danger'
              "
              v-model="confPassword"
              required
            />
          </div>
        </div>
        <div class="field">
          <div class="control">
            <p
              v-if="!equalsPassword && confPassword.length"
              class="help is-danger"
            >
              Las contraseñas no coinciden
            </p>
          </div>
        </div>
        <div class="field">
          <div class="control">
            <button class="button is-link is-fullwidth">
              Modificar contraseña
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import jsonInfo from "../../assets/info.json";
import * as crypto from "crypto-js";
export default {
  name: "modPassword",
  data() {
    return {
      mssg: "Contraseña modificada con éxito",
      mssgDifPassword:
        "La contraseña actual que ingreso es diferente a la ya establecida",
      mssgEqlPassword: "La nueva contraseña es igual a la actual",
      confPassword: "",
      currentPassword: "",
      equalsPassword: false,
      info: {},
      id: "",
    };
  },
  methods: {
    loadCurrentPassword() {
      this.info = {};
      var url =
        jsonInfo.url_server + jsonInfo.name_app + "/client/getPassword.php";
      this.id = this.$session.get("id");
      var requestObject = {
        tabla: "usuario",
        id: this.id,
      };
      console.log(requestObject);
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          this.currentPassword = response.data[0].password;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    modPassword() {
      this.info.currentPassword = crypto
        .SHA512(this.info.currentPassword)
        .toString();
      this.info.newPassword = crypto.SHA512(this.info.newPassword).toString();
      if (this.info.currentPassword !== this.currentPassword) {
        alert(this.mssgDifPassword);
      } else if (this.info.newPassword === this.currentPassword) {
        alert(this.mssgEqlPassword);
      } else {
        var url =
          jsonInfo.url_server + jsonInfo.name_app + "/globals/update.php";
        var data = {};
        data.tabla = "usuario";
        data.password = this.info.newPassword;
        data.id = this.id;
        this.$axios
          .post(url, data)
          .then((response) => {
            if (response.data == true) alert(this.mssg);
          })
          .catch((e) => {
            console.log(e);
          });
      }
      this.info = {};
      this.currentPassword = "";
      this.confPassword = "";
      this.loadCurrentPassword();
    },
  },
  watch: {
    confPassword(newvalue) {
      if (newvalue !== this.info.newPassword) {
        this.equalsPassword = false;
      } else {
        this.equalsPassword = true;
      }
    },
  },
  beforeCreate() {
    this.$bus.$emit("checkSession", "");
  },
  created() {
    this.loadCurrentPassword();
  },
};
</script>

<style scope>
.label {
  color: black;
}
</style>