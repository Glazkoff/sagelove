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
        Тема № {{ orderNumber }}. {{ nameGroupQuestion }}
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
              v-for="(answer, answ_index) in questionElem.question
                .answerscaleSet"
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
                  :value="getSliderValue(question_index, answ_index)"
                  @input="setSliderValue($event, question_index, answ_index)"
                  @change="setSliderValue($event, question_index, answ_index)"
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
              @change="radioButtonChanged"
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
            >
              Далее
            </v-btn>
            <v-btn
              v-else
              dark
              color="colorOfSea"
              class="my-button"
              @click="finishTesting"
            >
              Завершить тестирование
            </v-btn>
          </div>
        </v-col>
      </v-row>
    </div>
  </v-flex>
</template>

<script>
import {
  QUESTION_GROUP,
  QUESTION_GROUP_COUNT,
  USER_GROUP_SCALE_ANSWERS,
  USER_GROUP_OPTION_ANSWERS
} from "@/graphql/questions_queries";
import {
  CREATE_USER_OPTION_ANSWER,
  CREATE_USER_SCALE_ANSWER,
  FINISH_USER_TESTING
} from "@/graphql/questions_mutations";
import { CREATE_DATINGS_ALGORITHMS } from "@/graphql/accounts_mutations";
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
    },
    userGroupScaleAnswers: {
      query: USER_GROUP_SCALE_ANSWERS,
      variables() {
        return {
          groupId: this.groupId,
          userId: this.$store.getters.user_id
        };
      }
    },
    userGroupOptionAnswers: {
      query: USER_GROUP_OPTION_ANSWERS,
      variables() {
        return {
          groupId: this.groupId,
          userId: this.$store.getters.user_id
        };
      }
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
    finishTesting() {
      this.$apollo
        .mutate({
          mutation: FINISH_USER_TESTING,
          variables: {
            userId: this.$store.getters.user_id
          }
        })
        .then(res => {
          this.$apollo.mutate({
            mutation: CREATE_DATINGS_ALGORITHMS,
            variables: {
              userFirst: this.$store.getters.user_id
            }
          });
          if (res.data.finishUserTesting.statusOk) {
            this.$router.push("/datings");
          }
        });
    },
    sendUserAnswers() {
      let group = this.groupId;
      return new Promise((resolve, reject) => {
        try {
          let userAnswersString = JSON.stringify(this.userAnswers);
          let userAnswers = JSON.parse(userAnswersString);

          for (let index = 0; index < this.questionsSet.length; index++) {
            const element = this.questionsSet[index];
            if (element.type == this.WITH_SCALE_TYPE) {
              for (
                let row_index = 0;
                row_index < element.question.answerscaleSet.length;
                row_index++
              ) {
                const scale_row = element.question.answerscaleSet[row_index];
                // console.log(
                //   `Type: with_scale, question_row_id: ${
                //     scale_row.id
                //   }, answer: ${userAnswers[index][row_index] + 1}`
                // );
                if (
                  userAnswers[index] !== null &&
                  userAnswers[index] != undefined
                ) {
                  if (
                    userAnswers[index][row_index] !== null &&
                    userAnswers[index][row_index] != undefined
                  ) {
                    this.$apollo.mutate({
                      mutation: CREATE_USER_SCALE_ANSWER,
                      variables: {
                        userId: this.$store.getters.user_id,
                        questionRowId: scale_row.id,
                        answer: userAnswers[index][row_index] + 1
                      },
                      update: (cache, { data: { createUserScaleAnswer } }) => {
                        const data = cache.readQuery({
                          query: USER_GROUP_SCALE_ANSWERS,
                          variables: {
                            groupId: group,
                            userId: this.$store.getters.user_id
                          }
                        });
                        let findIndex = data.userGroupScaleAnswers.findIndex(
                          el => {
                            return el.answerScaleLine.id == scale_row.id;
                          }
                        );
                        if (findIndex == -1) {
                          data.userGroupScaleAnswers.push(
                            createUserScaleAnswer.userScaleAnswer
                          );
                        } else {
                          data.userGroupScaleAnswers[findIndex] =
                            createUserScaleAnswer.userScaleAnswer;
                        }
                        cache.writeQuery({
                          query: USER_GROUP_SCALE_ANSWERS,
                          variables: {
                            groupId: this.groupId,
                            userId: this.$store.getters.user_id
                          },
                          data
                        });
                      }
                    });
                  }
                }
              }
            } else {
              // console.log(
              //   `Type: with_options, question_id: ${element.question.id}, answer: ${userAnswers[index]}`
              // );
              if (
                userAnswers[index] != null &&
                userAnswers[index] != undefined
              ) {
                this.$apollo.mutate({
                  mutation: CREATE_USER_OPTION_ANSWER,
                  variables: {
                    userId: this.$store.getters.user_id,
                    questionId: element.question.id,
                    answerId: userAnswers[index]
                  },
                  update: (cache, { data: { createUserOptionAnswer } }) => {
                    const data = cache.readQuery({
                      query: USER_GROUP_OPTION_ANSWERS,
                      variables: {
                        groupId: group,
                        userId: this.$store.getters.user_id
                      }
                    });
                    let findIndex = data.userGroupOptionAnswers.findIndex(
                      el => {
                        return el.questionWithOption.id == element.question.id;
                      }
                    );
                    if (findIndex == -1) {
                      data.userGroupOptionAnswers.push(
                        createUserOptionAnswer.userOptionAnswer
                      );
                    } else {
                      data.userGroupOptionAnswers[findIndex] =
                        createUserOptionAnswer.userOptionAnswer;
                    }
                    cache.writeQuery({
                      query: USER_GROUP_OPTION_ANSWERS,
                      variables: {
                        groupId: this.groupId,
                        userId: this.$store.getters.user_id
                      },
                      data
                    });
                  }
                });
              }
            }
          }
          resolve();
        } catch (error) {
          reject(error);
        }
      });
    },
    getSliderValue(question_index, answ_index) {
      if (this.userAnswers[question_index] != undefined) {
        if (this.userAnswers[question_index][answ_index] === undefined) {
          this.userAnswers[question_index][answ_index] = 2;
        }
      } else {
        this.userAnswers[question_index] = [];
        this.userAnswers[question_index][answ_index] = 2;
      }
      return this.userAnswers[question_index][answ_index];
    },
    radioButtonChanged() {
      this.sendUserAnswers();
    },
    setSliderValue(newValue, question_index, answ_index) {
      if (this.userAnswers[question_index] === undefined) {
        this.userAnswers[question_index] = [];
      }
      this.userAnswers[question_index][answ_index] = newValue;
      this.sendUserAnswers();
    },
    resizeHandler() {
      let width = document.body.clientWidth + 16;
      this.clientWidth = width;
    },
    onContinueLater() {
      // TODO: синхронизация результатов
      this.$router.push("/test");
    },
    goToNextGroup() {
      this.sendUserAnswers().then(() => {
        this.userAnswers = [];
        this.$router.push(`/question/${this.nextGroupId}`);
      });
    },
    goToPrevGroup() {
      this.sendUserAnswers().then(() => {
        this.userAnswers = [];
        this.$router.push(`/question/${this.prevGroupId}`);
      });
    }
  },
  watch: {
    groupId() {
      this.$apollo.queries.userGroupOptionAnswers.refetch();
      this.$apollo.queries.userGroupOptionAnswers.refresh();
      this.$apollo.queries.userGroupScaleAnswers.refetch();
      this.$apollo.queries.userGroupScaleAnswers.refresh();
    },
    clientWidth() {
      this.isLessThen600px = this.clientWidth < 600;
    },
    questionGroup() {
      if (
        !this.$apollo.queries.questionGroup.loading &&
        this.questionGroup == null
      ) {
        // console.log(null);
      }
    },
    userAnswers() {
      this.sendUserAnswers();
    },
    userGroupScaleAnswers(val) {
      if (val != undefined) {
        for (let index = 0; index < val.length; index++) {
          const question = val[index];
          if (question.type == this.WITH_SCALE_TYPE) {
            this.userAnswers[index] = [];
            for (
              let scaleIndex = 0;
              scaleIndex < question.question.answerscaleSet.length;
              scaleIndex++
            ) {
              const scaleLine = question.question.answerscaleSet[scaleIndex];

              if (val != undefined) {
                let answerIndex = val.findIndex(el => {
                  return el.answerScaleLine.id == scaleLine.id;
                });

                if (answerIndex != -1) {
                  this.userAnswers[index][scaleIndex] =
                    val[answerIndex].answer - 1;
                } else {
                  this.userAnswers[index][scaleIndex] = 2;
                }
              } else {
                this.userAnswers[index][scaleIndex] = 2;
              }
            }
          }
        }
      }
    },
    userGroupOptionAnswers(val) {
      if (val != undefined) {
        for (let index = 0; index < this.questionsSet.length; index++) {
          const question = this.questionsSet[index];
          if (question.type == this.WITH_OPTION_TYPE) {
            this.userAnswers[index] = null;
            let questionId = question.question.id;
            let answerIndex = val.findIndex(el => {
              return el.questionWithOption.id == questionId;
            });
            if (answerIndex != -1) {
              this.userAnswers[index] = val[answerIndex];
            }
          }
        }
      }
    },
    questionsSet(val) {
      if (val != undefined) this.userAnswers = [];
      for (let index = 0; index < val.length; index++) {
        const question = val[index];
        if (question.type == this.WITH_SCALE_TYPE) {
          this.userAnswers[index] = [];
          for (
            let scaleIndex = 0;
            scaleIndex < question.question.answerscaleSet.length;
            scaleIndex++
          ) {
            const scaleLine = question.question.answerscaleSet[scaleIndex];

            if (this.userGroupScaleAnswers != undefined) {
              let answerIndex = this.userGroupScaleAnswers.findIndex(el => {
                return el.answerScaleLine.id == scaleLine.id;
              });

              if (answerIndex != -1) {
                this.userAnswers[index][scaleIndex] =
                  this.userGroupScaleAnswers[answerIndex].answer - 1;
              } else {
                this.userAnswers[index][scaleIndex] = 2;
              }
            } else {
              this.userAnswers[index][scaleIndex] = 2;
            }
          }
        } else {
          if (this.userGroupOptionAnswers != undefined) {
            let questionId = question.question.id;
            let answerIndex = this.userGroupOptionAnswers.findIndex(el => {
              return el.questionWithOption.id == questionId;
            });
            if (answerIndex != -1) {
              this.userAnswers[index] =
                this.userGroupOptionAnswers[answerIndex].answer.id;
            } else {
              this.userAnswers[index] = null;
            }
          }
        }
      }
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
