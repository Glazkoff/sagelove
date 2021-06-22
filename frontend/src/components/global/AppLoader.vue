<template>
  <div class="text-center">
    <v-dialog v-model="dialog" class="pa-2 d-flex" width="400" persistent>
      <v-card
        class="pa-2 d-flex flex-column justify-space-between align-center"
        width="400"
      >
        <h2 class="text-center title">Пожалуйста, подождите</h2>
        <v-progress-circular
          indeterminate
          color="colorOfSea"
          class="mt-4 mb-4"
        ></v-progress-circular>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: "AppLoader",
  data() {
    return {
      dialog: true
    };
  }
};
</script>

<style lang="scss" scoped></style>
