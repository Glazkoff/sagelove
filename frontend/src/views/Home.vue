<template>
  <v-app>
    <v-app-bar app color="lightBlue">
      <v-container class="py-0 fill-height">
        <img src="../assets/img/logo.svg" alt="Logo" width="15%" class="py-0" />
        <div id="nav">
          <v-btn text :exact="true" to="/test">Test</v-btn>
        </div>
        <v-spacer></v-spacer>
      </v-container>
    </v-app-bar>
    <v-main>
      <v-container>
        <router-view></router-view>
        <!-- <v-layout align-center="align-center" justify-center="justify-center">
          <v-flex class="text-center">
            <h1>Вы авторизованы!</h1>
            <v-btn
              text
              color="darkBlue"
              class="mt-3 darkBlue--text"
              @click="logOut"
              >Выйти
            </v-btn>
          </v-flex>
        </v-layout> -->
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  methods: {
    logOut() {
      this.$store.dispatch("LOG_OUT").then(
        () => {
          this.$router.push("/login");
        },
        err => {
          console.log(err);
        }
      );
    }
  }
};
</script>
