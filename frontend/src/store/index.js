import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import jwt_decode from "jwt-decode";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    jwt: localStorage.getItem("t"),
    endpoints: {
      obtainJWT: "/api/auth/obtain_token",
      refreshJWT: "/api/auth/refresh_token"
    }
  },
  mutations: {
    updateToken(state, newToken) {
      localStorage.setItem("t", newToken);
      state.jwt = newToken;
    },
    removeToken(state) {
      localStorage.removeItem("t");
      state.jwt = null;
    }
  },
  actions: {
    obtainToken(username, password) {
      const payload = {
        username: username,
        password: password
      };
      axios
        .post(this.state.endpoints.obtainJWT, payload)
        .then(response => {
          this.commit("updateToken", response.data.token);
        })
        .catch(error => {
          console.log(error);
        });
    },
    refreshToken() {
      const payload = {
        token: this.state.jwt
      };
      axios
        .post(this.state.endpoints.refreshJWT, payload)
        .then(response => {
          this.commit("updateToken", response.data.token);
        })
        .catch(error => {
          console.log(error);
        });
    },
    inspectToken(store) {
      const token = store.state.jwt;
      if (token) {
        const decoded = jwt_decode(token);
        const exp = decoded.exp;
        const orig_iat = decoded.orig_iat;
        if (
          exp - Date.now() / 1000 < 1800 &&
          Date.now() / 1000 - orig_iat < 628200
        ) {
          store.dispatch("refreshToken");
        } else if (exp - Date.now() / 1000 < 1800) {
          // DO NOTHING, DO NOT REFRESH
        } else {
          // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
        }
      }
    },
    LOG_IN(store, data) {
      return new Promise((resolve, reject) => {
        try {
          axios({
            url: "/api/auth/login/",
            method: "POST",
            data
          })
            .then(resp => {
              store.mutate("", resp.data);
              resolve(resp.data);
            })
            .catch(err => {
              reject(err.response.data);
            });
        } catch (error) {
          reject(error);
        }
      });
    }
  },
  modules: {}
});
