<template>
  <v-flex>
    <div v-if="isStart">
      <h1 class="title text-center mt-5 mb-5">
        Заполните опросник о ваших предпочтениях
      </h1>
      <br />
      <p class="text-center mt-5 mb-5">
        Это всего {{ full_question_count }} вопроса, если Вы остановитесь и
        захотите продолжить чуть позже -<br />просто нажимите кнопку "продолжу
        чуть позже"
      </p>
      <br />
      <div class="text-center">
        <v-btn dark color="colorOfSea" @click="onTestStart"
          >Начать тестирование</v-btn
        >
      </div>
    </div>
    <div v-else-if="isInProgress">
      <h1 class="title text-center mt-5 mb-5">
        Опросник о ваших предпочтениях
      </h1>
      <br />
      <p class="text-center mt-5 mb-5">
        Вы остановились на вопросе {{ last_question }} из
        {{ full_question_count }}
      </p>
      <br />
      <div class="text-center">
        <v-btn dark class="mt-2" color="colorOfSea" @click="onTestContinue"
          >Продолжить</v-btn
        >
        <v-btn dark class="ml-5 mt-2" color="colorOfSea" @click="onTestReset"
          >Пройти заново</v-btn
        >
      </div>
    </div>
  </v-flex>
</template>

<script>
const START_STATUS = "start";
const IN_PROGRESS_STATUS = "in_progress";

export default {
  name: "TestStatus",
  data() {
    return {
      status: START_STATUS,
      last_question: 1,
      full_question_count: 64
    };
  },
  computed: {
    isStart() {
      return this.status == START_STATUS;
    },
    isInProgress() {
      return this.status == IN_PROGRESS_STATUS;
    }
  },
  methods: {
    onTestStart() {
      console.log("onTestStart");
    },
    onTestContinue() {
      console.log("onTestContinue");
    },
    onTestReset() {
      console.log("onTestReset");
    }
  }
};
</script>

<style lang="scss" scoped></style>
