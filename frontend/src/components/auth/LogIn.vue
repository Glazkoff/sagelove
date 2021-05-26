<template>
  <v-flex class="auth-form text-center">
    <div class="display-1 mb-3">
      <v-icon class="mr-2" large="large">mdi-cards-heart</v-icon> Амурчики
    </div>
    <v-card light="light">
      <v-card-text>
        <v-form>
          <v-text-field
            light="light"
            prepend-icon="mdi-email"
            label="Email"
            type="email"
          ></v-text-field>
          <v-text-field
            light="light"
            prepend-icon="mdi-lock"
            label="Пароль"
            type="password"
          ></v-text-field>
          <v-checkbox
            light="light"
            label="Запомните меня"
            hide-details="hide-details"
          ></v-checkbox>
          <v-btn
            class="mt-2"
            color="purple"
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
