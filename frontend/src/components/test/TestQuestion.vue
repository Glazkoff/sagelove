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
      <div v-for="i in 2" :key="i">
        <v-row>
          <v-col
            class="align-center d-flex align-items-center"
            cols="12"
            xs="12"
            sm="2"
            md="2"
            lg="2"
          >
            <p class="text-right question-side">Лилия, фрезия, роза</p>
          </v-col>
          <v-col
            class="align-center d-flex align-items-center question-slider"
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
              :vertical="isLessThen600px"
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
            <p class="text-left question-side">
              Цветочные ароматы и интересные цветочные композиции без привязки к
              запаху какого-то цветка
            </p>
          </v-col>
        </v-row>
        <v-divider class="mt-4 mb-4 mobile-divider"></v-divider>
      </div>
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
// TODO: добавить проверку экрана на ширину для вертикального слайдера
export default {
  name: "TestQuestion",
  data() {
    return {
      value: 2,
      clientWidth: null,
      isLessThen600px: false,
      ticksLabels: [
        "Да",
        "Скорее да, чем нет",
        "Ни один из ответов",
        "Скорее да, чем нет",
        "Да"
      ]
    };
  },
  computed: {
    media() {
      return {
        "is-phone": this.$screen.sm,
        "is-tablet": this.$screen.md,
        "is-desktop": this.$screen.lg,
        "can-touch": this.$screen.touch,
        breakpoint: this.$screen.breakpoint
      };
    }
  },
  created() {
    window.addEventListener("resize", this.resizeHandler);
    this.clientWidth = document.body.clientWidth;
  },
  destroyed() {
    window.removeEventListener("resize", this.resizeHandler);
  },
  methods: {
    resizeHandler() {
      let width = document.body.clientWidth + 16;
      this.clientWidth = width;
    }
  },
  watch: {
    clientWidth() {
      this.isLessThen600px = this.clientWidth < 600;
    }
  }
};
</script>

<style lang="scss">
.v-slider__tick-label {
  white-space: unset !important;
  width: 100px;
  text-align: center;
  font-weight: bold;
}
.v-slider__tick:first-child .v-slider__tick-label {
  text-align: left;
}
.v-slider__tick:last-child .v-slider__tick-label {
  text-align: right;
}
.v-slider--vertical {
  min-height: 230px !important;
  .v-slider__tick-label {
    text-align: left;
    width: 170px;
  }
  .v-slider__tick:first-child .v-slider__tick-label {
    text-align: left;
  }
  .v-slider__tick:last-child .v-slider__tick-label {
    text-align: left;
  }
}

.mobile-divider {
  display: none !important;
}

@media screen and (max-width: 600px) {
  p.question-side {
    margin-bottom: 0px !important;
  }
  .question-slider {
    .v-input__slot {
      // display: block !important;
      // justify-content: flex-start !important;
      width: 0%;
      margin-left: 20px !important;
    }
  }
  .mobile-divider {
    display: block !important;
  }
}
</style>
