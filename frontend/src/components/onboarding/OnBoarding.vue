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
      ><v-carousel-item>
        <div class="position-cross mr-3">
          <img
            src="../../assets/img/cross.svg"
            alt="Cross"
            class="mt-5 pr-5"
            @click="onWatchOnBoarding()"
          />
        </div>
        <div class="position-text">
          <v-sheet :color="lightBlue" height="100%">
            <h1 class="title mb-5 mt-5 mb-sm-10 mt-sm-10">Привет!</h1>
            <v-row class="my-3" justify="center">
              <p class="mobile-padding-text">
                Сайт SageLove - это пространство для тех, кто хочет создать
                семью или ищет серьёзные отношения.
              </p>
              <p class="mobile-padding-text">
                Здесь на основании умного математического алгоритма Вы можете
                пригласить в свою жизнь родственную душу или полную свою
                противоположность.
              </p>
              <p class="mobile-padding-text">
                Листай и на следующей странице ознакомишься с простыми правилами
              </p>
            </v-row>
          </v-sheet>
        </div>
        <!-- <div class="background-sliders"></div> -->
      </v-carousel-item>
      <v-carousel-item>
        <div class="position-cross mr-3">
          <img
            src="../../assets/img/cross.svg"
            alt="Cross"
            class="mt-5 pr-5"
            @click="onWatchOnBoarding()"
          />
        </div>
        <div class="position-text">
          <v-sheet :color="lightBlue" height="100%">
            <h1 class="title mb-5 mt-5 mb-sm-10 mt-sm-10">Правила SageLove:</h1>
            <v-row class="my-3" justify="center">
              <ol class="mobile-padding-text">
                <li>
                  При регистрации в анкете укажи правдиво дату рождения, пол,
                  критерии поиска, образ отношений, который будет представлен на
                  картинках. Если ни один из образов не соответствует твоим
                  представлениям, то выбирай картинку с чистым листом бумаги как
                  говорят "Начнем с чистого листа".
                </li>
                <li>
                  Далее последует тест из 64 вопросов, при заполнении которого
                  Вы в любой момент можете остановиться и продолжить позже. При
                  заполнении теста о своих предпочтениях укажите максимально
                  точно свои привычки и предпочтения. Помните в алгоритме
                  математический расчет, поэтому важно быть искренним.
                </li>
                <li>
                  После заполнения опросника о себе и о критериях поиска Вашего
                  любимого человека, Вам будут предложены по заданным параметрам
                  кандидаты, для знакомства.
                </li>
                <li>
                  Вы можете начать с ними общаться, соблюдая этикет и не
                  допуская употребления нецензурной лексики. В случае, если с
                  кем-то контакт не сложился - можно просто удалить чат.
                </li>
              </ol>
            </v-row>
          </v-sheet>
        </div>
        <!-- <div class="background-sliders"></div> --> </v-carousel-item
      ><v-carousel-item>
        <div class="position-cross mr-3">
          <img
            src="../../assets/img/cross.svg"
            alt="Cross"
            class="mt-5 pr-5"
            @click="onWatchOnBoarding()"
          />
        </div>
        <div class="position-text">
          <v-sheet :color="lightBlue" height="100%">
            <h1 class="title mb-5 mt-5 mb-sm-10 mt-sm-10">Стоимость</h1>
            <v-row class="my-3" justify="center">
              <p class="mobile-padding-text">
                Стоимость данного ресурса состоит из двух частей: первичный
                взнос в размере 10 000руб и далее ежемесячно 5000 руб до момента
                пока Вы не примете решение остановиться и не покинете наш сайт.
                Да, цель данного ресурса - максимально точно и быстро найти Вам
                человека в соответствии с Вашим запросом и сподвигнуть Вас на
                общение, а далее Вы и без нас справитесь........ а у нас есть
                чем заняться)))
              </p>
            </v-row>
          </v-sheet>
        </div>
        <!-- <div class="background-sliders"></div> --> </v-carousel-item
      ><v-carousel-item>
        <div class="position-cross mr-3">
          <img
            src="../../assets/img/cross.svg"
            alt="Cross"
            class="mt-5 pr-5"
            @click="onWatchOnBoarding()"
          />
        </div>
        <div class="position-text">
          <v-sheet :color="lightBlue" height="100%">
            <h1 class="title mb-5 mt-5 mb-sm-10 mt-sm-10">
              Мы всегда рады помочь Вам!
            </h1>
            <v-row class="my-3" justify="center">
              <p class="mobile-padding-text">
                При наличии любых вопросов пишите в службу подержки, мы
                обязательно ответим в течение ближайшего рабочего дня
                <br />
                <a class="link" href="mailto:info@sagelave.ru"
                  >info@sagelave.ru</a
                >
              </p>
            </v-row>
          </v-sheet>
        </div>
        <!-- <div class="background-sliders"></div> -->
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
      lightBlue: "#E2F9FC"
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
// .background-sliders {
//   filter: brightness(65%) blur(1px);
//   background-color: white;
//   background-size: cover;
//   width: 100%;
//   height: 100%;
//   position: absolute;
//   left: 0;
//   right: 0;
//   top: 0;
//   bottom: 0;
//   z-index: -10;
// }
.position-text {
  z-index: 10;
}

div.v-carousel div.v-carousel__controls {
  background: rgba(0, 0, 0, 0) !important;
}
p {
  color: var(--v-darkBlue-base) !important;
  text-align: center;
  max-width: 40.25rem;
}
ol {
  color: var(--v-darkBlue-base) !important;
  text-align: center;
  max-width: 40.25rem;
}
h1 {
  text-align: center;
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
