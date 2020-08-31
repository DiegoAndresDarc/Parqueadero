<template>
  <div class="recoverPassword">
    <div class="content-recoverPsswd">
      <div class="field">
        <form @submit.prevent="recoverPassword()" autocomplete="off">
          <h1>Recuperar contraseña</h1>
          <div class="field">
            <label class="label">Digite el correo electrónico asociado a la cuenta</label>
            <div class="control">
              <input
                class="input is-medium"
                type="email"
                placeholder="Correo electrónico"
                id="email"
                required
              />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-link is-fullwidth is-medium">Recuperar contraseña</button>
            </div>
          </div>
        </form>
      </div>
      <div class="field">
        <div class="control">
          <button
            class="button is-fullwidth is-medium is-link is-light"
            v-on:click="cancelar"
          >Cancelar</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "recoverPassword",
  components: {},
  data() {
    return {
      message: "Confirmación de clave",
    };
  },
  methods: {
    recoverPassword() {
        console.log("Recuperar contraseña");
    },
    cancelar(event) {
      //Limpiar la pantalla
      this.$router.push("/");
    },
  },
  created() {
    console.log("RecoverPassword.vue");
  },
};
</script>
<style>
</style>