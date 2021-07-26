<template>
  <div>
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
        return { userId: this.$store.getters.user_id };
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
