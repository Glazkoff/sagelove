<template>
  <div>
    <div class="must-delete">
      <v-divider></v-divider>
      Test
      <v-btn text :exact="true" to="/test">Test</v-btn>
      <v-btn
        text
        :exact="true"
        :to="{ name: 'TestQuestion', params: { id: 1 } }"
      >
        TestQuestion
      </v-btn>
      <v-btn text :exact="true" :to="{ name: 'TestResult' }">TestResult</v-btn>
      <v-divider></v-divider>
    </div>
    <v-layout align-center="align-center" justify-center="justify-center">
      <router-view></router-view>
    </v-layout>
  </div>
</template>

<script>
export default {
  name: "Test"
};
</script>

<style lang="scss" scoped></style>
