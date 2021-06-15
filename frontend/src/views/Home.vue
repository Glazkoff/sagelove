<template>
  <v-app>
    <v-app-bar app color="#C8F5FA">
      <v-container class="py-0 fill-height">
        <h2 class="darkBlueGreen--text title logo">Логотип</h2>
        <v-spacer></v-spacer>
      </v-container>
    </v-app-bar>
    <v-main>
      <v-container fill-height="fill-height">
        <v-layout align-center="align-center" justify-center="justify-center">
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
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  components: {},
  methods: {
    logOut() {
      this.$store.dispatch("LOG_OUT").then(
        () => {
          this.$router.push("/auth");
          console.log("!!!");
        },
        err => {
          console.log(err);
        }
      );
    }
  }
};
</script>
