import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import jwt_decode from "jwt-decode";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // jwt: localStorage.getItem("t"),
    // endpoints: {
    //   obtainJWT: "/api/auth/obtain_token",
    //   refreshJWT: "/api/auth/refresh_token"
    // },
    access_token: null,
    refresh_token: localStorage.getItem("t") || null,
    user: {
      email: null,
      first_name: null,
      last_name: null,
      pk: null,
      username: null
    },
    loading: false,
    firstPath: null
  },
  getters: {
    isAuthenticated: state => {
      return state.access_token !== null && state.refresh_token !== null;
    },
    decoded: state => {
      const access_token = state.access_token;
      if (access_token) {
        const decoded = jwt_decode(access_token);
        return decoded;
      } else {
        return null;
      }
    },
    user_id: state => {
      const access_token = state.access_token;
      if (access_token) {
        const decoded = jwt_decode(access_token);
        return decoded.user_id;
      } else {
        return null;
      }
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
    },
    SET_USER(state, user) {
      state.access_token = user.access_token;
      state.refresh_token = user.refresh_token;
      localStorage.setItem("t", user.refresh_token);
      state.user.email = user.user.email;
      state.user.first_name = user.user.first_name;
      state.user.last_name = user.user.last_name;
      state.user.pk = user.user.pk;
      state.user.username = user.user.username;
    },
    SET_ACCESS_TOKEN(state, token) {
      state.access_token = token;
    },
    START_APP_LOADING(state) {
      state.loading = true;
    },
    STOP_APP_LOADING(state) {
      state.loading = false;
    },
    SET_FIRST_PATH(state, firstPath) {
      state.firstPath = firstPath;
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
              store.commit("SET_USER", resp.data);
              resolve(resp.data);
            })
            .catch(err => {
              reject(err.response.data);
            });
        } catch (error) {
          reject(error);
        }
      });
    },
    SIGN_UP(store, data) {
      store.loading = true;
      return new Promise((resolve, reject) => {
        try {
          axios({
            url: "/api/auth/registration/",
            method: "POST",
            data
          })
            .then(resp => {
              store.commit("SET_USER", resp.data);
              store.loading = false;
              resolve(resp.data);
            })
            .catch(err => {
              store.loading = false;
              reject(err.response.data);
            });
        } catch (error) {
          store.loading = false;
          reject(error);
        }
      });
    },
    REFRESH_TOKEN(store) {
      return new Promise((resolve, reject) => {
        try {
          axios({
            url: "/api/auth/token/refresh/",
            method: "POST",
            data: {
              token: store.refresh_token
            }
          })
            .then(resp => {
              store.commit("SET_ACCESS_TOKEN", resp.data.access);
              resolve(resp.data);
            })
            .catch(err => {
              localStorage.clear("t");
              reject(err.response.data);
            });
        } catch (error) {
          reject(error);
        }
      });
    },
    CHANGE_PASSWORD(store, data) {
      store.loading = true;
      return new Promise((resolve, reject) => {
        try {
          axios({
            url: "/api/auth/password/change/",
            method: "POST",
            data
          })
            .then(() => {
              store.loading = false;
              resolve();
            })
            .catch(err => {
              store.loading = false;
              reject(err.response.data);
            });
        } catch (error) {
          store.loading = false;
          reject(error);
        }
      });
    },
    LOG_OUT(store) {
      return new Promise((resolve, reject) => {
        try {
          axios({
            url: "/api/auth/logout/",
            method: "POST",
            data: {}
          })
            .then(resp => {
              store.commit("SET_USER", {
                access_token: null,
                refresh_token: null,
                user: {
                  email: null,
                  first_name: null,
                  last_name: null,
                  pk: null,
                  username: null
                }
              });
              localStorage.clear("t");
              resolve(resp.data);
            })
            .catch(err => {
              localStorage.clear("t");
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
