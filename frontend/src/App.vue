<template>
  <v-app>
    <AppLoader v-if="appLoading"></AppLoader>
    <div id="app" v-else>
      <router-view />
    </div>
  </v-app>
</template>

<script>
import AppLoader from "@/components/global/AppLoader.vue";

export default {
  async mounted() {
    let refreshToken = localStorage.getItem("t");
    if (refreshToken !== null) {
      this.$store.commit("START_APP_LOADING");
      this.$store.dispatch("REFRESH_TOKEN").then(
        () => {
          this.$store.commit("STOP_APP_LOADING");
          this.$router.push({ path: this.$store.state.firstPath || "/" });
        },
        errors => {
          this.$store.commit("STOP_APP_LOADING");
          console.log("ERROR: ", errors);
        }
      );
    }
  },
  components: {
    AppLoader
  },
  computed: {
    appLoading() {
      return this.$store.state.loading;
    }
  }
};
</script>

<style lang="scss">
@import "~vuetify/src/styles/styles.sass";

@font-face {
  font-family: "YesevaOne";
  src: url("assets/fonts/YesevaOne-Regular.ttf") format("truetype");
  font-style: normal;
  font-weight: 400;
}

@font-face {
  font-family: "OpenSans";
  src: url("assets/fonts/OpenSans-Regular.ttf") format("truetype");
  font-style: normal;
  font-weight: 400;
}

@font-face {
  font-family: "OpenSans";
  src: url("assets/fonts/OpenSans-Bold.ttf") format("truetype");
  font-style: normal;
  font-weight: 700;
}

@font-face {
  font-family: "OpenSans";
  src: url("assets/fonts/OpenSans-BoldItalic.ttf") format("truetype");
  font-style: italic;
  font-weight: 700;
}

@font-face {
  font-family: "OpenSans";
  src: url("assets/fonts/OpenSans-ExtraBold.ttf") format("truetype");
  font-style: normal;
  font-weight: 800;
}

@font-face {
  font-family: "OpenSans";
  src: url("assets/fonts/OpenSans-ExtraBoldItalic.ttf") format("truetype");
  font-style: italic;
  font-weight: 800;
}

@font-face {
  font-family: "OpenSans";
  src: url("assets/fonts/OpenSans-Italic.ttf") format("truetype");
  font-style: italic;
  font-weight: 400;
}

@font-face {
  font-family: "OpenSans";
  src: url("assets/fonts/OpenSans-Light.ttf") format("truetype");
  font-style: normal;
  font-weight: 200;
}
@font-face {
  font-family: "OpenSans";
  src: url("assets/fonts/OpenSans-LightItalic.ttf") format("truetype");
  font-style: italic;
  font-weight: 200;
}
@font-face {
  font-family: "OpenSans";
  src: url("assets/fonts/OpenSans-SemiBold.ttf") format("truetype");
  font-style: normal;
  font-weight: 600;
}
@font-face {
  font-family: "OpenSans";
  src: url("assets/fonts/OpenSans-SemiBoldItalic.ttf") format("truetype");
  font-style: italic;
  font-weight: 600;
}

$body-font-family: "OpenSans";
$title-font: "YesevaOne";

.v-application {
  font-family: $body-font-family, sans-serif !important;
  h1.title,
  h2.title,
  h3.title,
  h4.title,
  h5.title,
  h6.title {
    font-family: $title-font, sans-serif !important;
  }
}

button.v-btn.my-button,
a.v-btn.my-button {
  text-transform: none !important;
  border-radius: 5px;
  height: 36px !important;
  font-size: 14px !important;
  &.wide-padding {
    padding: 0 37px !important;
  }
}

h1.title,
.v-application h1.title {
  color: var(--v-darkBlue-base);
  font-style: normal !important;
  font-weight: normal !important;
  font-size: 48px !important;
  line-height: 48px !important;
}

button.theme--light.v-btn.v-btn--disabled.v-btn--has-bg,
a.theme--light.v-btn.v-btn--disabled.v-btn--has-bg {
  background-color: #c8f5fa !important;
  color: #fff !important;
}

a.link {
  text-decoration: none;
  color: #ff618c !important;
  font-weight: 700;
}

p {
  color: var(--v-darkBlue-base);
  font-size: 16px !important;
}

h2.title,
.v-application h2.title {
  color: var(--v-darkBlue-base);
  font-style: normal !important;
  font-weight: normal !important;
  font-size: 28px !important;
}

h4,
.v-application h4 {
  color: var(--v-darkBlue-base);
  font-style: normal !important;
  font-weight: normal !important;
  font-size: 20px !important;
}

div.v-application .primary--text {
  color: #00acc2 !important;
  caret-color: #00acc2 !important;
}
div.v-input--selection-controls__input:hover {
  color: #00acc2;
}
div.v-input--selection-controls {
  margin-top: 0px;
  padding-top: 0px;
}

div.v-input__slot {
  margin-bottom: 0px;
}
div.v-carousel div.v-carousel__controls {
  background: rgba(0, 0, 0, 0) !important;
}
button.v-carousel__controls__item {
  color: white !important;
}
button.v-carousel__controls__item .v-icon {
  opacity: 1 !important;
}
button.v-carousel__controls__item span.v-btn__content i.v-icon:active {
  color: #00acc2 !important;
}

.theme--dark.v-btn--active:before,
.theme--dark.v-btn--active:hover:before {
  opacity: 0 !important;
}
.theme--dark.v-btn--active,
.theme--dark.v-btn--active {
  color: #00acc2 !important;
}
div.v-window__container div.v-window__next,
div.v-window__container div.v-window__prev {
  background: rgba(0, 0, 0, 0);
}
div.v-responsive__content.my-carousel {
  position: relative !important;
}
@media (max-width: 600px) {
  h1.title,
  .v-application h1.title {
    font-size: 32px !important;
  }
}
@media (max-width: 465px) {
  div.container div.v-carousel {
    height: 53.75rem !important;
  }
  div.container div.v-carousel div.v-window__container {
    height: 53.75rem !important;
  }
  div.container
    div.v-carousel
    div.v-window__container
    div.v-window-item
    div.v-responsive {
    height: 53.75rem !important;
  }
}
</style>
