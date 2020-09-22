<template>
  <div class="recoverPassword">
    <div class="head">
      <nav class="navbar"></nav>
    </div>
    <div class="box clogin content-recoverPsswd">
      <div class="field">
        <form @submit.prevent="recoverPassword()" autocomplete="off">
          <h1 class="subtitle is-size-3">Recuperar contraseña</h1>
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
              <transition name="slide">
                <p
                  v-if="success"
                  class="help is-success is-medium"
                >Si el correo electrónico digitado está asociado a una cuenta, se le enviará al correo electrónico su nueva contraseña.</p>
              </transition>
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-colorcustom">Recuperar contraseña</button>
            </div>
          </div>
        </form>
      </div>
      <div class="field">
        <div class="control">
          <button class="button is-colorcustom" v-on:click="cancelar">Cancelar</button>
        </div>
      </div>
    </div>
    <div class="foot">
      <nav class="navbar"></nav>
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
      success: false,
    };
  },
  methods: {
    recoverPassword() {
      console.log("Recuperar contraseña");
      var responseObject = {
        email: document.getElementById("email"),
      };
      this.$axios
        .post("MainServlet/recoverPassword", responseObject)
        .then((response) => {
          this.success = true;
          waitToBack();
          this.$router.push("/login");
        })
        .catch((e) => {
          console.log(e);
        });
    },
    cancelar(event) {
      //Limpiar la pantalla
      this.$router.push("/login");
    },
    waitToBack() {
      this.seg = 0;
      setInterval(() => {
        this.seg += 1;
        if (this.seg === 3) {
          this.success = false;
        }
      }, 2000);
    },
  },
  created() {
    console.log("RecoverPassword.vue");
  },
};
</script>
<style>
</style>