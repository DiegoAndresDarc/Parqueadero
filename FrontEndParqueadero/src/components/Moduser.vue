<template>
  <div class="moduser">
    <div class="content-moduser">
      <div class="field">
        <div class="control">
          <form @submit.prevent.once="modUser" autocomplete="off">
            <div class="field">
              <label class="label">Seleccione el usuario a modificar</label>
              <div class="control">
                <div class="select">
                  <select v-model="usuarioSeleccionado">
                    <option>{{selusuario}}</option>
                    <option
                      v-for="usuario in usuarios"
                      :value="usuario"
                      v-bind:key="usuario.id"
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
        <div class="field-set" v-show="seleccionado">
          <div class="control">
            <form v-for="(item,index) in usuarioSeleccionado" v-bind:key="index" class="fieldset">
              <div class="field" v-if="index === 'tipo_identificacion' || index === 'tipo_usuario'">
                <div class="control">
                  <label class="label">{{index}}</label>
                </div>
                <div class="field-body">
                  <div class="control">
                    <div class="select" v-if="index === 'tipo_usuario'">
                      <select v-model="tipo_usr">
                        <option v-if="root_admin === 'R'">Administrador</option>
                        <option>Cliente</option>
                        <option>Guardia de seguridad</option>
                      </select>
                    </div>
                    <div class="select" v-else>
                      <select v-model="tipo_doc">
                        <option>CC</option>
                        <option>CE</option>
                      </select>
                    </div>
                  </div>
                </div>
              </div>
              <div class="field is-horizontal" v-else-if="index==='al_dia' || index=='sancionado'">
                <div class="field-label">
                  <label class="label">{{index}}</label>
                </div>
                <div class="field-body">
                  <div class="field is-narrow">
                    <div class="control">
                      <label class="radio">
                        <input type="radio" name="member" />
                        Si
                      </label>
                      <label class="radio">
                        <input type="radio" name="member" />
                        No
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="field" v-else>
                <label class="label">{{index}}</label>
                <div class="control">
                  <input
                    :type="index == 'password'?'password': index == 'email'?'email':'text'"
                    :value="item"
                  />
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
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Moduser",
  props: {
    root_admin: {
      type: String,
      default: "C",
    },
  },
  data() {
    return {
      mssg: "Usuario modificado con éxito",
      selusuario: "Seleccione un usuario",
      usuarios: [],
      usuarioSeleccionado: {},
      seleccionado: false,
      tipo_usr: "Cliente",
      tipo_doc: "CC",
    };
  },
  methods: {
    loadUsers() {
      this.usuarios = [];
      this.$axios
        .get("MainServlet/getUsers")
        .then((response) => {
          this.usuarios = response.data;
          console.log(this.usuarios);
        })
        .catch((e) => {
          console.log(e);
          this.error = true;
        });
    },
    modUser() {
      this.seleccionado = true;
      console.log(this.usuarioSeleccionado);
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