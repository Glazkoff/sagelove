import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Auth from "../views/Auth.vue";
import LogIn from "../components/auth/LogIn.vue";
import SignUp from "../components/auth/SignUp.vue";

import Aims from "../components/aims/Aims.vue";

import Account from "../components/account/Account.vue";

import Chat from "../components/chat/Chat.vue";

import Datings from "../components/datings/Datings.vue";
import DatingsPerson from "../components/datings/DatingsPerson.vue";
import DatingsStatus from "../components/datings/DatingsStatus.vue";

import OnBoarding from "../components/onboarding/OnBoarding.vue";

import Test from "../components/test/Test.vue";
import TestStatus from "../components/test/TestStatus.vue";
import TestQuestion from "../components/test/TestQuestion.vue";
import TestResult from "../components/test/TestResult.vue";

import store from "../store/index.js";

Vue.use(VueRouter);

const ifAuthenticated = (to, from, next) => {
  if (store.getters.isAuthenticated) {
    next();
    return;
  }
  next("/login");
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
    beforeEnter: ifAuthenticated,
    children: [
      {
        path: "",
        component: OnBoarding
      },
      {
        path: "/test",
        component: Test,
        children: [
          {
            path: "",
            component: TestStatus
          },
          {
            path: "/question/:id",
            component: TestQuestion
          },
          {
            path: "/result",
            component: TestResult
          }
        ]
      },
      {
        path: "/aims",
        component: Aims
      },
      {
        path: "/account",
        component: Account
      },
      {
        path: "/chat",
        component: Chat
      },
      {
        path: "/datings",
        component: Datings,
        children: [
          {
            name: "DatingsStatus",
            path: "",
            component: DatingsStatus
          },
          {
            name: "DatingsPerson",
            path: "/person/:id",
            component: DatingsPerson
          }
        ]
      }
    ]
  },
  {
    path: "/login",
    component: Auth,
    beforeEnter: ifNotAuthenticated,
    children: [
      {
        path: "",
        name: "LogIn",
        component: LogIn
      }
    ]
  },
  {
    path: "/signup",
    component: Auth,
    beforeEnter: ifNotAuthenticated,
    children: [
      {
        path: "",
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
