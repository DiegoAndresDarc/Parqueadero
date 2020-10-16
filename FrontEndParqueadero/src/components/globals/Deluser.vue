<template>
  <div class="deluser">
    <div class="content-deluser">
      <div class="field">
        <div class="control">
          <form @submit.prevent.once="delUser" autocomplete="off">
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <label class="label">Seleccione el usuario a eliminar</label>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <div class="select is-fullwidth">
                      <select v-model="usuarioSeleccionado">
                        <option>{{ selusuario }}</option>
                        <option
                          v-for="usuario in usuarios"
                          :value="usuario"
                          v-bind:key="usuario.identificacion"
                        >
                          {{ usuario.nombres }} {{ usuario.apellidos }}
                        </option>
                      </select>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <button class="button is-link is-fullwidth">Eliminar</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import jsonInfo from "../../assets/info.json";
export default {
  name: "Deluser",
  data() {
    return {
      mssg: "Usuario eliminado con éxito",
      selusuario: "Seleccione un usuario...",
      usuarios: [],
      usuarioSeleccionado: {},
      error: false,
    };
  },
  methods: {
    loadUsers() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/select.php";
      this.usuarios = [];
      var requestObject = {
        tabla: "usuario",
      };
      this.$axios
        .get(url, { params: requestObject })
        .then((response) => {
          this.usuarios = response.data;
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
    },
    delUser() {
      var url = jsonInfo.url_server + jsonInfo.name_app + "/globals/delete.php";
      var requestObject = {
        tabla: "usuario",
        id: this.usuarioSeleccionado.id,
      };
      this.$axios
        .post(url, requestObject)
        .then((response) => {
          if (response.data == true) alert(this.mssg);
          this.loadUsers();
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
    },
  },
  beforeCreate() {
    this.$bus.$emit("checkSession", "");
  },
  created() {
    this.loadUsers();
    console.log("Moduser.vue");
  },
};
</script>

<style>
</style>