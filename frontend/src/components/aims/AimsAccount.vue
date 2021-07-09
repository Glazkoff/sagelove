<template>
  <v-flex>
    <h1 class="title mb-12 text-center mb-5 mt-5 mb-sm-10 mt-sm-10">Цели</h1>
    <div class="d-flex justify-center">
      <div class="background-aimsaccount rounded-lg pa-8">
        <v-row class="direction-block">
          <v-col><p class="dark-blue-text">Я ищу партнера:</p></v-col>
          <v-col><p class="gray-text">для создания семьи</p></v-col>
        </v-row>
        <v-row class="direction-block">
          <v-col><p class="dark-blue-text">Я хочу встретить:</p></v-col>
          <v-col><p class="gray-text">такого, как я</p></v-col>
        </v-row>
        <v-row class="direction-block">
          <v-col><p class="dark-blue-text">Моя история по ощущениям:</p></v-col>
          <v-col
            ><img src="../../assets/img/6.jpg" alt="" class="width-img-history"
          /></v-col>
        </v-row>
        <v-btn
          class="mt-8 my-button white--text"
          color="colorOfSea"
          block="block"
          type="submit"
          to="/aimsaccountedit"
        >
          Изменить
        </v-btn>
      </div>
    </div>
  </v-flex>
</template>

<script>
export default {
  name: "AimsAccount",
  data() {
    return {};
  }
};
</script>

<style lang="scss" scoped>
.dark-blue-text {
  color: var(--v-darkBlue-base) !important;
}
.gray-text {
  color: rgba(148, 148, 148, 1) !important;
}
.background-aimsaccount {
  background-color: #e2f9fc !important;
  filter: drop-shadow(0 0 4px rgba(0, 0, 0, 0.25));
}
.width-img-history {
  width: 100%;
}
@media (max-width: 500px) {
  .direction-block {
    flex-direction: column !important;
  }
}
</style>
