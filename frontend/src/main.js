import Vue from "vue";
import Vuex from "vuex";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import VueAxios from "vue-axios";
import vuetify from "./plugins/vuetify";
import VueTelInputVuetify from "vue-tel-input-vuetify/lib";

Vue.config.productionTip = false;

Vue.use(Vuex);
Vue.use(VueAxios, axios);
Vue.use(VueTelInputVuetify, {
  vuetify
});

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
