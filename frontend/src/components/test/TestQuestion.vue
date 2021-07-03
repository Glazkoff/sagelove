<template>
  <v-flex>
    <div>
      <h1 class="title text-center mt-5 mb-5">
        Опросник о ваших предпочтениях
      </h1>
      <v-row>
        <v-col>
          <div>
            <h3 class="colorOfSea--text">41%</h3>
          </div>
        </v-col>
        <v-col>
          <div class="text-right">
            <v-btn dark color="colorOfSea" class="my-button"
              >Продолжу позже</v-btn
            >
          </div>
        </v-col>
      </v-row>
      <v-progress-linear
        value="41"
        class="mt-2 mb-4"
        color="colorOfSea"
        height="8"
      ></v-progress-linear>
      <h2 class="title colorOfSea--text">Тема № 1. Запахи</h2>
      <p>2. Какие запахи духов Вы обчно выбираете для себя?</p>
      <v-row v-for="i in 2" :key="i">
        <v-col
          class="align-center d-flex align-items-center"
          cols="12"
          xs="12"
          sm="2"
          md="2"
          lg="2"
        >
          <p class="text-right">Лилия, фрезия, роза</p>
        </v-col>
        <v-col
          class="align-center d-flex align-items-center"
          cols="12"
          xs="12"
          sm="8"
          md="8"
          lg="8"
        >
          <v-slider
            v-model="value"
            color="colorOfSea"
            track-color="colorOfSea"
            thumb-color="colorOfSea"
            :tick-labels="ticksLabels"
            ticks="always"
            tick-size="4"
            :max="4"
            step="1"
          ></v-slider>
        </v-col>
        <v-col
          class="align-center d-flex align-items-center"
          cols="12"
          xs="12"
          sm="2"
          md="2"
          lg="2"
        >
          <p class="text-left">
            Цветочные ароматы и интересные цветочные композиции без привязки к
            запаху какого-то цветка
          </p>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <div class="text-left">
            <v-btn dark color="colorOfSea">Назад</v-btn>
          </div>
        </v-col>
        <v-col>
          <div class="text-right">
            <v-btn dark color="colorOfSea">Далее</v-btn>
          </div>
        </v-col>
      </v-row>
    </div>
  </v-flex>
</template>

<script>
function getWidth() {
  if (self.innerWidth) {
    return self.innerWidth;
  }

  if (document.documentElement && document.documentElement.clientWidth) {
    return document.documentElement.clientWidth;
  }

  if (document.body) {
    return document.body.clientWidth;
  }
}

export default {
  name: "TestQuestion",
  data() {
    return {
      value: 2,
      ticksLabels: [
        "Да",
        "Скорее да, чем нет",
        "Ни один из ответов",
        "Скорее да, чем нет",
        "Да"
      ]
    };
  }
};
</script>

<style lang="scss">
.v-slider__tick-label {
  white-space: unset !important;
  width: 100px;
  text-align: center;
}
.v-slider__tick:first-child .v-slider__tick-label {
  text-align: left;
}
.v-slider__tick:last-child .v-slider__tick-label {
  text-align: right;
}
</style>
