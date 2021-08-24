<template>
  <div class="notifications box clogin" v-if="mostrar">
    <article class="message is-info">
      <div class="message-header">
        <p>{{ titulo }}</p>
        <button class="delete" aria-label="delete" @click="backToHome"></button>
      </div>
      <div class="message-body">
        <ul class="list">
          <li
            v-for="(content, index) in contenido"
            v-bind:key="index"
          >
            <p>
              {{ content }}
            </p>
          </li>
        </ul>
      </div>
    </article>
  </div>
</template>

<script>
import jsonInfo from "../../assets/info.json";
import moment from "moment";
export default {
  name: "notifications",
  data() {
    return {
      titulo: "Notificaciones",
      cerrar: "Cerrar",
      contenido: [],
      mostrar: true,
      dia: "",
    };
  },
  methods: {
    backToHome() {
      this.$router.replace({ name: "Home" });
    },
    verifyDay() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      var day = new Date().getDay();
      switch (day) {
        case 0:
          this.dia = "DOMINGO";
          break;
        case 1:
          this.dia = "LUNES";
          break;
        case 2:
          this.dia = "MARTES";
          break;
        case 3:
          this.dia = "MIERCOLES";
          break;
        case 4:
          this.dia = "JUEVES";
          break;
        case 5:
          this.dia = "VIERNES";
          break;
        case 6:
          this.dia = "SABADO";
          break;
      }
      var requestObject = {
        tabla: "configuraciones",
        id_copropiedad: this.$session.get("id_coprop"),
      };
      console.log(requestObject);
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          var showAlerts = false;
          if (response.data[0].dia_arqueo == this.dia) {
            this.contenido.push("La caja debe ser arqueada el día de hoy.");
            showAlerts = true;
          }
          if (response.data[0].dia_alertas == this.dia) {
            this.loadAlerts();
            showAlerts = true;
          }
          if (!showAlerts) {
            this.backToHome();
          }
        })
        .catch((e) => {
          console.log(e);
        });
    },
    loadAlerts() {
      var url =
        jsonInfo.url_server +
        jsonInfo.name_app +
        "/admin/getVehiclesofCoprop.php";
      var requestObject = {
        id_copropiedad: this.$session.get("id_coprop"),
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          console.log(response);
          var vehicles = response.data,
            toDayMoment = moment();
          vehicles.forEach((vehicle) => {
            var dateMoment = moment(
              vehicle.fecha_vencimiento_soat,
              "YYYY-MM-DD"
            );
            var diff = dateMoment.diff(toDayMoment, "days");
            var txt =
              "El vehiculo con placas " +
              vehicle.placa +
              " del propietario " +
              vehicle.nombres +
              " " +
              vehicle.apellidos;
            if (diff <= 15 && diff > 0) {
              txt += " se le vence el SOAT en " + diff + " días.";
              this.contenido.push(txt);
            }
            if (diff <= 0) {
              txt += " tiene el SOAT vencido.";
              this.contenido.push(txt);
            }
          });
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
    this.verifyDay();
  },
};
</script>

<style scoped>
.list {
  text-align: left;
  list-style: disc;
}
</style>