<template>
  <v-app>
    <v-app-bar app color="#C8F5FA">
      <v-container class="py-0 fill-height">
        <h2 class="darkBlueGreen--text title logo">Логотип</h2>
        <!-- <div id="nav">
          <v-btn text :exact="true" to="/">Home</v-btn>
          <v-btn text :exact="true" to="/auth">Auth - LogIn</v-btn>
          <v-btn text :exact="true" to="/auth/signup">Auth - Signup</v-btn>
        </div> -->
        <v-spacer></v-spacer>
        <v-btn color="colorOfSea" dark large to="/auth">Войти</v-btn>
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

h2.logo {
  font-style: normal;
  font-weight: 400;
  font-size: 28px !important;
  line-height: 36px;
}

</style>
