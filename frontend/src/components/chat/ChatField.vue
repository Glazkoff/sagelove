<template>
  <v-container
    fluid
    class="h-100 pa-0 d-flex flex-column align-stretch justify-space-between"
  >
    <v-app-bar class="w-100 chat-bar">
      <v-avatar class="mr-4">
        <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="Avatar" />
      </v-avatar>
      <v-toolbar-title><b>Алина</b></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="pink" text>Заблокировать</v-btn>
    </v-app-bar>
    <div class="chat-messages">
      <v-container>
        <div class="message-box w-100 companion-message">
          <div class="message-box-row">
            <div class="message-box-text">
              <v-container>
                <v-row class="mb-1">
                  <v-spacer></v-spacer>
                  <small>22:17</small>
                </v-row>
                <v-row> Привет 😋 </v-row>
              </v-container>
            </div>
          </div>
        </div>
        <div class="message-box w-100 my-message">
          <div class="message-box-row">
            <div class="message-box-text">
              <v-container>
                <v-row class="mb-1">
                  <v-spacer></v-spacer>
                  <small>22:18</small>
                </v-row>
                <v-row> Привет 😍 </v-row>
              </v-container>
            </div>
          </div>
        </div>
        <div class="message-box w-100 my-message">
          <div class="message-box-row">
            <div class="message-box-text">
              <v-container>
                <v-row class="mb-1">
                  <v-spacer></v-spacer>
                  <small>22:18</small>
                </v-row>
                <v-row> Как дела? </v-row>
              </v-container>
            </div>
          </div>
        </div>
      </v-container>
    </div>
    <div>
      <ChatMessageInput></ChatMessageInput>
    </div>
  </v-container>
</template>

<script>
import ChatMessageInput from "./ChatMessageInput.vue";

export default {
  name: "ChatField",
  components: {
    ChatMessageInput
  }
};
</script>

<style lang="scss" scoped>
.chat-bar {
  max-height: 64px;
}
.chat-messages {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}
.message-box {
  .row + .row {
    margin-top: 0px;
  }
  &-row {
    width: 100%;
    display: flex;
    flex-direction: row;
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
  }
  &.my-message &-row {
    justify-content: flex-end;
  }
  &-text {
    background: #c8f5fa;
    max-width: 300px;
    padding: 0.5rem 1rem;
    -webkit-border-radius: 8px;
    -moz-border-radius: 8px;
    border-radius: 8px;

    & small {
      font-size: 70%;
    }
  }
  .companion-message &-text {
    -webkit-border-bottom-left-radius: 0;
    -moz-border-radius-bottomleft: 0;
    border-bottom-left-radius: 0;
  }
  .my-message &-text {
    -webkit-border-bottom-right-radius: 0;
    -moz-border-radius-bottomright: 0;
    border-bottom-right-radius: 0;
  }
}
</style>
