<template>
  <v-layout>
    <AppLoader v-if="this.$apollo.queries.user.loading"></AppLoader>
    <v-flex v-if="!this.$apollo.queries.user.loading">
      <h1 class="title mb-5 mt-5 mb-sm-10 mt-sm-10 text-center">Профиль</h1>
      <v-row class="mt-sm-3">
        <v-col class="col-12 col-sm-3 d-flex flex-column align-center">
          <v-avatar
            size="144"
            class="mr-md-4"
            v-if="user.photo && user.photo != ''"
          >
            <img
              class="custom-img"
              :src="`/media/${user.photo}`"
              alt="Аватар"
            />
          </v-avatar>
          <v-avatar size="144" class="mr-md-4" v-else>
            <img
              class="custom-img"
              :src="`/media/photo_placeholder.svg`"
              alt="Аватар"
            />
          </v-avatar>
          <v-btn
            v-if="editFlag"
            @click="onFileInputClick()"
            class="my-button custom-full-width mt-4 white--text"
            color="colorOfSea"
            large
          >
            {{ buttonText | truncate(20) }}
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
              <h2 class="title darkBlue--text mb-5">{{ user.firstName }}</h2>
            </div>
            <v-row>
              <v-col class="col-4">
                <p class="mb-0">Пол:</p>
              </v-col>
              <v-col class="col-8">
                <p class="mb-0">
                  {{ formatGender(user.gender) }}
                </p>
              </v-col>
              <v-col class="col-4">
                <p class="mb-0">Дата рождения:</p>
              </v-col>
              <v-col class="col-8">
                <p class="mb-0">{{ formatDate(user.dateOfBirth) }}</p>
              </v-col>

              <v-col class="col-4">
                <p class="mb-0">Номер телефона:</p>
              </v-col>
              <v-col class="col-8">
                <p class="mb-0">
                  {{ user.phoneNumber }}
                </p>
              </v-col>
              <v-col class="col-4">
                <p class="mb-0">О себе:</p>
              </v-col>
              <v-col class="col-8">
                <p v-if="!editAboutMeFlag" class="mb-0">
                  {{ user.aboutMe }}
                </p>
                <v-textarea
                  v-if="editAboutMeFlag"
                  color="colorOfSea"
                  counter
                  class="pt-0 mt-0"
                  maxlength="200"
                  required
                  :error-messages="aboutMeErrors"
                  v-model.trim="$v.form.aboutMe.$model"
                  @input="$v.form.aboutMe.$touch()"
                  @blur="$v.form.aboutMe.$touch()"
                ></v-textarea>
              </v-col>
            </v-row>
            <v-row v-if="editAboutMeFlag && !editPasswordFlag">
              <v-col class="col-12 pointer">
                <p
                  class="
                    mb-0
                    font-weight-bold
                    colorOfSea--text
                    custom-icon-margin-top
                  "
                  @click="editPasswordFlag = true"
                >
                  <v-icon color="colorOfSea">mdi-pencil</v-icon>
                  Изменить пароль
                </p>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-btn
                  v-if="!editAboutMeFlag"
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
                  v-if="editAboutMeFlag"
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
            <v-row v-if="editPasswordFlag">
              <v-col class="col-4">
                <p class="mb-0">Старый пароль:</p>
              </v-col>
              <v-col class="col-8">
                <v-text-field
                  class="pt-0 mt-0"
                  light="light"
                  :type="passOldShow ? 'text' : 'password'"
                  color="colorOfSea"
                  :append-icon="passOldShow ? 'mdi-eye' : 'mdi-eye-off'"
                  @click:append="passOldShow = !passOldShow"
                  required
                  :error-messages="passwordOldErrors"
                  v-model.trim="$v.formPassword.passwordOld.$model"
                  @input="
                    $v.formPassword.passwordOld.$touch();
                    formPasswordOldErrors = [];
                  "
                  @blur="
                    $v.formPassword.passwordOld.$touch();
                    formPasswordOldErrors = [];
                  "
                  counter
                ></v-text-field>
              </v-col>
              <v-col class="col-4">
                <p class="mb-0">Новый пароль:</p>
              </v-col>
              <v-col class="col-8">
                <v-text-field
                  class="pt-0 mt-0"
                  light="light"
                  :type="passNewShow ? 'text' : 'password'"
                  color="colorOfSea"
                  :append-icon="passNewShow ? 'mdi-eye' : 'mdi-eye-off'"
                  @click:append="passNewShow = !passNewShow"
                  required
                  :error-messages="passwordNewErrors"
                  v-model.trim="$v.formPassword.passwordNew.$model"
                  @input="
                    $v.formPassword.passwordNew.$touch();
                    formPasswordNewErrors = [];
                  "
                  @blur="
                    $v.formPassword.passwordNew.$touch();
                    formPasswordNewErrors = [];
                  "
                  counter
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row v-if="editPasswordFlag">
              <v-col>
                <v-btn
                  color="colorOfSea"
                  class="
                    custom-mobile-full-width
                    my-button
                    wide-padding
                    white--text
                  "
                  large
                  :disabled="$v.formPassword.$invalid"
                  @click="onEditPassword()"
                  >Сохранить новый пароль</v-btn
                >
              </v-col>
            </v-row>
          </div>
        </v-col>
      </v-row>
    </v-flex>
    <v-snackbar v-model="snackbarPassword" color="colorOfSea" timeout="4000">
      Вы успешно изменили пароль!
      <template v-slot:action="{ attrs }">
        <v-btn
          color="white"
          text
          v-bind="attrs"
          @click="snackbarPassword = false"
        >
          Закрыть
        </v-btn>
      </template>
    </v-snackbar>
    <v-snackbar v-model="snackbarAboutMe" color="colorOfSea" timeout="4000">
      Вы успешно изменили информацию о себе!
      <template v-slot:action="{ attrs }">
        <v-btn
          color="white"
          text
          v-bind="attrs"
          @click="snackbarAboutMe = false"
        >
          Закрыть
        </v-btn>
      </template>
    </v-snackbar>
  </v-layout>
</template>

<script>
import AppLoader from "@/components/global/AppLoader.vue";
import { required, minLength } from "vuelidate/lib/validators";
import { USER_INFORMATION } from "@/graphql/user_queries";
import { EDIT_ABOUT_ME } from "@/graphql/user_mutations";
export default {
  name: "Account",
  components: {
    AppLoader
  },

  apollo: {
    user: {
      query: USER_INFORMATION,
      variables() {
        return { userId: this.$store.getters.user_id };
      }
    }
  },
  validations: {
    form: {
      aboutMe: {
        required
      }
    },
    formPassword: {
      passwordNew: {
        required,
        minLength: minLength(8)
      },
      passwordOld: {
        required,
        minLength: minLength(8)
      }
    }
  },
  data() {
    return {
      snackbarPassword: false,
      snackbarAboutMe: false,
      editAboutMeFlag: false,
      editPasswordFlag: false,
      passNewShow: false,
      passOldShow: false,
      defaultButtonText: "Изменить фото",
      selectedFile: null,
      isSelecting: false,
      formPasswordNewErrors: [],
      formPasswordOldErrors: [],
      form: {
        aboutMe: null
      },
      formPassword: {
        passwordNew: null,
        passwordOld: null
      }
    };
  },
  filters: {
    truncate: function (data, num) {
      const reqdString = data.split("").slice(0, num).join("");
      const reqdString_array = data.split("");
      if (data != "Изменить фото" && reqdString_array.length >= 20) {
        const reqdStringAll = reqdString + "...";
        return reqdStringAll;
      } else {
        return reqdString;
      }
    }
  },

  computed: {
    editFlag() {
      return this.editAboutMeFlag || this.editPasswordFlag;
    },
    passwordNewErrors() {
      const errors = [];
      if (!this.$v.formPassword.passwordNew.$dirty) return errors;
      !this.$v.formPassword.passwordNew.required &&
        errors.push("Укажите пароль!");
      !this.$v.formPassword.passwordNew.minLength &&
        errors.push("Пароль должен содержать минимум 8 символов!");
      this.formPasswordNewErrors.length > 0 &&
        this.formPasswordNewErrors.forEach(element => {
          errors.push(element);
        });
      return errors;
    },
    passwordOldErrors() {
      const errors = [];
      if (!this.$v.formPassword.passwordOld.$dirty) return errors;
      !this.$v.formPassword.passwordOld.required &&
        errors.push("Укажите пароль!");
      !this.$v.formPassword.passwordOld.minLength &&
        errors.push("Пароль должен содержать минимум 8 символов!");
      this.formPasswordOldErrors.length > 0 &&
        this.formPasswordOldErrors.forEach(element => {
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
    formatGender(gender) {
      if (gender == "F") return "Женский";
      if (gender == "M") return "Мужской";
      if (gender == "NS") return "Не указан";
      return null;
    },
    onEdit() {
      if (!this.editAboutMeFlag) {
        this.form.aboutMe = this.user.aboutMe;
        this.editAboutMeFlag = true;
      } else {
        if (
          this.user.aboutMe == this.$v.form.aboutMe.$model &&
          this.selectedFile == null
        ) {
          this.editAboutMeFlag = false;
        } else {
          this.$apollo
            .mutate({
              mutation: EDIT_ABOUT_ME,
              variables: {
                userId: this.$store.getters.user_id,
                aboutMe: this.$v.form.aboutMe.$model,
                photo: this.selectedFile
              },
              update: (cache, { data: { updateUserInformation } }) => {
                let data = cache.readQuery({
                  query: USER_INFORMATION,
                  variables: { userId: this.$store.getters.user_id }
                });

                if (updateUserInformation.user != undefined) {
                  data.user.aboutMe = updateUserInformation.user.aboutMe;
                  data.user.photo = updateUserInformation.user.photo;
                }

                cache.writeQuery({
                  query: USER_INFORMATION,
                  variables: { userId: this.$store.getters.user_id },
                  data
                });
              },
              optimisticResponse: {
                __typename: "Mutation",
                updateUserInformation: {
                  __typename: "UpdateUserInformation",
                  user: {
                    __typename: "CustomUserType",
                    id: this.$store.getters.user_id,
                    firstName: this.user.firstName,
                    aboutMe: this.$v.form.aboutMe.$model,
                    dateOfBirth: this.user.dateOfBirth,
                    gender: this.user.gender,
                    photo: this.user.photo,
                    phoneNumber: this.user.phoneNumber
                  }
                }
              }
            })
            .then(() => {
              this.editAboutMeFlag = false;
              this.snackbarAboutMe = true;
            })
            .catch(error => {
              console.error(error);
            });
        }
      }
    },
    onEditPassword() {
      if (!this.editPasswordFlag) {
        this.editPasswordFlag = true;
      } else {
        if (this.formPassword.passwordNew == this.formPassword.passwordOld) {
          this.formPasswordNewErrors.push("Пароли совпадают!");
          this.formPasswordOldErrors.push("Пароли совпадают!");
        }
        let sendObj = {
          new_password1: this.formPassword.passwordNew,
          new_password2: this.formPassword.passwordNew,
          old_password: this.formPassword.passwordOld
        };
        this.$store.dispatch("CHANGE_PASSWORD", sendObj).then(
          () => {
            this.snackbarPassword = true;
            this.editPasswordFlag = false;
            this.formPassword.passwordNew = "";
            this.formPassword.passwordOld = "";
            this.passNewShow = false;
            this.passOldShow = false;
            this.formPasswordNewErrors = [];
            this.formPasswordOldErrors = [];
          },
          errors => {
            if (
              errors.new_password2 != null &&
              errors.new_password2.length != 0
            ) {
              for (
                let index = 0;
                index < errors.new_password2.length;
                index++
              ) {
                this.formPasswordNewErrors.push(errors.new_password2[index]);
              }
            }
            if (
              errors.old_password != null &&
              errors.old_password.length != 0
            ) {
              for (let index = 0; index < errors.old_password.length; index++) {
                this.formPasswordOldErrors.push(errors.old_password[index]);
              }
            }
          }
        );
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
.custom-icon-margin-top {
  margin-top: -2px;
}

.v-card__title {
  width: 100%;
}

.custom-img {
  width: unset;
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
