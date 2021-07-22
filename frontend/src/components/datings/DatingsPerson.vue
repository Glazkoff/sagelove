<template>
  <v-layout>
    <v-flex>
      <h1 class="title mb-5 mt-5 mb-sm-10 mt-sm-10 text-center">Знакомства</h1>
      <v-row>
        <v-col>
          <p>
            <router-link :to="{ name: 'DatingsStatus' }" class="link"
              >Знакомства</router-link
            >
            <span class="grey--text mr-3 ml-3">/</span>
            <span class="grey--text">Иван</span>
          </p>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="col-12 col-sm-3">
          <img class="custom-img" src="https://picsum.photos/200" alt="Аватар"
        /></v-col>
        <v-col class="col-12 col-sm-9">
          <div class="custom-card pa-4 pa-sm-8">
            <div class="custom-relative">
              <a
                class="link custom-absolute d-flex justify-end align-center"
                @click="dialog = true"
                >Заблокировать</a
              >
              <h2 class="title darkBlue--text mb-5">{{ person.user_name }}</h2>
            </div>
            <v-row>
              <v-col class="col-4">
                <p class="mb-0">Дата рождения:</p>
              </v-col>
              <v-col class="col-8">
                <p class="mb-0">{{ formatDate(person.user_birthday) }}</p>
              </v-col>
              <v-col class="col-4">
                <p class="mb-0">О себе:</p>
              </v-col>
              <v-col class="col-8">
                <p class="mb-0">
                  {{ person.personal_information }}
                </p>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-btn
                  color="colorOfSea"
                  class="my-button wide-padding white--text"
                  large
                  >Написать</v-btn
                >
              </v-col>
            </v-row>
          </div>
        </v-col>
      </v-row>
    </v-flex>

    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-title class="lightBlue pa-4 pr-12 custom-relative">
          <h4>Заблокировать пользователя</h4>
          <v-icon
            @click="dialog = false"
            color="#013351"
            class="custom-absolute d-flex justify-end cross"
            >mdi-close</v-icon
          >
        </v-card-title>

        <v-card-text class="pa-4">
          <p class="mb-0">
            Вы уверены, что хотите заблокировать пользователя
            {{ person.user_name }}?
          </p>
        </v-card-text>

        <v-card-actions class="pb-4">
          <v-btn
            color="colorOfSea"
            class="my-button wide-padding white--text"
            large
            @click="dialog = false"
            :to="{ name: 'DatingsStatus' }"
            >Заблокировать</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
export default {
  name: "DatingsPerson",
  data() {
    return {
      dialog: false,
      person: {
        id: 1,
        user_name: "Иван",
        user_birthday: "1987-06-15",
        url_foto: "",
        personal_information:
          "Текст о себе, текст о себе. Текст о себе, текст о себе.Текст о себе, текст о себе."
      }
    };
  },
  methods: {
    formatDate(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      return `${day}.${month}.${year}`;
    }
  }
};
</script>

<style lang="scss" scoped>
.v-card__title {
  width: 100%;
}

.custom-relative {
  position: relative;
}

.custom-absolute {
  width: 100%;
  height: 100%;
  position: absolute !important;
  &.cross {
    width: auto;
    right: 16px;
  }
}

.custom-img {
  width: 100%;
  height: auto;
  margin-right: 1rem;
  border-radius: 50%;
}

.custom-card {
  background: var(--v-lightLightBlue-base);
  min-height: 10rem;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}
</style>
