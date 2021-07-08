<template>
  <v-flex>
    <h1 class="title mb-12 text-center">Выберите цель</h1>
    <div class="d-flex justify-center">
      <div>
        <v-radio-group v-model="radios" class="dark-blue-text">
          <label class="pb-4">1. Я ищу партнёра:</label>
          <v-radio value="guestMarriage">
            <template v-slot:label>
              <div class="dark-blue-text">для гостевого брака</div>
            </template>
          </v-radio>
          <v-radio value="family">
            <template v-slot:label>
              <div class="dark-blue-text">для создания семьи</div>
            </template>
          </v-radio>
          <v-radio value="justForFun">
            <template v-slot:label>
              <div class="dark-blue-text">
                для просто поболтать и вместе потусить
              </div>
            </template>
          </v-radio>
        </v-radio-group>
        <v-radio-group v-model="radios" class="dark-blue-text">
          <label class="pb-4">2. Я хочу встретить:</label>
          <v-radio value="same">
            <template v-slot:label>
              <div class="dark-blue-text">такого, как я</div>
            </template>
          </v-radio>
          <v-radio value="another">
            <template v-slot:label>
              <div class="dark-blue-text">мою противоположность</div>
            </template>
          </v-radio>
          <v-radio value="mathematic">
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
              :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
              :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
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
          class="mt-8 my-button"
          color="colorOfSea"
          block="block"
          type="submit"
          to="/test"
        >
          Дальше
        </v-btn>
      </div>
    </div>
  </v-flex>
</template>

<script>
export default {
  name: "Aims",
  data() {
    return {
      isBlueBorder: undefined
    };
  }
};
</script>

<style lang="scss" scoped>
.dark-blue-text {
  color: var(--v-darkBlue-base) !important;
}

.blueborder {
  border: 3px solid #00acc2 !important;
}
.v-application .grey.lighten-2 {
  background-color: #00acc2 !important;
  border-color: #00acc2 !important;
}
.col {
  padding: 0.5rem !important;
}
</style>
