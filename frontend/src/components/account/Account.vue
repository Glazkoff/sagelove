<template>
  <v-layout>
    <v-flex>
      <h1 class="title mb-5 mt-5 mb-sm-10 mt-sm-10 text-center">
        Личный кабинет
      </h1>
      <v-row class="mt-sm-3">
        <v-col class="col-12 col-sm-3 d-flex flex-column align-center">
          <img
            class="custom-img mr-md-4"
            src="https://picsum.photos/200"
            alt="Ававтар"
          />

          <v-btn
            v-if="editFlag"
            @click="onFileInputClick()"
            class="my-button custom-full-width mt-4 white--text"
            color="colorOfSea"
            large
          >
            {{ buttonText }}
          </v-btn>
          <input
            ref="finput"
            class="d-none"
            type="file"
            accept="image/*"
            @change="onFileChanged"
          />
        </v-col>
        <v-col class="col-12 col-sm-9">
          <div class="custom-card pa-4 pa-sm-8">
            <div>
              <h2 class="title darkBlue--text mb-5">{{ person.user_name }}</h2>
            </div>
            <v-row>
              <v-col class="col-4">
                <p class="mb-0">Пол:</p>
              </v-col>
              <v-col class="col-8">
                <p class="mb-0">
                  {{ person.gender }}
                </p>
              </v-col>
              <v-col class="col-4">
                <p class="mb-0">Дата рождения:</p>
              </v-col>
              <v-col class="col-8">
                <p class="mb-0">{{ formatDate(person.user_birthday) }}</p>
              </v-col>

              <v-col class="col-4">
                <p class="mb-0">Номер телефона:</p>
              </v-col>
              <v-col class="col-8">
                <p class="mb-0">
                  {{ formatPhone(person.phone_number) }}
                </p>
              </v-col>
              <v-col class="col-4">
                <p class="mb-0">О себе:</p>
              </v-col>
              <v-col class="col-8">
                <p v-if="!editFlag" class="mb-0">
                  {{ person.personal_information }}
                </p>
                <v-textarea
                  v-if="editFlag"
                  color="colorOfSea"
                  counter
                  class="pt-0 mt-0"
                  maxlength="200"
                  required
                  :error-messages="about_meErrors"
                  v-model.trim="$v.form.about_me.$model"
                  @input="$v.form.about_me.$touch()"
                  @blur="$v.form.about_me.$touch()"
                ></v-textarea>
              </v-col>
              <v-col v-if="editFlag" class="col-4">
                <p class="mb-0">Старый пароль:</p>
              </v-col>
              <v-col class="col-8">
                <v-text-field
                  class="pt-0 mt-0"
                  v-if="editFlag"
                  light="light"
                  :type="passOldShow ? 'text' : 'password'"
                  color="colorOfSea"
                  :append-icon="passOldShow ? 'mdi-eye' : 'mdi-eye-off'"
                  @click:append="passOldShow = !passOldShow"
                  autocomplete="current-password"
                  required
                  :error-messages="passwordOldErrors"
                  v-model.trim="$v.form.passwordOld.$model"
                  @input="
                    $v.form.passwordOld.$touch();
                    formPasswordOldErrors = [];
                  "
                  @blur="
                    $v.form.passwordOld.$touch();
                    formPasswordOldErrors = [];
                  "
                  counter
                ></v-text-field>
              </v-col>
              <v-col v-if="editFlag" class="col-4">
                <p class="mb-0">Новый пароль:</p>
              </v-col>
              <v-col class="col-8">
                <v-text-field
                  class="pt-0 mt-0"
                  v-if="editFlag"
                  light="light"
                  :type="passNewShow ? 'text' : 'password'"
                  color="colorOfSea"
                  :append-icon="passNewShow ? 'mdi-eye' : 'mdi-eye-off'"
                  @click:append="passNewShow = !passNewShow"
                  autocomplete="current-password"
                  required
                  :error-messages="passwordNewErrors"
                  v-model.trim="$v.form.passwordNew.$model"
                  @input="
                    $v.form.passwordNew.$touch();
                    formPasswordNewErrors = [];
                  "
                  @blur="
                    $v.form.passwordNew.$touch();
                    formPasswordNewErrors = [];
                  "
                  counter
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-btn
                  v-if="!editFlag"
                  color="colorOfSea"
                  class="
                    custom-mobile-full-width
                    my-button
                    wide-padding
                    white--text
                  "
                  large
                  @click="onEdit()"
                  >Изменить</v-btn
                >
                <v-btn
                  v-if="editFlag"
                  large
                  color="colorOfSea"
                  class="
                    custom-mobile-full-width
                    my-button
                    wide-padding
                    white--text
                  "
                  :disabled="$v.form.$invalid"
                  @click="onEdit()"
                  >Сохранить</v-btn
                >
              </v-col>
            </v-row>
          </div>
        </v-col>
      </v-row>
    </v-flex>
  </v-layout>
</template>

<script>
import { required, minLength } from "vuelidate/lib/validators";
export default {
  name: "Account",
  validations: {
    form: {
      passwordNew: {
        required,
        minLength: minLength(8)
      },
      passwordOld: {
        required,
        minLength: minLength(8)
      },
      about_me: {
        required
      }
    }
  },
  data() {
    return {
      editFlag: false,
      passNewShow: false,
      passOldShow: false,
      defaultButtonText: "Изменить фото",
      selectedFile: null,
      isSelecting: false,
      formPasswordNewErrors: [],
      formPasswordOldErrors: [],
      form: {
        passwordNew: null,
        passwordOld: null,
        about_me: null
      },
      person: {
        id: 1,
        user_name: "Иван",
        gender: "Мужской",
        user_birthday: "1987-06-15",
        phone_number: "9271112233",
        url_foto: "",
        personal_information:
          "Текст о себе, текст о себе. Текст о себе, текст о себе.Текст о себе, текст о себе."
      }
    };
  },
  computed: {
    passwordNewErrors() {
      const errors = [];
      if (!this.$v.form.passwordNew.$dirty) return errors;
      !this.$v.form.passwordNew.required && errors.push("Укажите пароль!");
      !this.$v.form.passwordNew.minLength &&
        errors.push("Пароль должен содержать минимум 8 символов!");
      this.formPasswordNewErrors.length > 0 &&
        this.formPasswordNewErrors.forEach(element => {
          errors.push(element);
        });
      return errors;
    },
    passwordOldErrors() {
      const errors = [];
      if (!this.$v.form.passwordOld.$dirty) return errors;
      !this.$v.form.passwordOld.required && errors.push("Укажите пароль!");
      !this.$v.form.passwordOld.minLength &&
        errors.push("Пароль должен содержать минимум 8 символов!");
      this.formPasswordOldErrors.length > 0 &&
        this.formPasswordOldErrors.forEach(element => {
          errors.push(element);
        });
      return errors;
    },
    about_meErrors() {
      const errors = [];
      if (!this.$v.form.about_me.$dirty) return errors;
      !this.$v.form.about_me.required &&
        errors.push("Укажите информацию о себе!");
      return errors;
    },
    buttonText() {
      return this.selectedFile
        ? this.selectedFile.name
        : this.defaultButtonText;
    }
  },
  methods: {
    formatDate(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      return `${day}.${month}.${year}`;
    },
    formatPhone(phone) {
      if (!phone) return null;
      return `+7 (${phone[0]}${phone[1]}${phone[2]}) ${phone[3]}${phone[4]}${phone[5]}-${phone[6]}${phone[7]}-${phone[8]}${phone[9]}`;
    },
    onEdit() {
      if (!this.editFlag) {
        this.form.about_me = this.person.personal_information;
        this.editFlag = true;
      } else {
        this.editFlag = false;
        this.person.personal_information = this.$v.form.about_me.$model;
      }
    },
    onFileInputClick() {
      this.isSelecting = true;
      window.addEventListener(
        "focus",
        () => {
          this.isSelecting = false;
        },
        { once: true }
      );

      this.$refs.finput.click();
    },
    onFileChanged(e) {
      this.selectedFile = e.target.files[0];
    }
  }
};
</script>

<style lang="scss" scoped>
.v-card__title {
  width: 100%;
}

.custom-img {
  width: 100%;
  height: auto;
  border-radius: 50%;
}

.custom-card {
  background: var(--v-lightLightBlue-base);
  min-height: 10rem;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}

.my-button.custom-full-width {
  width: 100%;
}

.custom-choose-image {
  position: absolute;
}

@media (max-width: 599px) {
  .my-button.custom-mobile-full-width {
    width: 100%;
  }
}
</style>
