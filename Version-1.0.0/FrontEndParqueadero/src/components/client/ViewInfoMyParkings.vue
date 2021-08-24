<template>
  <div class="view-info">
    <div class="content">
        <table class="table">
            <thead></thead>
            <tbody></tbody>
        </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "viewInfoMyParkings",
  data() {
    return {
      mssg: "",
    };
  },
  methods: {
    loadMyParkings() {},
  },
  beforeCreate() {
    this.$bus.$emit("checkSession", "");
  },
  created() {
    this.loadMyParkings();
  },
};
</script>

<style>
</style>