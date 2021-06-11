<template>
  <v-flex class="auth-form text-center">
    <h1 class="display-1 mb-3">Авторизация</h1>
    <v-card light="light">
      <v-card-text>
        <v-form>
          <v-text-field
            light="light"
            prepend-icon="mdi-email"
            label="Email"
            type="email"
            autocomplete="email"
          ></v-text-field>
          <v-text-field
            light="light"
            prepend-icon="mdi-lock"
            label="Пароль"
            type="password"
            autocomplete="current-password"
          ></v-text-field>
          <v-checkbox
            light="light"
            label="Запомните меня"
            hide-details="hide-details"
          ></v-checkbox>
          <v-btn
            class="mt-2"
            color="pink"
            dark
            @click.prevent
            block="block"
            type="submit"
            >Войти</v-btn
          >
        </v-form>
      </v-card-text>
    </v-card>
    <div>
      Ещё нет аккаунта?
      <v-btn light="light" to="/auth/signup" plain>Зарегистрируйтесь!</v-btn>
    </div>
  </v-flex>
</template>

<script>
export default {
  name: "LogIn"
};
</script>

<style lang="scss" scoped></style>
