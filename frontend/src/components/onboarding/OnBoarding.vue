<template>
  <div>OnBoarding {{ hello }}</div>
</template>

<script>
import { HELLO } from "../../graphql/test_queries";
export default {
  name: "OnBoarding",
  apollo: {
    hell: {
      query: HELLO
    }
  },
  mounted() {
    this.$apollo.queries.hell.refresh();
    this.$apollo.queries.hell.refetch();
    console.log(HELLO);
  }
};
</script>

<style lang="scss" scoped></style>
