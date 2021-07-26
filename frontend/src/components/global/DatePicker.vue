<template>
  <v-menu
    ref="menu"
    v-model="menu"
    :close-on-content-click="false"
    transition="scale-transition"
    offset-y
    max-width="290px"
    min-width="auto"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-text-field
        v-model="dateFormatted"
        :label="label"
        persistent-hint
        prepend-icon="mdi-calendar"
        v-bind="attrs"
        :autocomplete="autocomplete"
        @blur="
          date = parseDate(dateFormatted);
          $v.dateFormatted.$touch();
        "
        v-on="on"
        color="colorOfSea"
        v-mask="'##.##.####'"
        required
        :error-messages="dateErrors"
        v-model.trim="$v.dateFormatted.$model"
        @input="$v.dateFormatted.$touch()"
      ></v-text-field>
    </template>
    <v-date-picker
      v-model="date"
      no-title
      @input="menu = false"
      color="colorOfSea"
      :max="max"
      :min="min"
    ></v-date-picker>
  </v-menu>
</template>

<script>
import { required } from "vuelidate/lib/validators";
export default {
  name: "DatePicker",
  props: ["label", "value", "autocomplete", "max", "min"],
  validations: {
    dateFormatted: {
      required
    }
  },
  data() {
    return {
      date: null,
      dateFormatted: null,
      menu: false
    };
  },
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
    dateErrors() {
      const errors = [];
      if (!this.$v.dateFormatted.$dirty) return errors;
      !this.$v.dateFormatted.required && errors.push("Укажите дату!");
      return errors;
    }
  },
  watch: {
    date() {
      this.dateFormatted = this.formatDate(this.date);
      this.$emit("update", this.dateFormatted);
    }
  },
  methods: {
    formatDate(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      return `${day}.${month}.${year}`;
    },
    parseDate(date) {
      if (!date) return null;

      const [day, month, year] = date.split(".");
      return `${year}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
    }
  }
};
</script>

<style lang="scss" scoped></style>
