<template>
  <v-app>
    <v-app-bar app color="#E2F9FC">
      <v-container class="py-0 fill-height">
        <h2>Логотип</h2>
        <div id="nav">
          <v-btn text :exact="true" to="/">Home</v-btn>
          <v-btn text :exact="true" to="/auth">Auth - LogIn</v-btn>
          <v-btn text :exact="true" to="/auth/signup">Auth - Signup</v-btn>
        </div>
        <v-spacer></v-spacer>
        <v-btn color="success" large>Войти</v-btn>
      </v-container>
    </v-app-bar>
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
