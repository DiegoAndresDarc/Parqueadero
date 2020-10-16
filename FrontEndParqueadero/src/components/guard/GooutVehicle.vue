<template>
  <div class="guard">
    <div class="content">
      <form @submit.prevent="goOutVehicle">
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Código de barras del carnet</label>
          </div>
          <div class="field-body">
            <input class="input" type="text" v-model="codigo" required />
          </div>
        </div>
        <div class="field">
            <div class="control">
                <button class="button is-fullwidth is-link">Aceptar</button>
            </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "goOutVehicle",
  data() {
    return {
      fecha: "",
      codigo: "",
    };
  },
  methods: {
      goOutVehicle(){
          
      }
  },
  beforeCreate() {
    this.$bus.$emit("checkSession", "");
  },
  created() {},
};
</script>

<style>
</style>