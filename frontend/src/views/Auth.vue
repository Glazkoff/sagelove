<template>
  <v-app>
    <v-main>
      <v-container fill-height="fill-height">
        <v-layout align-center="align-center" justify-center="justify-center">
          <router-view></router-view>
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "Auth"
};
</script>

<style lang="scss" scoped>
.auth-form {
  max-width: 500px;
}
</style>
