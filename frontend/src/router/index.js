import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Auth from "../views/Auth.vue";
import LogIn from "../components/auth/LogIn.vue";
import SignUp from "../components/auth/SignUp.vue";

import store from "../store/index.js";

Vue.use(VueRouter);

const ifAuthenticated = (to, from, next) => {
  if (store.getters.isAuthenticated) {
    next();
    return;
  }
  next("/auth");
};

const ifNotAuthenticated = (to, from, next) => {
  if (!store.getters.isAuthenticated) {
    next();
    return;
  }
  next("/");
};

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    beforeEnter: ifAuthenticated
  },
  {
    path: "/auth",
    component: Auth,
    beforeEnter: ifNotAuthenticated,
    children: [
      {
        path: "",
        name: "LogIn",
        component: LogIn
      },
      {
        path: "signup",
        name: "SignUp",
        component: SignUp
      }
    ]
  }
  // {
  //   path: "/about",
  //   name: "About",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/About.vue"),
  // },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
