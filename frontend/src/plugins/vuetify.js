import Vue from "vue";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
import ru from "vuetify/lib/locale/ru";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    options: {
      customProperties: true
    },
    themes: {
      light: {
        primary: "#007BFF",
        secondary: "#424242",
        accent: "#82B1FF",
        error: "#DA2036",
        info: "#2196F3",
        success: "#4CAF50",
        warning: "#FFC107",
        white: "#FFFFFF",
        lightBlue: "#C8F5FA",
        pink: "#FF618C",
        green: "#00C76F",
        colorOfSea: "#00ACC2",
        darkBlueGreen: "#016064",
        darkBlue: "#013351",
        grey: "#949494",
        lightLightBlue: "#E2F9FC"
      }
    }
  },
  lang: {
    locales: { ru },
    current: "ru"
  }
});
