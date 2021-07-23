<template>
  <v-layout class="d-flex justify-center align-center h-100">
    <AppLoader
      v-if="
        this.$apollo.queries.user.loading ||
        this.$apollo.queries.matchForUser.loading
      "
    ></AppLoader>

    <v-flex
      v-if="
        !this.$apollo.queries.user.loading &&
        !this.$apollo.queries.matchForUser.loading
      "
      class="text-center width-window pt-5 pt-sm-10 pb-5 pb-sm-10"
    >
      <h1
        v-if="
          (!isPaid && !wasFound && !wasCongratulated) || (!isPaid && wasFound)
        "
        class="title mb-5 mb-sm-10"
      >
        Поздравляем!
      </h1>
      <h1 v-if="isPaid" class="title mb-5 mb-sm-10">Знакомства</h1>
      <p v-if="!isPaid && !wasFound && !wasCongratulated">
        {{ textResultTest }}
      </p>
      <p v-if="!isPaid && !wasFound && !wasCongratulated">
        Дайте нам немного времени, и, как только наш умный алгоритм просчитает
        совпадение, мы вас проинформируем. Обычно на это уходит не более 6 часов
      </p>

      <v-row
        class="custom-relative"
        v-if="
          !isPaid || (isPaid && personsArr.length == 0) || (isPaid && !wasFound)
        "
      >
        <h2
          v-if="
            (!isPaid && !wasFound) ||
            (isPaid && personsArr.length == 0) ||
            (isPaid && !wasFound)
          "
          z-index="11"
          class="
            title
            darkBlue--text
            text-center
            custom-absolute
            d-flex
            justify-center
            align-center
          "
        >
          Совсем скоро мы найдем для вас интересных людей!
        </h2>
        <div
          z-index="10"
          v-if="!isPaid && wasFound"
          class="custom-absolute d-flex justify-center align-center flex-column"
        >
          <p class="text-center ml-5 mr-5 ml-sm-12 mr-sm-12">
            Мы нашли варианты интересных людей, которые полностью совпадают с
            вашими критериями поиска, если вы хотите с ними познакомиться и
            выбрать с кем будете общаться, внесите клубный взнос в размере 10
            000 рублей.
          </p>
          <v-btn
            color="colorOfSea my-button wide-padding"
            dark
            large
            @click="onPay()"
            >Оплатить</v-btn
          >
        </div>

        <v-col
          v-for="i in 8"
          :key="i"
          class="
            col-12 col-sm-6
            custom-sceleton
            d-flex
            justify-start
            align-start
            flex-row
          "
        >
          <div class="circle"></div>
          <div class="custom-wrap">
            <div class="line line-title"></div>
            <div class="line line-description"></div>
            <div class="line line-description"></div>
          </div>
        </v-col>
      </v-row>

      <!-- Если оплачено, то показываются профили -->
      <v-row v-if="isPaid && wasFound">
        <v-col
          v-for="person in personsArr"
          :key="person.id"
          class="
            col-12 col-sm-6
            custom-sceleton
            d-flex
            justify-center
            align-start
            flex-row
            text-left
          "
        >
          <img
            @click="onRouteToPerson(person.id)"
            class="custom-img pointer"
            src="https://picsum.photos/200"
            alt="Ававтар"
          />
          <div class="custom-wrap user">
            <p class="font-weight-bold mb-1">
              <router-link
                :to="{ name: 'DatingsPerson', params: { id: person.id } }"
                class="link"
                >{{ person.firstName }}</router-link
              >
            </p>
            <p class="mb-1">{{ countAge(person.dateOfBirth) }}</p>
            <v-btn color="colorOfSea my-button" dark large>Написать</v-btn>
          </div>
        </v-col>
      </v-row>
    </v-flex>
  </v-layout>
</template>

<script>
import AppLoader from "@/components/global/AppLoader.vue";

import { USER_AFTER_TEST_STATUS } from "@/graphql/user_queries.js";
import {
  UPDATE_USER_CONGRATULATIONS_STATUS,
  UPDATE_USER_TEST_RESULT_DEMO
} from "@/graphql/user_mutation.js";
import { MATCHES_FOR_USER } from "@/graphql/accounts_queries.js";
export default {
  name: "DatingsStatus",
  components: {
    AppLoader
  },
  apollo: {
    user: {
      query: USER_AFTER_TEST_STATUS,
      variables() {
        return { userId: this.$store.getters.decoded.user_id };
      }
    },
    matchForUser: {
      query: MATCHES_FOR_USER,
      variables() {
        return { userId: this.$store.getters.decoded.user_id };
      }
    }
  },
  watch: {
    user: function (val) {
      if (val.congratulationsAfterTest && !this.wasCongratulatedUpdated) {
        this.wasCongratulated = true;
      } else {
        this.wasCongratulatedUpdated = true;
        this.$apollo
          .mutate({
            mutation: UPDATE_USER_CONGRATULATIONS_STATUS,
            variables: {
              congratulationsAfterTest: true,
              userId: this.$store.getters.decoded.user_id
            }
          })
          .then(() => {})
          .catch(err => {
            console.log(err);
          });
      }
      switch (val.testResultDemo) {
        case "NFNP":
        default:
          this.wasFound = false;
          this.isPaid = false;
          break;
        case "FNP":
          this.wasFound = true;
          this.isPaid = false;
          break;
        case "NFP":
          this.wasFound = false;
          this.isPaid = true;
          break;
        case "FP":
          this.wasFound = true;
          this.isPaid = true;
          break;
      }
    }
    // matchForUser: function (val) {}
  },
  data() {
    return {
      wasCongratulated: false,
      wasCongratulatedUpdated: false,
      isPaid: false,
      wasFound: false,
      textResultTest:
        "Вы смелы и решительны. Вы можете принимать решения в зависимости от ситуации: то завоевать весь мир, то бросить все дела и переключить внимание на что-то очень важное. Вы не боятесь общественного мнения, у Вас есть свое мнение на любой счет."
    };
  },
  computed: {
    personsArr() {
      if (this.matchForUser != undefined || this.matchForUser != null) {
        let arr = [];
        this.matchForUser.forEach(el => {
          if (
            el.user1.id == this.$store.getters.decoded.user_id &&
            el.user2.id != this.$store.getters.decoded.user_id
          )
            arr.push(el.user2);
          if (
            el.user1.id != this.$store.getters.decoded.user_id &&
            el.user2.id == this.$store.getters.decoded.user_id
          )
            arr.push(el.user1);
        });
        return arr;
      } else return [];
    }
  },
  methods: {
    onPay() {
      this.$apollo
        .mutate({
          mutation: UPDATE_USER_TEST_RESULT_DEMO,
          variables: {
            testResultDemo: "FP",
            userId: this.$store.getters.decoded.user_id
          }
        })
        .then(() => {})
        .catch(err => {
          console.log(err);
        });
    },
    onRouteToPerson(id) {
      this.$router.push({ name: "DatingsPerson", params: { id: id } });
    },
    countAge(dateString) {
      var today = new Date();
      var birthDate = new Date(dateString);
      console.log(dateString);
      var age = today.getFullYear() - birthDate.getFullYear();
      var m = today.getMonth() - birthDate.getMonth();
      if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
      }

      return this.yearsOldWord(age);
    },
    yearsOldWord(age) {
      let txt;
      let count;
      count = age % 100;
      if (count >= 5 && count <= 20) {
        txt = "лет";
      } else {
        count = count % 10;
        if (count == 1) {
          txt = "год";
        } else if (count >= 2 && count <= 4) {
          txt = "года";
        } else {
          txt = "лет";
        }
      }
      return `${age} ${txt}`;
    }
  }
};
</script>

<style lang="scss" scoped>
.width-window {
  max-width: 600px;
}

.custom-relative {
  position: relative;
}

.custom-absolute {
  height: 100%;
  position: absolute;
}
.custom-img {
  width: 80px;
  height: 80px;
  margin-right: 1rem;
  border-radius: 50%;
}

.custom-sceleton {
  & .circle {
    width: 80px;
    height: 80px;
    margin-right: 1rem;
    background-color: var(--v-lightLightBlue-base);
    border-radius: 50%;
  }
  & .custom-wrap {
    margin-top: 1rem;
    &.user {
      margin-top: 0 !important;
    }

    & .line {
      width: 5rem;
      height: 0.75rem;
      border-radius: 1rem;
      background-color: var(--v-lightLightBlue-base);
      margin-bottom: 0.5rem;
      &.line-title {
        margin-bottom: 0.75rem;
      }
      &.line-description {
        min-width: 10rem;
      }
    }
  }
}
@media (max-width: 600px) {
  .custom-sceleton {
    width: 100%;
    & .custom-wrap {
      width: calc(100% - 96px);
      &.user {
        width: auto !important;
      }
      & .line {
        width: 80px;
        &.line-description {
          width: 100%;
        }
      }
    }
  }
}
</style>
