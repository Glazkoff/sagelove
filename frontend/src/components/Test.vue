<template>
  <div>
    <v-form ref="form" lazy-validation>
      <v-file-input
        chips
        accept="image/png, image/jpeg, image/bmp"
        placeholder="Прикрепите фото"
        label="Фото"
        prepend-icon="mdi-camera"
        v-model="$v.form.photo.$model"
      ></v-file-input>
      <v-btn
        class="mt-8 my-button wide-padding white--text"
        color="colorOfSea"
        @click.prevent="click"
        block="block"
        type="submit"
        :disabled="$v.form.$invalid"
        >Зарегистрироваться</v-btn
      >
    </v-form>
  </div>
</template>

<script>
import { required } from "vuelidate/lib/validators";
import { SET_USER_PHOTO } from "@/graphql/user_mutations.js";

export default {
  name: "Test",
  data() {
    return {
      form: {
        photo: null
      }
    };
  },
  validations: {
    form: {
      photo: {
        required
      }
    }
  },
  methods: {
    click() {
      console.log(this.$v.form.$model.photo);
      this.$apollo
        .mutate({
          mutation: SET_USER_PHOTO,
          variables: {
            userId: 1,
            photo: this.$v.form.$model.photo
          }
        })
        .then(res => {
          console.log(res);
        });
    }
  }
};
</script>

<style lang="scss" scoped></style>
