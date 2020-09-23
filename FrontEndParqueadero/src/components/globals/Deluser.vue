<template>
  <div class="deluser">
    <div class="content-deluser">
      <div class="field">
        <div class="control">
          <form @submit.prevent.once="delUser" autocomplete="off">
            <div class="field">
              <label class="label">Seleccione el usuario a eliminar</label>
              <div class="control">
                <div class="select">
                  <select v-model="usuarioSeleccionado">
                    <option>{{selusuario}}</option>
                    <option
                      v-for="usuario in usuarios"
                      :value="usuario"
                      v-bind:key="usuario.identificacion"
                    >{{usuario.nombres}} {{usuario.apellidos}}</option>
                  </select>
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
export default {
  name: "Deluser",
  data() {
    return {
      mssg: "Usuario eliminado con éxito",
      selusuario: "Seleccione un usuario...",
      usuarios: [],
      usuarioSeleccionado: {},
      seleccionado: false,
      error: false,
      root_admin: "",
    };
  },
  methods: {
    loadUsers() {
      this.usuarios = [];
      var requestObject = {
        tabla: "usuario",
      };
      this.$axios
        .post("MainServlet/getInformation", requestObject)
        .then((response) => {
          this.usuarios = response.data;
          console.log(this.usuarios);
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
    },
    delUser() {
      this.seleccionado = true;
      console.log(this.usuarioSeleccionado);
      var requestObject = {
        tabla: "usuario",
        id: this.usuarioSeleccionado.id,
      };
      this.$axios
        .post("MainServlet/delete", requestObject)
        .then((response) => {
          alert(this.mssg);
          this.loadUsers();
          console.log(this.usuarios);
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
    },
  },
  beforeCreate(){
      this.$bus.$emit("checkSession", "");
  },
  created() {
    this.root_admin = localStorage.usuario;
    this.loadUsers();
    console.log("Moduser.vue");
  },
};
</script>

<style>
</style>