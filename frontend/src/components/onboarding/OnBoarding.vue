<template>
  <div>
    <v-carousel height="37.5rem" class="rounded-lg my-4" show-arrows-on-hover>
      <template v-slot:prev="{ on, attrs }">
        <img
          src="../../assets/img/arrow.svg"
          alt="arrow-left"
          v-bind="attrs"
          v-on="on"
          width="35"
          class="rotate-arrow mx-5"
        />
      </template>
      <template v-slot:next="{ on, attrs }">
        <!-- <router-link to="/aims"
          ><img src="../../assets/img/arrow.svg" alt="arrow-right" width="35"
        /></router-link> -->
        <img
          src="../../assets/img/arrow.svg"
          alt="arrow-right"
          v-bind="attrs"
          v-on="on"
          width="35"
          class="mx-5"
        /> </template
      ><v-carousel-item
        v-for="(slide, i) in slides"
        :key="i"
        class="my-carousel"
      >
        <div class="position-cross mr-3">
          <img
            src="../../assets/img/cross.svg"
            alt="Cross"
            class="mt-5 pr-5"
            @click="onWatchOnBoarding()"
          />
        </div>
        <div class="position-text">
          <h1 class="title mb-5 mt-5 mb-sm-10 mt-sm-10">{{ slide.header }}</h1>
          <v-row class="my-3" justify="center">
            <p class="mobile-padding-text">{{ slide.text }}</p>
          </v-row>
        </div>
        <div class="background-sliders"></div>
      </v-carousel-item>
    </v-carousel>
  </div>
</template>

<script>
import { WATCH_ON_BOARDING } from "../../graphql/user_queries.js";
import { UPDATE_WATCH_ON_BOARDING } from "../../graphql/user_mutations.js";
export default {
  name: "OnBoarding",
  apollo: {
    user: {
      query: WATCH_ON_BOARDING,
      variables() {
        return { userId: this.$store.getters.user_id };
      }
    }
  },
  watch: {
    user: function (val) {
      let route = "";
      if (val != undefined) {
        switch (val.watchOnBoarding) {
          case true:
          default:
            route = { name: "TestStatus" };
            break;
          case false:
            route = "";
            break;
        }
        if (
          this.$route.path != route &&
          this.$route.path.substring(0, this.$route.path.length - 1) != route
        ) {
          this.$router.push(route);
        }
      }
    }
  },
  methods: {
    onWatchOnBoarding() {
      this.$apollo
        .mutate({
          mutation: UPDATE_WATCH_ON_BOARDING,
          variables: {
            watchOnBoarding: true,
            userId: this.$store.getters.user_id
          }
        })
        .then(() => {})
        .catch(err => {
          console.log(err);
        });
      if (this.user.partnerType != null) {
        this.$router.push({ name: "TestStatus" });
      } else this.$router.push({ name: "AimsSignUp" });
    }
  },
  data() {
    return {
      slides: [
        {
          header: "Привет",
          text: "У каждой истории есть песня… или мелодия.  И у нашего сайта знакомств несколько историй и несколько мелодий, которые будут появляться для тебя путем случайного выбора.  Этот сайт создан для поиска отношений с человеком, о котором ты мечтаешь путем подбора кандидатуры по  математическому алгоритму и психологическому совпадению. Сайт не является брачным агентством или сайтом для однодневных знакомств, где ты можешь опасаться или не доверять предложенному тебе кандидату. На нашем сайте ты познакомишься с человеком, с котором действительно хочешь встретиться при условии соблюдения 4-х правил. Звучит интригующе?   попробуй и если это не так, то мы вернем тебе деньги за регистрацию на сайте и угостим чашечкой ароматного кофе ...... ну что, изучишь правила нашего сайта знакомств?"
        },
        {
          header: "",
          text: "второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд второй слайд"
        },
        {
          header: "",
          text: "третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд третий слайд"
        },
        {
          header: "",
          text: "четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд четвертый слайд"
        },
        {
          header: "",
          text: "пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый слайд пятый"
        }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
.position-cross {
  position: absolute;
  top: 0;
  right: 0;
  width: 3rem;
}
.rotate-arrow {
  transform: rotate(180deg);
}
.background-sliders {
  filter: brightness(65%) blur(1px);
  background-image: url(../../assets/img/background.jpg);
  background-size: cover;
  width: 100%;
  height: 100%;
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: -10;
}
.position-text {
  z-index: 10;
}

div.v-carousel div.v-carousel__controls {
  background: rgba(0, 0, 0, 0) !important;
}
p {
  color: white !important;
  text-align: center;
  max-width: 40.25rem;
}
h1 {
  text-align: center;
  color: white !important;
  margin-top: 5.125rem;
  margin-bottom: 4.375rem;
}
.v-btn__content {
  color: #00acc2 !important;
}
@media (max-width: 750px) {
  p {
    padding-right: 4rem;
    padding-left: 4rem;
  }
  .position-cross img {
    width: 3rem;
  }
}
</style>
