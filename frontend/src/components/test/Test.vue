<template>
  <div>
    <div class="must-delete">
      <!-- <v-divider></v-divider>
      Test
      <v-btn text :exact="true" to="/test">Test</v-btn>
      <v-btn
        text
        :exact="true"
        class="my-button"
        :to="{ name: 'TestQuestion', params: { id: 1 } }"
      >
        TestQuestion
      </v-btn>
      <v-btn text :exact="true" :to="{ name: 'TestResult' }">TestResult</v-btn>
      <v-divider></v-divider> -->
    </div>
    <v-layout align-center="align-center" justify-center="justify-center">
      <router-view></router-view>
    </v-layout>
  </div>
</template>

<script>
import { USER_TEST_STATUS } from "../../graphql/user_queries.js";

export default {
  name: "Test",
  apollo: {
    user: {
      query: USER_TEST_STATUS,
      variables() {
        return { userId: this.$store.getters.decoded.user_id };
      }
    }
  },
  watch: {
    user: function (val) {
      let route = "";
      switch (val.testStatus) {
        case "START":
        case "INPROGRESS":
        default:
          route = "/test";
          break;
        case "FINISH":
          route = "/result";
          break;
      }
      if (
        this.$route.path != route &&
        this.$route.path.substring(0, this.$route.path.length - 1) != route
      ) {
        this.$router.push(route);
      }
    }
  }
};
</script>

<style lang="scss" scoped></style>
