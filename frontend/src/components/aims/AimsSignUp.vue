<template>
  <v-flex>
    <h1 class="title mb-12 text-center mb-5 mt-5 mb-sm-10 mt-sm-10">
      Выберите цель
    </h1>
    <div class="d-flex justify-center">
      <div>
        <v-radio-group v-model="partner" class="dark-blue-text">
          <label class="pb-4">1. Я ищу партнёра:</label>
          <v-radio value="GM">
            <template v-slot:label>
              <div class="dark-blue-text">для гостевого брака</div>
            </template>
          </v-radio>
          <v-radio value="FAM">
            <template v-slot:label>
              <div class="dark-blue-text">для создания семьи</div>
            </template>
          </v-radio>
          <v-radio value="JFF">
            <template v-slot:label>
              <div class="dark-blue-text">
                для просто поболтать и вместе потусить
              </div>
            </template>
          </v-radio>
        </v-radio-group>
        <v-radio-group v-model="wish" class="dark-blue-text">
          <label class="pb-4">2. Я хочу встретить:</label>
          <v-radio value="SAME">
            <template v-slot:label>
              <div class="dark-blue-text">такого, как я</div>
            </template>
          </v-radio>
          <v-radio value="ANTI">
            <template v-slot:label>
              <div class="dark-blue-text">мою противоположность</div>
            </template>
          </v-radio>
          <v-radio value="MATH">
            <template v-slot:label>
              <div class="dark-blue-text">
                выбор путем математического алгоритма
              </div>
            </template>
          </v-radio>
        </v-radio-group>

        <p class="dark-blue-text">3. Выберите свою историю по ощущениям:</p>
        <v-row>
          <v-col v-for="n in 9" :key="n" class="d-flex child-flex" cols="4">
            <v-img
              :src="require('../../assets/img/history/' + n + '.jpg')"
              aspect-ratio="1"
              class="grey lighten-2"
              :class="{ blueborder: n == isBlueBorder }"
              @click="isBlueBorder = n"
            >
              <template v-slot:placeholder>
                <v-row class="fill-height ma-0" align="center" justify="center">
                  <v-progress-circular
                    indeterminate
                    color="grey lighten-5"
                  ></v-progress-circular>
                </v-row>
              </template>
            </v-img>
          </v-col>
        </v-row>
        <v-btn
          class="mt-8 my-button white--text"
          color="colorOfSea"
          block="block"
          type="submit"
          @click="onUpdateAims(isBlueBorder, wish, partner)"
        >
          Дальше
        </v-btn>
      </div>
    </div>
  </v-flex>
</template>

<script>
import { UPDATE_USER_AIMS } from "@/graphql/user_queries";
export default {
  name: "AimsSignUp",
  data() {
    return {
      isBlueBorder: undefined,
      partner: null,
      wish: null
    };
  },
  methods: {
    onUpdateAims(n, wish, partner) {
      this.$apollo
        .mutate({
          mutation: UPDATE_USER_AIMS,
          variables: {
            partnerType: partner,
            purposeMeet: wish,
            numberFotoHistoryByFelling: n,
            userId: this.$store.getters.decoded.user_id
          }
        })
        .then(() => {})
        .catch(err => {
          console.log(err);
        });
      this.$router.push({ name: "Test" });
    }
  }
};
</script>

<style lang="scss" scoped>
.dark-blue-text {
  color: var(--v-darkBlue-base) !important;
}

.blueborder {
  outline: 4px solid #00acc2 !important;
}
.v-application .grey.lighten-2 {
  background-color: #00acc2 !important;
  outline-color: #00acc2 !important;
}
.col {
  padding: 0.5rem !important;
}
</style>
