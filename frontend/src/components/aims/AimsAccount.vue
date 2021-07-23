<template>
  <v-layout>
    <AppLoader v-if="this.$apollo.queries.user.loading"></AppLoader>
    <v-flex v-if="!this.$apollo.queries.user.loading">
      <h1 class="title mb-12 text-center mb-5 mt-5 mb-sm-10 mt-sm-10">Цели</h1>
      <div v-if="!isEdit" class="d-flex justify-center">
        <div class="background-aimsaccount rounded-lg pa-8">
          <v-row class="direction-block">
            <v-col class="mobile-padding"
              ><p class="dark-blue-text">Я ищу партнера:</p></v-col
            >
            <v-col class="mobile-padding1">
              <p v-if="user.partnerType == 'GM'" class="gray-text">
                для гостевого брака
              </p>
              <p v-if="user.partnerType == 'FAM'" class="gray-text">
                для создания семьи
              </p>
              <p v-if="user.partnerType == 'JFF'" class="gray-text">
                для просто поболтать и вместе потусить
              </p></v-col
            >
          </v-row>
          <v-row class="direction-block">
            <v-col class="mobile-padding"
              ><p class="dark-blue-text">Я хочу встретить:</p></v-col
            >
            <v-col class="mobile-padding1">
              <p v-if="user.purposeMeet == 'SAME'" class="gray-text">
                такого, как я
              </p>
              <p v-if="user.purposeMeet == 'ANTI'" class="gray-text">
                мою противоположность
              </p>
              <p v-if="user.purposeMeet == 'MATH'" class="gray-text">
                выбор путем математического алгоритма
              </p></v-col
            >
          </v-row>
          <v-row class="direction-block">
            <v-col class="mobile-padding"
              ><p class="dark-blue-text">Моя история по ощущениям:</p></v-col
            >
            <v-col class="mobile-padding1"
              ><img
                :src="
                  require('../../assets/img/history/' +
                    user.numberFotoHistoryByFelling +
                    '.jpg')
                "
                alt="history"
                class="width-img-history"
            /></v-col>
          </v-row>
          <v-btn
            class="mt-8 my-button white--text"
            color="colorOfSea"
            block="block"
            type="submit"
            @click="onEdit()"
          >
            Изменить
          </v-btn>
        </div>
      </div>
      <div v-if="isEdit" class="d-flex justify-center">
        <div class="background-aimsaccount rounded-lg pa-8">
          <v-row class="direction-block">
            <v-col class="mobile-padding"
              ><p class="dark-blue-text">Я ищу партнера:</p></v-col
            >
            <v-col>
              <v-radio-group v-model="partner" class="dark-blue-text">
                <v-radio value="GM">
                  <template v-slot:label>
                    <div class="dark-blue-text">
                      для гостевого брака
                    </div></template
                  >
                </v-radio>
                <v-radio value="FAM">
                  <template v-slot:label>
                    <div class="dark-blue-text">
                      для создания семьи
                    </div></template
                  >
                </v-radio>
                <v-radio value="JFF">
                  <template v-slot:label
                    ><div class="dark-blue-text">
                      для просто поболтать и вместе потусить
                    </div></template
                  >
                </v-radio>
              </v-radio-group></v-col
            >
          </v-row>
          <v-row class="direction-block">
            <v-col class="mobile-padding"
              ><p class="dark-blue-text">Я хочу встретить:</p></v-col
            >
            <v-col
              ><v-radio-group v-model="wish" class="dark-blue-text">
                <v-radio value="SAME">
                  <template v-slot:label>
                    <div class="dark-blue-text">такого, как я</div></template
                  >
                </v-radio>
                <v-radio value="ANTI">
                  <template v-slot:label>
                    <div class="dark-blue-text">
                      мою противоположность
                    </div></template
                  >
                </v-radio>
                <v-radio value="MATH">
                  <template v-slot:label>
                    <div class="dark-blue-text">
                      выбор путем математического алгоритма
                    </div></template
                  >
                </v-radio>
              </v-radio-group></v-col
            >
          </v-row>
          <v-row class="direction-block">
            <v-col class="mobile-padding"
              ><p class="dark-blue-text">Моя история по ощущениям:</p></v-col
            >
            <v-col
              ><v-row>
                <v-col
                  v-for="n in 9"
                  :key="n"
                  class="d-flex child-flex col-history hover-eye"
                  cols="4"
                >
                  <v-img
                    :src="require('../../assets/img/history/' + n + '.jpg')"
                    aspect-ratio="1"
                    class="grey lighten-2"
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
                  </v-img>
                </v-col>
                <v-dialog v-model="dialog">
                  <v-card>
                    <img
                      :src="
                        require('../../assets/img/history/' +
                          isNumberFoto +
                          '.jpg')
                      "
                      alt="history"
                      class="width-dialog-image"
                    />
                  </v-card>
                </v-dialog> </v-row
            ></v-col>
          </v-row>
          <v-btn
            class="mt-8 my-button white--text"
            color="colorOfSea"
            block="block"
            type="submit"
            @click="onUpdateAims(isBlueBorder, wish, partner)"
          >
            Сохранить
          </v-btn>
        </div>
      </div>
    </v-flex></v-layout
  >
</template>

<script>
import AppLoader from "@/components/global/AppLoader.vue";
import { USER_AIMS } from "@/graphql/user_queries";
import { UPDATE_USER_AIMS } from "@/graphql/user_mutations";
export default {
  name: "AimsAccount",
  components: { AppLoader },
  apollo: {
    user: {
      query: USER_AIMS,
      variables() {
        return { userId: this.$store.getters.decoded.user_id };
      }
    }
  },
  data() {
    return {
      isEdit: false,
      isBlueBorder: undefined,
      partner: null,
      wish: null,
      dialog: false,
      isNumberFoto: 1
    };
  },
  methods: {
    onEdit() {
      if (!this.isEdit) {
        this.isEdit = true;
        this.isBlueBorder = this.user.numberFotoHistoryByFelling;
        this.partner = this.user.partnerType;
        this.wish = this.user.purposeMeet;
      } else {
        this.isEdit = false;
      }
    },
    onUpdateAims(n, wish, partner) {
      this.$apollo
        .mutate({
          mutation: UPDATE_USER_AIMS,
          variables: {
            partnerType: partner,
            purposeMeet: wish,
            numberFotoHistoryByFelling: n,
            userId: this.$store.getters.decoded.user_id
          },
          update: (cache, { data: { updateAimsForUser } }) => {
            console.log("updateAimsForUser ", updateAimsForUser);
            let data = cache.readQuery({
              query: USER_AIMS,
              variables: {
                userId: this.$store.getters.decoded.user_id
              }
            });
            data.user.partnerType = this.partner;
            data.user.purposeMeet = this.wish;
            data.user.numberFotoHistoryByFelling = this.isBlueBorder;
            cache.writeQuery({ query: USER_AIMS, data });
          },
          optimisticResponse: {
            __typename: "Mutation",
            updateAimsForUser: {
              __typename: "UpdateAimsForUserMutation",
              partnerType: this.partner,
              purposeMeet: this.wish,
              numberFotoHistoryByFelling: this.isBlueBorder
            }
          }
        })
        .then(() => {})
        .catch(err => {
          console.log(err);
        });
      this.isEdit = false;
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
.gray-text {
  color: rgba(148, 148, 148, 1) !important;
}
.background-aimsaccount {
  background-color: #e2f9fc !important;
  filter: drop-shadow(0 0 4px rgba(0, 0, 0, 0.25));
}
.width-img-history {
  width: 100%;
}
.blueborder {
  border: 3px solid #00acc2 !important;
}
.v-application .grey.lighten-2 {
  background-color: #00acc2 !important;
  border-color: #00acc2 !important;
}
.col .col-history {
  padding: 0.5rem !important;
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
.width-dialog-image {
  max-height: 35rem !important;
  max-width: 35rem !important;
}
@media (max-width: 600px) {
  .direction-block {
    flex-direction: column !important;
  }
  p {
    margin-bottom: 0px !important;
  }
  .mobile-padding {
    padding-top: 0;
    padding-bottom: 0;
  }
  .mobile-padding1 {
    padding-top: 0.1rem;
  }
  .col .col-history {
    padding-top: 0.1rem !important;
  }
}
@media (max-width: 500px) {
  .direction-block {
    flex-direction: column !important;
  }
}
</style>
