<template>
  <v-app>
    <AppLoader
      v-if="this.$apollo.queries.user.loading || user == undefined"
    ></AppLoader>
    <v-app-bar v-if="user != undefined" app color="lightBlue">
      <v-container class="py-0 fill-height">
        <v-app-bar-nav-icon
          color="colorOfSea"
          @click="drawer = true"
          class="pointer d-flex d-md-none"
        ></v-app-bar-nav-icon>
        <img
          @click="routerToHome()"
          src="../assets/img/logo.svg"
          alt="Logo"
          class="py-0 width-logo pointer"
        />

        <v-spacer class="d-none d-md-flex"></v-spacer>
        <div id="nav" class="d-none d-md-flex flex-row align-center">
          <router-link
            v-if="
              user != undefined &&
              user.watchOnBoarding &&
              user.partnerType &&
              user.purposeMeet &&
              user.numberFotoHistoryByFelling &&
              user.testStatus.toUpperCase() != 'FINISH'
            "
            :exact="true"
            to="/test"
            tag="p"
            class="mb-0 pointer custom-menu-link"
            >Тестирование</router-link
          >
          <router-link
            v-if="
              user != undefined && user.testStatus.toUpperCase() == 'FINISH'
            "
            :exact="true"
            to="/result"
            tag="p"
            class="mb-0 ml-16 pointer custom-menu-link"
            >Результаты</router-link
          >
          <router-link
            v-if="
              user != undefined && user.testStatus.toUpperCase() == 'FINISH'
            "
            :exact="true"
            to="/datings"
            tag="p"
            class="mb-0 ml-16 pointer custom-menu-link"
            >Знакомства</router-link
          >
          <!-- <router-link
            v-if="
              user != undefined && user.testStatus.toUpperCase() == 'FINISH'
            "
            :exact="true"
            to="/chat"
            tag="p"
            class="mb-0 ml-16 pointer custom-menu-link"
            >Чаты</router-link
          > -->

          <v-menu offset-y offset-overflow :close-on-content-click="true">
            <template v-slot:activator="{ on, attrs }">
              <div class="user-group d-flex flex-row align-center ml-16">
                <v-avatar
                  size="40"
                  class="mr-md-4 mr-2"
                  v-if="user.photo && user.photo != ''"
                >
                  <img
                    style="width: unset"
                    class="custom-img"
                    :src="`/media/${user.photo}`"
                    alt="Аватар"
                  />
                </v-avatar>
                <v-avatar size="40" class="mr-md-4" v-else>
                  <img
                    style="width: unset"
                    class="custom-img mr-2"
                    :src="`/media/photo_placeholder.svg`"
                    alt="Аватар"
                  />
                </v-avatar>
                <p class="mb-0 mr-2 pointer" v-bind="attrs" v-on="on">
                  {{ user !== undefined ? user.firstName : "-" }}
                </p>
                <v-icon
                  color="colorOfSea"
                  v-bind="attrs"
                  v-on="on"
                  class="pointer"
                  >mdi-menu-down</v-icon
                >
              </div>
            </template>
            <v-list>
              <v-list-item v-if="user != undefined && user.watchOnBoarding">
                <v-list-item-title>
                  <router-link
                    :exact="true"
                    to="/account"
                    tag="p"
                    class="mb-0 pointer"
                    >Профиль</router-link
                  ></v-list-item-title
                >
              </v-list-item>
              <v-list-item
                v-if="
                  user != undefined &&
                  user.watchOnBoarding &&
                  user.partnerType &&
                  user.purposeMeet &&
                  user.numberFotoHistoryByFelling
                "
              >
                <v-list-item-title>
                  <router-link
                    :exact="true"
                    to="/aims_account"
                    tag="p"
                    class="mb-0 pointer"
                    >Цели</router-link
                  ></v-list-item-title
                >
              </v-list-item>

              <v-list-item>
                <v-list-item-title>
                  <p class="mb-0 pointer" @click="dialog = true">Выйти</p>
                </v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </div>
      </v-container>
    </v-app-bar>

    <v-main>
      <v-container
        class="h-100"
        :class="{ 'p-0-imp': this.$route.path == '/chat' }"
      >
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-navigation-drawer v-model="drawer" fixed temporary>
      <v-list nav dense>
        <v-list-item-group v-model="group" active-class="colorOfSea--text ">
          <p class="ma-2 pointer font-weight-bold">
            Здравствуйте, {{ user !== undefined ? user.firstName : "-" }}!
          </p>

          <v-list-item
            v-if="
              user != undefined &&
              user.watchOnBoarding &&
              user.partnerType &&
              user.purposeMeet &&
              user.numberFotoHistoryByFelling &&
              user.testStatus.toUpperCase() != 'FINISH'
            "
          >
            <v-list-item-title>
              <router-link :exact="true" to="/test" tag="p" class="mb-0 pointer"
                >Тестирование</router-link
              ></v-list-item-title
            >
          </v-list-item>
          <v-list-item
            v-if="
              user != undefined &&
              user.watchOnBoarding &&
              user.testStatus.toUpperCase() == 'FINISH'
            "
          >
            <v-list-item-title>
              <router-link
                :exact="true"
                to="/result"
                tag="p"
                class="mb-0 pointer"
                >Результаты тестирования</router-link
              ></v-list-item-title
            >
          </v-list-item>

          <v-list-item
            v-if="
              user != undefined && user.testStatus.toUpperCase() == 'FINISH'
            "
          >
            <v-list-item-title
              ><router-link
                :exact="true"
                to="/datings"
                tag="p"
                class="mb-0 pointer"
                >Знакомства</router-link
              ></v-list-item-title
            >
          </v-list-item>

          <!-- <v-list-item
            v-if="
              user != undefined && user.testStatus.toUpperCase() == 'FINISH'
            "
          >
            <v-list-item-title
              ><router-link
                :exact="true"
                to="/chat"
                tag="p"
                class="mb-0 pointer"
                >Чаты</router-link
              ></v-list-item-title
            >
          </v-list-item> -->

          <v-list-item v-if="user != undefined && user.watchOnBoarding">
            <v-list-item-title
              ><router-link
                :exact="true"
                to="/account"
                tag="p"
                class="mb-0 pointer"
                >Профиль</router-link
              ></v-list-item-title
            >
          </v-list-item>

          <v-list-item
            v-if="
              user != undefined &&
              user.watchOnBoarding &&
              user.partnerType &&
              user.purposeMeet &&
              user.numberFotoHistoryByFelling
            "
          >
            <v-list-item-title
              ><router-link
                :exact="true"
                to="/aims_account"
                tag="p"
                class="mb-0 pointer"
                >Цели</router-link
              ></v-list-item-title
            >
          </v-list-item>

          <v-list-item>
            <v-list-item-title
              ><p class="mb-0 pointer" @click="dialog = true">
                Выйти
              </p></v-list-item-title
            >
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-title class="lightBlue pa-4 pr-12 custom-relative">
          <h4>Выйти из аккаунта</h4>
          <v-icon
            @click="dialog = false"
            color="#013351"
            class="custom-absolute d-flex justify-end cross"
            >mdi-close</v-icon
          >
        </v-card-title>

        <v-card-text class="pa-4">
          <p class="mb-0">Вы уверены, что хотите выйти из аккаунта?</p>
        </v-card-text>

        <v-card-actions class="pb-4">
          <v-btn
            color="colorOfSea"
            class="my-button wide-padding white--text"
            large
            @click="
              logOut();
              dialog = false;
            "
            >Выйти</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>
import { USER_INFO_FOR_HEADER } from "@/graphql/user_queries.js";
import AppLoader from "@/components/global/AppLoader.vue";

export default {
  name: "Home",
  components: {
    AppLoader
  },
  apollo: {
    user: {
      query: USER_INFO_FOR_HEADER,
      variables() {
        return { userId: this.$store.getters.user_id };
      }
    }
  },
  data: () => ({
    dialog: false,
    drawer: false,
    group: false,
    name: "Иван"
  }),
  methods: {
    routerToHome() {
      if (this.$route.path != "/") {
        this.$router.push({ path: "/" });
      }
    },
    logOut() {
      this.$store.dispatch("LOG_OUT").then(
        () => {
          this.$router.push("/login");
        },
        err => {
          console.log(err);
        }
      );
    }
  }
};
</script>
<style lang="scss" scoped>
.width-logo {
  width: 10rem;
}

div.v-menu__content {
  top: 53px !important;
}
.custom-img {
  width: unset;
}
p.custom-menu-link {
  width: auto;
  position: relative;
}
p.custom-menu-link:after {
  display: block;
  position: absolute;
  left: 0;
  width: 0px;
  height: 1px;
  background-color: var(--v-darkBlue-base);
  content: "";
  transition: width 0.3s ease-out;
}
p.custom-menu-link:hover:after {
  width: 100%;
}

.custom-relative {
  position: relative;
}

.custom-absolute {
  width: 100%;
  height: 100%;
  position: absolute !important;
  &.cross {
    width: auto;
    right: 16px;
  }
}

.p-0-imp {
  padding: 0 !important;
  margin-left: 0px;
  margin-right: 0px;
  max-width: 100vw;
}
</style>
