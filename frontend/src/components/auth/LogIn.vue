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
            required
            :error-messages="emailErrors"
            v-model.trim="$v.form.email.$model"
            @input="$v.form.email.$touch()"
            @blur="$v.form.email.$touch()"
          ></v-text-field>
          <v-text-field
            light="light"
            label="Пароль"
            :type="passShow ? 'text' : 'password'"
            color="colorOfSea"
            :append-icon="passShow ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="passShow = !passShow"
            autocomplete="current-password"
            required
            :error-messages="passwordErrors"
            v-model.trim="$v.form.password.$model"
            @input="$v.form.password.$touch()"
            @blur="$v.form.password.$touch()"
          ></v-text-field>
          <v-btn
            class="mt-2"
            color="colorOfSea"
            :dark="!$v.form.$invalid"
            @click.prevent
            block="block"
            type="submit"
            :disabled="$v.form.$invalid"
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
import { required, email } from "vuelidate/lib/validators";
export default {
  name: "LogIn",
  data() {
    return {
      passShow: false,
      form: {
        email: "",
        password: ""
      }
    };
  },
  validations: {
    form: {
      email: {
        required,
        email
      },
      password: {
        required
      }
    }
  },
  computed: {
    emailErrors() {
      const errors = [];
      if (!this.$v.form.email.$dirty) return errors;
      !this.$v.form.email.email && errors.push("Введите корректный e-mail");
      !this.$v.form.email.required && errors.push("Укажите ваш e-mail");
      return errors;
    },
    passwordErrors() {
      const errors = [];
      if (!this.$v.form.password.$dirty) return errors;
      !this.$v.form.password.required && errors.push("Укажите пароль!");
      return errors;
    }
  }
};
</script>

<style lang="scss" scoped></style>
