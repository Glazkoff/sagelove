<template>
  <v-flex class="auth-form text-center">
    <h1 class="mb-3">Регистрация</h1>
    <v-card flat light="light">
      <v-card-text>
        <v-form>
          <v-text-field
            light="light"
            label="Имя"
            type="text"
            color="colorOfSea"
            autocomplete="name"
            v-model.trim="$v.form.name.$model"
            required
            :error-messages="nameErrors"
            @input="$v.form.name.$touch()"
            @blur="$v.form.name.$touch()"
            :disabled="formLoading"
          ></v-text-field>
          <v-select
            :items="[
              { text: 'Мужской', val: 'м' },
              { text: 'Женский', val: 'ж' }
            ]"
            autocomplete="sex"
            item-text="text"
            item-value="val"
            label="Пол"
            color="colorOfSea"
            required
            :error-messages="sexErrors"
            v-model.trim="$v.form.sex.$model"
            @input="$v.form.sex.$touch()"
            @blur="$v.form.sex.$touch()"
            :disabled="formLoading"
          ></v-select>
          <DatePicker
            label="Дата рождения"
            autocomplete="birthday"
            @update="form.birthday = $event"
            :disabled="formLoading"
          ></DatePicker>
          <v-text-field
            light="light"
            label="Телефон"
            type="text"
            color="colorOfSea"
            autocomplete="phone"
            v-mask="'+7 (###) ###-##-##'"
            required
            :error-messages="phoneErrors"
            v-model.trim="$v.form.phone.$model"
            @input="$v.form.phone.$touch()"
            @blur="$v.form.phone.$touch()"
            :disabled="formLoading"
          ></v-text-field>
          <v-text-field
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
              formEmailErrors = [];
            "
            @blur="
              $v.form.email.$touch();
              formEmailErrors = [];
            "
            :disabled="formLoading"
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
            @input="
              $v.form.password.$touch();
              formPasswordErrors = [];
            "
            @blur="
              $v.form.password.$touch();
              formPasswordErrors = [];
            "
            counter
            :disabled="formLoading"
          ></v-text-field>
          <v-file-input
            :disabled="formLoading"
            truncate-length="15"
            label="Ваша фотография"
            color="colorOfSea"
          ></v-file-input>
          <v-textarea
            :disabled="formLoading"
            label="О себе"
            color="colorOfSea"
            counter
            maxlength="200"
            required
            :error-messages="aboutMeErrors"
            v-model.trim="$v.form.aboutMe.$model"
            @input="$v.form.aboutMe.$touch()"
            @blur="$v.form.aboutMe.$touch()"
          ></v-textarea>
          <v-btn
            class="mt-2"
            color="colorOfSea"
            :dark="!$v.form.$invalid && !formLoading"
            @click.prevent="signUp"
            block="block"
            type="submit"
            :disabled="$v.form.$invalid || formLoading"
            :loading="formLoading"
            >Зарегистрироваться</v-btn
          >
        </v-form>
      </v-card-text>
    </v-card>
    <div class="darkBlue--text">
      Уже есть аккаунт?
      <v-btn class="darkBlueGreen--text" text :exact="true" to="/auth"
        >Войдите!</v-btn
      >
    </div>
  </v-flex>
</template>

<script>
import DatePicker from "@/components/global/DatePicker";
import {
  required,
  minLength,
  maxLength,
  email
} from "vuelidate/lib/validators";

export default {
  name: "SignUp",
  validations: {
    form: {
      name: {
        required
      },
      sex: {
        required
      },
      phone: {
        required,
        minLength: minLength(18),
        maxLength: maxLength(18)
      },
      email: {
        required,
        email
      },
      password: {
        required,
        minLength: minLength(8)
      },
      birthday: {
        required
      },

      aboutMe: {
        required
      }
    }
  },
  components: {
    DatePicker
  },
  data() {
    return {
      passShow: false,
      dateMenu: false,
      formLoading: false,
      formEmailErrors: [],
      formPasswordErrors: [],
      form: {
        email: null,
        sex: null,
        password: null,
        name: null,
        birthday: null,
        phone: null,
        aboutMe: null
      }
    };
  },
  computed: {
    nameErrors() {
      const errors = [];
      if (!this.$v.form.name.$dirty) return errors;
      !this.$v.form.name.required && errors.push("Укажите имя!");
      return errors;
    },
    sexErrors() {
      const errors = [];
      if (!this.$v.form.sex.$dirty) return errors;
      !this.$v.form.sex.required && errors.push("Укажите пол!");
      return errors;
    },
    phoneErrors() {
      const errors = [];
      if (!this.$v.form.phone.$dirty) return errors;
      !this.$v.form.phone.minLength &&
        errors.push("Введите номер телефон полностью! ");
      !this.$v.form.phone.required && errors.push("Укажите номер телефона!");
      return errors;
    },
    emailErrors() {
      const errors = [];
      if (!this.$v.form.email.$dirty) return errors;
      !this.$v.form.email.email && errors.push("Введите корректный e-mail");
      !this.$v.form.email.required && errors.push("Укажите ваш e-mail");
      this.formEmailErrors.length > 0 &&
        this.formEmailErrors.forEach(element => {
          errors.push(element);
        });
      return errors;
    },
    passwordErrors() {
      const errors = [];
      if (!this.$v.form.password.$dirty) return errors;
      !this.$v.form.password.required && errors.push("Укажите пароль!");
      !this.$v.form.password.minLength &&
        errors.push("Пароль должен содержать минимум 8 символов!");
      this.formPasswordErrors.length > 0 &&
        this.formPasswordErrors.forEach(element => {
          errors.push(element);
        });
      return errors;
    },
    aboutMeErrors() {
      const errors = [];
      if (!this.$v.form.aboutMe.$dirty) return errors;
      !this.$v.form.aboutMe.required &&
        errors.push("Укажите информацию о себе!");
      return errors;
    }
  },
  methods: {
    signUp() {
      let sendObj = { ...this.form };
      sendObj.password1 = this.form.password;
      sendObj.password2 = this.form.password;
      this.formLoading = true;
      this.$store.dispatch("SIGN_UP", sendObj).then(
        () => {
          this.formLoading = false;
          this.$router.push("/");
        },
        errors => {
          this.formLoading = false;
          if (errors.email != null && errors.email.length != 0) {
            for (let index = 0; index < errors.email.length; index++) {
              this.formEmailErrors.push(errors.email[index]);
            }
          }
          if (errors.password1 != null && errors.password1.length != 0) {
            for (let index = 0; index < errors.password1.length; index++) {
              this.formPasswordErrors.push(errors.password1[index]);
            }
          }
        }
      );
    }
  }
};
</script>

<style lang="scss" scoped></style>
