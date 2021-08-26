import Vue from "vue";
import Vuex from "vuex";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import VueAxios from "vue-axios";
import vuetify from "./plugins/vuetify";
import { VueMaskDirective } from "v-mask";
import Vuelidate from "vuelidate";
import VueApollo from "vue-apollo";
import { ApolloClient } from "apollo-client";
import { InMemoryCache } from "apollo-cache-inmemory";
// import { createHttpLink } from "apollo-link-http";
import { setContext } from "apollo-link-context";
import Cookies from "js-cookie";
import { createUploadLink } from "apollo-upload-client";

Vue.directive("mask", VueMaskDirective);

Vue.config.productionTip = false;

Vue.use(Vuex);
Vue.use(VueAxios, axios);
Vue.use(Vuelidate);

// Кэш Apollo (Graphql)
const cache = new InMemoryCache({
  addTypename: true
});

// Создание ссылки для Apollo
const httpLink = new createUploadLink({
  uri: process.env.VUE_APP_GRAPHQL_HTTP || "http://localhost:8001/api/graphql/"
});

// Создание websocket ссылки для Subscription
// TODO: включить
// const wsLink = new WebSocketLink({
//   uri: "ws://localhost:8001/api/graphql",
//   options: {
//     reconnect: true
//   }
// });

const authLink = setContext((_, { headers }) => {
  // get the authentication token from local storage if it exists
  const token = Cookies.get("csrftoken");
  // return the headers to the context so httpLink can read them
  return {
    headers: {
      ...headers,
      "X-CSRFToken": token ? `${token}` : ""
    }
  };
});

// Клиент Apollo
const apolloClient = new ApolloClient({
  link: authLink.concat(httpLink),
  cache,
  connectToDevTools: true
});

Vue.use(VueApollo);

// Провайдер Apollo (Graphql)
const apolloProvider = new VueApollo({
  defaultClient: apolloClient
});

new Vue({
  router,
  store,
  vuetify,
  apolloProvider,
  render: h => h(App)
}).$mount("#app");
