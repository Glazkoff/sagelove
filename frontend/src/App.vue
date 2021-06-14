<template>
  <div id="app">
    <router-view />
  </div>
</template>

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

button.v-btn,
a.v-btn {
  text-transform: none !important;
  border-radius: 5px;
  height: 36px !important;
  padding: 0 37px !important;
  font-size: 14px !important;
}

h1.title,
.v-application h1.title {
  color: var(--v-darkBlue-base);
  font-style: normal !important;
  font-weight: normal !important;
  font-size: 48px !important;
  line-height: 55px !important;
}

button.theme--light.v-btn.v-btn--disabled.v-btn--has-bg,
a.theme--light.v-btn.v-btn--disabled.v-btn--has-bg {
  background-color: #c8f5fa !important;
  color: #fff !important;
}

a.link{
  text-decoration: none;
  color: #FF618C !important;
  font-weight: 700;
}
</style>
