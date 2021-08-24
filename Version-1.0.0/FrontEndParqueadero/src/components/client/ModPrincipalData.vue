<template>
  <div class="modData">
    <div class="content">
      <form @submit.prevent="modData" autocomplete="off">
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Nombres Completos</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  type="text"
                  class="input"
                  placeholder="Nombres"
                  v-model="info.nombres"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Apellidos Completos</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  type="text"
                  class="input"
                  placeholder="Apellidos"
                  v-model="info.apellidos"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Tipo de identificación</label>
          </div>
          <div class="field-body">
            <div class="field is-narrow">
              <div class="control">
                <div class="select">
                  <select v-model="info.tipo_identificacion">
                    <option>CC</option>
                    <option>CE</option>
                    <option>NIT</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Número de identificación</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  type="number"
                  class="input"
                  placeholder="Número de identificacion"
                  v-model="info.identificacion"
                  min="0"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Número de teléfono fijo</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="tel"
                  pattern="[0-9]{7}"
                  title="Un número de telefono fijo tiene una longitud de 7 digitos con números entre 0 y 9"
                  placeholder="telefono fijo"
                  v-model="info.telefono"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Número de teléfono celular</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="tel"
                  pattern="[3]{1}[0-9]{9}"
                  title="Un número de celular en Colombia inicia con el número 3 y tiene una longitud de 10 digitos con números entre 0 y 9"
                  placeholder="celular"
                  v-model="info.celular"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Email</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                  type="email"
                  class="input"
                  placeholder="Dirección de correo electrónico"
                  v-model="info.email"
                  required
                />
              </div>
            </div>
          </div>
        </div>
        <div class="field">
          <div class="control">
            <button class="button is-link is-fullwidth">Modificar</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "modPrincipalData",
  data() {
    return {
      mssg: "Datos modificados con éxito",
      info: {},
    };
  },
  methods: {
    loadData() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      this.id_copropiedad = this.$session.get("id_coprop");
      this.info = {};
      var requestObject = {
        tabla: "usuario",
        id_copropiedad: this.id_copropiedad,
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
    modData() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/update.php";
      this.info.tabla = "usuario";
      this.info.nombres = this.info.nombres.toUpperCase();
      this.info.apellidos = this.info.apellidos.toUpperCase();
      this.info.email = this.info.email.toUpperCase();
      this.$axios
        .post(url, this.info)
        .then((response) => {
          console.log(response);
          if (response.data == true) alert(this.mssg);
          this.loadData();
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
    this.loadData();
  },
};
</script>

<style scope>
.label {
  color: black;
}
</style>