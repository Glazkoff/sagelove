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
        @blur="date = parseDate(dateFormatted)"
        v-on="on"
        color="colorOfSea"
      ></v-text-field>
    </template>
    <v-date-picker
      v-model="date"
      no-title
      @input="menu = false"
      color="colorOfSea"
    ></v-date-picker>
  </v-menu>
</template>

<script>
export default {
  name: "DatePicker",
  props: ["label", "value"],
  data() {
    return {
      date: null,
      dateFormatted: this.formatDate(new Date().toISOString().substr(0, 10)),
      menu: false
    };
  },
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date);
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
