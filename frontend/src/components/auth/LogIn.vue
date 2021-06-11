<template>
  <v-flex class="auth-form text-center">
    <h1 class="display-1 mb-3">Авторизация</h1>
    <v-card flat light="light">
      <v-card-text>
        <v-form>
          <v-text-field
            light="light"
            label="Email"
            type="email"
            color="colorOfSea"
            autocomplete="email"
            v-model="email"
          ></v-text-field>
          <v-text-field
            light="light"
            label="Пароль"
            :type="passShow ? 'text' : 'password'"
            color="colorOfSea"
            :append-icon="passShow ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="passShow = !passShow"
            autocomplete="current-password"
            v-model="password"
          ></v-text-field>

          <v-btn
            class="mt-2"
            color="colorOfSea"
            dark
            @click.prevent
            block="block"
            type="submit"
            >Войти</v-btn
          >
        </v-form>
      </v-card-text>
    </v-card>
    <div class="darkBlue--text">
      Ещё нет аккаунта?
      <v-btn class="darkBlueGreen--text" text to="/auth/signup"
        >Зарегистрируйтесь!</v-btn
      >
    </div>
  </v-flex>
</template>

<script>
export default {
  name: "LogIn",
  data() {
    return {
      passShow: false,
      email: "",
      password: ""
    };
  }
};
</script>

<style lang="scss" scoped></style>
