<template>
  <v-app>
    <v-app-bar app color="lightBlue">
      <v-container class="py-0 fill-height">
        <div class="d-flex justify-center justify-sm-start custom-flex-width">
          <img
            src="../assets/img/logo.svg"
            alt="Logo"
            class="py-0 width-logo"
          />
        </div>

        <v-spacer></v-spacer>
        <v-btn
          color="colorOfSea"
          class="colorOfSea my-button wide-padding white--text custom-full-width d-none d-sm-flex"
          dark
          large
          to="/login"
          >Войти</v-btn
        >
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
  name: "Auth",
  methods: {
    // routerToHome() {
    //   if (this.$route.path != "/") {
    //     this.$router.push({ path: "/" });
    //   }
    // }
  }
};
</script>

<style lang="scss" scoped>
.auth-form {
  max-width: 500px;
}
.width-logo {
  width: 10rem;
}

@media (max-width: 370px) {
  .custom-flex-width {
    width: 100%;
  }
}
</style>
