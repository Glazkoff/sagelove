<template>
  <v-flex class="auth-form text-center">
    <h1 class="display-1 mb-3">Регистрация</h1>
    <v-card flat light="light">
      <v-card-text>
        <v-form>
          <v-text-field
            light="light"
            label="Имя"
            type="text"
            color="colorOfSea"
            autocomplete="name"
            v-model="name"
          ></v-text-field>
          <v-select
            :items="[
              { text: 'Мужской', val: 'м' },
              { text: 'Женский', val: 'ж' }
            ]"
            item-text="text"
            item-value="val"
            label="Пол"
            color="colorOfSea"
          ></v-select>
          <!-- <v-menu
            ref="menu"
            v-model="dateMenu"
            :close-on-content-click="false"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="auto"
            color="colorOfSea"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="birthday"
                label="Дата рождения"
                prepend-icon="mdi-calendar"
                v-bind="attrs"
                v-on="on"
                color="colorOfSea"
              ></v-text-field>
            </template>
            <v-date-picker
              color="colorOfSea"
              v-model="birthday"
              @input="dateMenu = false"
            ></v-date-picker>
          </v-menu> -->
          <DatePicker
            label="Дата рождения"
            @update="birthday = $event"
          ></DatePicker>
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
            >Зарегистрироваться</v-btn
          >
        </v-form>
      </v-card-text>
    </v-card>
    <div class="darkBlue--text">
      Уже есть аккаунт?
      <v-btn class="darkBlueGreen--text" text to="/auth">Войдите!</v-btn>
    </div>
  </v-flex>
</template>

<script>
import DatePicker from "@/components/global/DatePicker";
export default {
  name: "SignUp",
  components: {
    DatePicker
  },
  data() {
    return {
      passShow: false,
      dateMenu: false,
      email: "",
      password: "",
      name: "",
      birthday: ""
    };
  }
};
</script>

<style lang="scss" scoped></style>
