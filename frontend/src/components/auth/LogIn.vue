<template>
  <v-flex class="auth-form text-center">
    <h1 class="display-1 mb-3">Авторизация</h1>
    <v-card flat light="light">
      <v-card-text>
        <v-form>
          <v-text-field
            :disabled="formLoading"
            light="light"
            label="Email"
            type="email"
            color="colorOfSea"
            autocomplete="email"
            required
            :error-messages="emailErrors"
            v-model.trim="$v.form.email.$model"
            @input="
              $v.form.email.$touch();
              requestErrors = [];
            "
            @blur="
              $v.form.email.$touch();
              requestErrors = [];
            "
          ></v-text-field>
          <v-text-field
            :disabled="formLoading"
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
            @input="
              $v.form.password.$touch();
              requestErrors = [];
            "
            @blur="
              $v.form.password.$touch();
              requestErrors = [];
            "
          ></v-text-field>
          <v-btn
            class="mt-2"
            color="colorOfSea"
            :dark="!$v.form.$invalid && !formLoading"
            @click.prevent="logIn"
            block="block"
            type="submit"
            :disabled="$v.form.$invalid || formLoading"
            :loading="formLoading"
          >
            Войти
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
    <div class="darkBlue--text">
      Ещё нет аккаунта?
      <v-btn
        class="darkBlueGreen--text"
        text
        to="/auth/signup"
        :disabled="formLoading"
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
      formLoading: false,
      form: {
        email: "",
        password: ""
      },
      requestErrors: []
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
      this.requestErrors.length > 0 &&
        this.requestErrors.forEach(element => {
          errors.push(element);
        });
      return errors;
    },
    passwordErrors() {
      const errors = [];
      if (!this.$v.form.password.$dirty) return errors;
      !this.$v.form.password.required && errors.push("Укажите пароль!");
      this.requestErrors.length > 0 &&
        this.requestErrors.forEach(element => {
          errors.push(element);
        });
      return errors;
    }
  },
  methods: {
    logIn() {
      let sendObj = { ...this.form };
      this.formLoading = true;
      this.$store.dispatch("LOG_IN", sendObj).then(
        () => {
          this.formLoading = false;
        },
        errors => {
          this.formLoading = false;
          if (errors.non_field_errors) {
            for (
              let index = 0;
              index < errors.non_field_errors.length;
              index++
            ) {
              this.requestErrors.push(errors.non_field_errors[index]);
            }
          }
        }
      );
    }
  }
};
</script>

<style lang="scss" scoped></style>
