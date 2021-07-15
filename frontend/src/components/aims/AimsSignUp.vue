<template>
  <v-layout>
    <AppLoader v-if="this.$apollo.queries.loading"></AppLoader>
    <v-flex v-if="!this.$apollo.queries.loading">
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
          <v-row class="history-felling">
            <v-col
              v-for="n in 9"
              :key="n"
              class="d-flex child-flex hover-eye"
              cols="4"
            >
              <v-img
                :src="require('../../assets/img/history/' + n + '.jpg')"
                aspect-ratio="1"
                class="grey lighten-2 hover-image"
                :class="{ blueborder: n == isBlueBorder }"
                @click="isBlueBorder = n"
              >
                <template v-slot:placeholder>
                  <v-row
                    class="fill-height ma-0"
                    align="center"
                    justify="center"
                  >
                    <v-progress-circular
                      indeterminate
                      color="grey lighten-5"
                    ></v-progress-circular>
                  </v-row>
                </template>
              </v-img>
              <v-btn
                color="colorOfSea"
                class="btn-dialog"
                @click="openDialog(n)"
                fab
                x-small
                dark
              >
                <v-icon>mdi-eye</v-icon>
              </v-btn>
            </v-col>
            <v-dialog v-model="dialog">
              <v-card>
                <img
                  :src="
                    require('../../assets/img/history/' + isNumberFoto + '.jpg')
                  "
                  alt="history"
                  class="width-dialog-image"
                />
              </v-card>
            </v-dialog>
          </v-row>
          <v-btn
            class="mt-8 my-button white--text"
            color="colorOfSea"
            block="block"
            type="submit"
            :disabled="
              isBlueBorder == undefined || partner == null || wish == null
            "
            @click="onUpdateAims(isBlueBorder, wish, partner)"
          >
            Дальше
          </v-btn>
        </div>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
import AppLoader from "@/components/global/AppLoader.vue";
import { UPDATE_USER_AIMS } from "@/graphql/user_queries";
export default {
  name: "AimsSignUp",
  components: { AppLoader },
  data() {
    return {
      isBlueBorder: undefined,
      partner: null,
      wish: null,
      dialog: false,
      isNumberFoto: 1
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
    },
    openDialog(n) {
      this.dialog = true;
      this.isNumberFoto = n;
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
  position: relative !important;
}
.btn-dialog {
  margin: 0 auto;
  opacity: 0 !important;
  position: absolute !important;
  transition: opacity 0.3s !important;
  left: 50% !important;
  top: 50% !important;
  transform: translate(-50%, -50%) !important;
}

.hover-eye:hover .btn-dialog {
  opacity: 1 !important;
  transition: opacity 0.3s !important;
}
.hover-eye:hover .hover-image {
  filter: blur(1px);
  transition: filter 0.3s !important;
}
.width-dialog-image {
  max-height: 35rem !important;
  max-width: 35rem !important;
}
</style>
