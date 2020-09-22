<template>
  <div class="moduser">
    <div class="content-moduser">
      <div class="field">
        <div class="control">
          <form @submit.prevent.once="selUser" autocomplete="off">
            <div class="field">
              <label class="label">Seleccione el usuario a modificar</label>
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
                <button class="button is-link is-fullwidth">Modificar</button>
              </div>
            </div>
          </form>
        </div>
      </div>
      <div class="field" v-show="seleccionado">
        <div class="control">
          <form @submit.prevent.once="modUser">
            <div class="field">
              <div class="control">
                <label class="label">Tipo y número de documento</label>
              </div>
              <div class="field has-addons">
                <div class="control">
                  <div class="select">
                    <select v-model="usuarioSeleccionado.tipo_identificacion">
                      <option>CC</option>
                      <option>CE</option>
                    </select>
                  </div>
                </div>
                <div class="control">
                  <input
                    class="input is-expanded"
                    type="number"
                    placeholder="numero de documento"
                    v-model="usuarioSeleccionado.identificacion"
                  />
                </div>
              </div>
            </div>
            <div class="field">
              <label class="label">Nombres Completos</label>
              <div class="control">
                <input
                  class="input is-medium"
                  type="text"
                  placeholder="Nombres"
                  v-model="usuarioSeleccionado.nombres"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Apellidos</label>
              <div class="control">
                <input
                  class="input is-medium"
                  type="text"
                  placeholder="Apellidos"
                  v-model="usuarioSeleccionado.apellidos"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Usuario</label>
              <div class="control">
                <input
                  class="input is-medium"
                  type="text"
                  placeholder="Usuario"
                  v-model="usuarioSeleccionado.usuario"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Contraseña</label>
              <div class="control">
                <input
                  class="input is-medium"
                  type="password"
                  placeholder="Contraseña"
                  v-model="usuarioSeleccionado.password"
                  autocomplete="new-password"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Dirección de correo electrónico</label>
              <div class="control">
                <input
                  class="input is-medium"
                  type="email"
                  placeholder="Correo electrónico"
                  v-model="usuarioSeleccionado.email"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Número de teléfono fijo</label>
              <div class="control">
                <input
                  class="input is-medium"
                  type="tel"
                  pattern="[0-9]{7}"
                  title="Un número de telefono fijo tiene una longitud de 7 digitos con números entre 0 y 9"
                  placeholder="telefono fijo"
                  v-model="usuarioSeleccionado.telefono"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Número de teléfono celular</label>
              <div class="control">
                <input
                  class="input is-medium"
                  type="tel"
                  pattern="[3]{1}[0-9]{9}"
                  title="Un número de celular en Colombia inicia con el número 3 y tiene una longitud de 10 digitos con números entre 0 y 9"
                  placeholder="celular"
                  v-model="usuarioSeleccionado.celular"
                />
              </div>
            </div>
            <div class="field">
              <div class="control">
                <label class="label">Tipo de usuario</label>
              </div>
              <div class="field">
                <div class="control">
                  <div class="select">
                    <select v-model="usuarioSeleccionado.tipo_usuario">
                      <option v-if="root_admin === 'R'">Administrador</option>
                      <option>Cliente</option>
                      <option>Guardia de seguridad</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <button class="button is-link is-fullwidth">Aceptar</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import * as crypto from "crypto-js";
export default {
  name: "Moduser",
  data() {
    return {
      mssg: "Usuario modificado con éxito",
      selusuario: "Seleccione un usuario",
      usuarios: [],
      usuarioSeleccionado: {},
      seleccionado: false,
      tipo_usr: "Cliente",
      tipo_doc: "CC",
      root_admin: "",
    };
  },
  methods: {
    loadUsers() {
      this.seleccionado = false;
      this.usuarioSeleccionado = {};
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
    selUser() {
      this.seleccionado = true;
    },
    modUser() {
      console.log(this.usuarioSeleccionado);
      this.usuarioSeleccionado.tabla = "usuario";
      this.usuarioSeleccionado.nombres = this.usuarioSeleccionado.nombres.toUpperCase();
      this.usuarioSeleccionado.apellidos = this.usuarioSeleccionado.nombres.toUpperCase();
      this.usuarioSeleccionado.password = crypto
        .SHA512(this.usuarioSeleccionado.password)
        .toString();
      this.usuarioSeleccionado.email = this.usuarioSeleccionado.email.toUpperCase();
      this.usuarioSeleccionado.tipo_usuario = this.usuarioSeleccionado.tipo_usuario.charAt(
        0
      );
      this.$axios
        .post("MainServlet/update", this.usuarioSeleccionado)
        .then((response) => {
          alert(this.mssg);
          this.loadUsers();
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
      this.seleccionado = false;
    },
  },
  created() {
    this.root_admin = this.$route.params.usuario;
    this.loadUsers();
    console.log("Moduser.vue");
  },
};
</script>

<style>
</style>