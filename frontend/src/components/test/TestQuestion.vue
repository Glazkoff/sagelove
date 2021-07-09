<template>
  <v-flex>
    <div>
      <h1 class="title text-center mt-5 mb-5">
        Опросник о ваших предпочтениях
      </h1>
      <v-row>
        <v-col>
          <div>
            <h3 class="colorOfSea--text">{{ progress }}%</h3>
          </div>
        </v-col>
        <v-col>
          <div class="text-right">
            <v-btn
              dark
              color="colorOfSea"
              class="my-button"
              @click="onContinueLater"
            >
              Продолжу позже
            </v-btn>
          </div>
        </v-col>
      </v-row>
      <v-progress-linear
        :value="progress"
        class="mt-2 mb-4"
        color="colorOfSea"
        height="8"
      ></v-progress-linear>
      <h2 class="title colorOfSea--text">
        Тема № {{ orderNumber }}.
        {{ nameGroupQuestion }}
      </h2>
      <div
        v-for="(questionElem, question_index) in questionsSet"
        :key="question_index"
      >
        <div v-if="questionElem.type == WITH_SCALE_TYPE">
          <p>
            {{ question_index + 1 }}. {{ questionElem.question.questionText }}
          </p>
          <div>
            <v-row
              v-for="answer in questionElem.question.answerscaleSet"
              :key="answer.id"
            >
              <v-col
                class="align-center d-flex align-items-center"
                cols="12"
                xs="12"
                sm="2"
                md="2"
                lg="2"
              >
                <p class="text-right question-side">
                  {{ answer.leftAnswerText }}
                </p>
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
                  v-model="userAnswers[question_index]"
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
                  {{ answer.rightAnswerText }}
                </p>
              </v-col>
            </v-row>
            <v-divider class="mt-4 mb-4 mobile-divider"></v-divider>
          </div>
        </div>
        <div v-else-if="questionElem.type == WITH_OPTIONS_TYPE">
          <p>
            {{ question_index + 1 }}. {{ questionElem.question.questionText }}
          </p>
          <!-- <v-radio-group v-model="radioGroup"> -->
          <v-radio-group v-model="userAnswers[question_index]">
            <v-radio
              v-for="answer in questionElem.question.answeroptionSet"
              :key="answer.id"
              :label="answer.answerText"
              :value="answer.id"
              color="colorOfSea"
            ></v-radio>
          </v-radio-group>
        </div>
      </div>
      <v-row>
        <v-col>
          <div class="text-left">
            <v-btn
              dark
              color="colorOfSea"
              class="my-button"
              v-if="prevGroupId !== null"
              @click="goToPrevGroup"
              >Назад</v-btn
            >
          </div>
        </v-col>
        <v-col>
          <div class="text-right">
            <v-btn
              v-if="nextGroupId !== null"
              dark
              color="colorOfSea"
              class="my-button"
              @click="goToNextGroup"
              >Далее</v-btn
            >
          </div>
        </v-col>
      </v-row>
    </div>
  </v-flex>
</template>

<script>
import {
  QUESTION_GROUP,
  QUESTION_GROUP_COUNT
} from "@/graphql/questions_queries";

export default {
  name: "TestQuestion",
  apollo: {
    questionGroup: {
      query: QUESTION_GROUP,
      variables() {
        return {
          questionGroupId: this.groupId
        };
      }
    },
    questionGroupsCount: {
      query: QUESTION_GROUP_COUNT
    }
  },
  data() {
    return {
      WITH_SCALE_TYPE: "with_scale",
      WITH_OPTIONS_TYPE: "with_options",
      value: 2,
      clientWidth: null,
      isLessThen600px: false,
      ticksLabels: [
        "Да",
        "Скорее да, чем нет",
        "Ни один из ответов",
        "Скорее да, чем нет",
        "Да"
      ],
      userAnswers: []
    };
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
    },
    onContinueLater() {
      // TODO: синхронизация результатов
      this.$router.push("/test");
    },
    goToNextGroup() {
      this.userAnswers = [];
      this.$router.push(`/question/${this.nextGroupId}`);
    },
    goToPrevGroup() {
      this.userAnswers = [];
      this.$router.push(`/question/${this.prevGroupId}`);
    }
  },
  watch: {
    clientWidth() {
      this.isLessThen600px = this.clientWidth < 600;
    },
    questionGroup() {
      if (
        !this.$apollo.queries.questionGroup.loading &&
        this.questionGroup == null
      ) {
        console.log(null);
      }
    },
    userAnswers(val) {
      console.log(val);
    }
  },
  computed: {
    groupId() {
      return this.$route.params.id;
    },
    progress() {
      if (this.questionGroup !== null && this.questionGroup !== undefined) {
        return Math.ceil(
          ((this.questionGroup.orderNumber - 1) / this.questionGroupsCount) *
            100
        );
      } else {
        return 0;
      }
    },
    orderNumber() {
      return this.questionGroup != null ? this.questionGroup.orderNumber : "-";
    },
    nameGroupQuestion() {
      return this.questionGroup != null
        ? this.questionGroup.nameGroupQuestion
        : "-";
    },
    questionsSet() {
      let questionsSet = [];
      if (this.questionGroup !== null && this.questionGroup !== undefined) {
        this.questionGroup.questionwithscaleSet.forEach(question => {
          questionsSet.push({
            type: this.WITH_SCALE_TYPE,
            question
          });
        });
        this.questionGroup.questionwithoptionSet.forEach(question => {
          questionsSet.push({
            type: this.WITH_OPTIONS_TYPE,
            question
          });
        });
      }
      return questionsSet;
    },
    nextGroupId() {
      if (this.questionGroup !== null && this.questionGroup !== undefined) {
        return this.questionGroup.nextGroupId;
      } else {
        return null;
      }
    },
    prevGroupId() {
      if (this.questionGroup !== null && this.questionGroup !== undefined) {
        return this.questionGroup.prevGroupId;
      } else {
        return null;
      }
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
