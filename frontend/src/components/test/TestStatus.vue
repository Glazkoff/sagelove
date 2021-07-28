<template>
  <v-flex>
    <div v-if="isStart">
      <h1 class="title text-center mt-5 mb-5">
        Заполните опросник о ваших предпочтениях
      </h1>
      <br />
      <p class="text-center mt-5 mb-5">
        Это всего {{ questionGroupsCount }} групп вопросов, если Вы остановитесь
        и захотите продолжить чуть позже -<br />просто нажимите кнопку "продолжу
        чуть позже"
      </p>
      <br />
      <div class="text-center">
        <v-btn dark color="colorOfSea" class="my-button" @click="onTestStart">
          Начать тестирование
        </v-btn>
      </div>
    </div>
    <div v-else-if="isInProgress">
      <h1 class="title text-center mt-5 mb-5">
        Опросник о ваших предпочтениях
      </h1>
      <br />
      <p class="text-center mt-5 mb-5">
        Вы остановились на группе вопросов
        {{ userLastGroup != undefined ? userLastGroup.orderNumber : "-" }} из
        {{ questionGroupsCount }}
      </p>
      <br />
      <div class="text-center">
        <v-btn
          dark
          class="mt-2 my-button"
          color="colorOfSea"
          @click="onTestContinue"
          >Продолжить</v-btn
        >
        <v-btn
          dark
          class="ml-5 mt-2 my-button"
          color="colorOfSea"
          @click="onTestReset"
          >Пройти заново</v-btn
        >
      </div>
    </div>
  </v-flex>
</template>

<script>
import { USER_TEST_STATUS } from "@/graphql/user_queries";
import { UPDATE_USER_TEST_STATUS } from "@/graphql/user_mutations";
import {
  QUESTION_GROUP_COUNT,
  USER_LAST_GROUP
} from "@/graphql/questions_queries";
const START_STATUS = "START";
const IN_PROGRESS_STATUS = "INPROGRESS";

export default {
  name: "TestStatus",
  apollo: {
    user: {
      query: USER_TEST_STATUS,
      variables() {
        return { userId: this.$store.getters.user_id };
      }
    },
    questionGroupsCount: {
      query: QUESTION_GROUP_COUNT
    },
    userLastGroup: {
      query: USER_LAST_GROUP,
      variables() {
        return { userId: this.$store.getters.user_id };
      }
    }
  },
  data() {
    return {
      status: START_STATUS,
      last_question_group: 1
    };
  },
  watch: {
    user: function () {
      switch (this.user.testStatus) {
        case "INPROGRESS":
          this.status = IN_PROGRESS_STATUS;
          break;
        case "START":
        default:
          this.status = START_STATUS;
          break;
      }
    }
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
      this.$apollo
        .mutate({
          mutation: UPDATE_USER_TEST_STATUS,
          variables: {
            testStatus: "inprogress",
            userId: this.$store.getters.user_id
          }
        })
        .then(() => {
          // TODO: find last question group
          let last = `/question/${this.userLastGroup.id}`;
          this.$router.push(last);
        })
        .catch(err => {
          console.log(err);
        });
    },
    onTestContinue() {
      // TODO: найти последний вопрос
      this.$router.push(`/question/${this.userLastGroup.id}`);
    },
    onTestReset() {
      this.$apollo
        .mutate({
          mutation: UPDATE_USER_TEST_STATUS,
          variables: {
            testStatus: "start",
            userId: this.$store.getters.user_id
          }
        })
        .then(() => {
          this.$apollo.queries.user.refetch();
          this.$apollo.queries.user.refresh();
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>

<style lang="scss" scoped></style>
