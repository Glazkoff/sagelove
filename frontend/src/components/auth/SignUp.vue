<template>
  <v-flex class="auth-form text-center">
    <h1 class="mt-13 title mb-12">Регистрация</h1>

    <v-card flat light="light">
      <v-card-text>
        <div class="text-left">
          <small>Все поля отмеченные * обязательны к заполнению</small>
        </div>
        <v-form>
          <v-text-field
            light="light"
            label="Имя*"
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
              { text: 'Мужской', val: 'M' },
              { text: 'Женский', val: 'F' }
            ]"
            autocomplete="gender"
            item-text="text"
            item-value="val"
            label="Пол*"
            color="colorOfSea"
            required
            :error-messages="genderErrors"
            v-model.trim="$v.form.gender.$model"
            @input="$v.form.gender.$touch()"
            @blur="$v.form.gender.$touch()"
            :disabled="formLoading"
          ></v-select>
          <DatePicker
            label="Дата рождения*"
            autocomplete="date_of_birth"
            @update="form.date_of_birth = $event"
            :disabled="formLoading"
            :max="getMaxDate"
            :errors="dateOfBirthErrors"
          ></DatePicker>
          <v-text-field
            light="light"
            label="Телефон*"
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
            label="Email*"
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
            label="Пароль*"
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
            label="Ваша фотография*"
            color="colorOfSea"
            class="mb-2"
            v-model="$v.form.photo.$model"
            accept="image/png, image/jpeg, image/bmp"
            placeholder="Прикрепите ваше фото"
            @input="$v.form.photo.$touch()"
            @blur="$v.form.photo.$touch()"
            :error-messages="photoErrors"
            :messages="[
              'Загрузите в формате png, jpeg, jpg, pjp, pjpeg, jfif, bmp'
            ]"
          ></v-file-input>
          <v-textarea
            :disabled="formLoading"
            label="О себе*"
            color="colorOfSea"
            counter
            maxlength="200"
            required
            :error-messages="aboutMeErrors"
            v-model.trim="$v.form.about_me.$model"
            @input="$v.form.about_me.$touch()"
            @blur="$v.form.about_me.$touch()"
          ></v-textarea>
          <v-btn
            class="mt-8 my-button wide-padding white--text"
            color="colorOfSea"
            @click.prevent="signUp"
            block="block"
            type="submit"
            :disabled="$v.form.$anyError || formLoading"
            :loading="formLoading"
            >Зарегистрироваться</v-btn
          >
        </v-form>
      </v-card-text>
    </v-card>
    <div class="darkBlue--text mb-16">
      Уже есть аккаунт?
      <router-link class="link" :exact="true" to="/login">Войдите!</router-link>
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
import { UPLOAD_USER_PHOTO } from "@/graphql/user_mutations";

export default {
  name: "SignUp",
  validations: {
    form: {
      name: {
        required
      },
      gender: {
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
      date_of_birth: {
        required
      },
      photo: {
        required
      },
      about_me: {
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
        gender: null,
        password: null,
        name: null,
        date_of_birth: null,
        phone: null,
        photo: null,
        about_me: null
      }
    };
  },
  computed: {
    getMaxDate() {
      let endDate = new Date(
        new Date().getFullYear() - 18,
        new Date().getMonth(),
        new Date().getDate()
      );
      return endDate.toISOString().slice(0, 10);
    },
    nameErrors() {
      const errors = [];
      if (!this.$v.form.name.$dirty) return errors;
      !this.$v.form.name.required && errors.push("Укажите имя!");
      return errors;
    },
    genderErrors() {
      const errors = [];
      if (!this.$v.form.gender.$dirty) return errors;
      !this.$v.form.gender.required && errors.push("Укажите пол!");
      return errors;
    },
    dateOfBirthErrors() {
      const errors = [];
      if (!this.$v.form.date_of_birth.$dirty) return errors;
      !this.$v.form.date_of_birth.required &&
        errors.push("Укажите дату рождения!");
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
    photoErrors() {
      const errors = [];
      if (!this.$v.form.photo.$dirty) return errors;
      !this.$v.form.photo.required && errors.push("Прикрепите фото!");
      return errors;
    },
    aboutMeErrors() {
      const errors = [];
      if (!this.$v.form.about_me.$dirty) return errors;
      !this.$v.form.about_me.required &&
        errors.push("Укажите информацию о себе!");
      return errors;
    }
  },
  methods: {
    signUp() {
      this.$v.form.$touch();
      if (!this.$v.form.$anyError) {
        let sendObj = { ...this.form };
        sendObj.password1 = this.form.password;
        sendObj.password2 = this.form.password;
        sendObj.first_name = this.form.name;
        sendObj.name = undefined;
        sendObj.phone_number = this.form.phone;
        sendObj.phone = undefined;
        this.formLoading = true;
        this.$store.dispatch("SIGN_UP", sendObj).then(
          res => {
            this.$apollo
              .mutate({
                mutation: UPLOAD_USER_PHOTO,
                variables: {
                  userId: res.user.pk,
                  photo: this.form.photo
                }
              })
              .then(() => {
                this.$router.push("/");
              })
              .finally(() => (this.formLoading = false));
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
            if (
              errors.non_field_errors != null &&
              errors.non_field_errors.length != 0
            ) {
              for (
                let index = 0;
                index < errors.non_field_errors.length;
                index++
              ) {
                this.formPasswordErrors.push(errors.non_field_errors[index]);
              }
            }
          }
        );
      }
    }
  }
};
</script>

<style lang="scss" scoped></style>
