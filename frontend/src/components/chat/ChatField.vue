<template>
  <v-container
    fluid
    class="h-100 pa-0 d-flex flex-column align-stretch justify-space-between"
  >
    <v-app-bar class="w-100 chat-bar">
      <v-avatar class="mr-4">
        <img
          v-if="chat != undefined"
          :src="
            chat.user2.photo != null && chat.user2.photo != ''
              ? `/media/${chat.user2.photo}`
              : `/media/photo_placeholder.svg`
          "
          alt="Avatar"
        />
        <img v-else src="/media/photo_placeholder.svg" alt="Avatar" />
      </v-avatar>
      <v-toolbar-title v-if="chat != undefined">
        <b>{{ chat.user2 != undefined ? chat.user2.firstName : "" }}</b>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="pink" text>Заблокировать</v-btn>
    </v-app-bar>
    <div class="chat-messages">
      <v-container class="h-100 d-flex flex-column">
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
        <div
          v-for="message in messagesForChat"
          :key="message.id"
          class="message-box w-100"
          :class="{
            'my-message': +message.messageAuthor.id == +userId,
            'companion-message': +message.messageAuthor.id != +userId
          }"
        >
          <div class="message-box-row">
            <div class="message-box-text">
              <v-container>
                <v-row class="mb-1">
                  <v-spacer></v-spacer>
                  <small>{{ message.createdAt }}</small>
                </v-row>
                <v-row>{{ message.messageText }}</v-row>
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
import { MESSAGES_FOR_CHAT, CHAT } from "@/graphql/chat_queries.js";
import { MESSAGE_CREATED } from "@/graphql/chat_subscriptions.js";

export default {
  name: "ChatField",
  components: {
    ChatMessageInput
  },
  apollo: {
    chat: {
      query: CHAT,
      variables() {
        return {
          chatId: this.pickedChatId
        };
      }
    },
    messagesForChat: {
      query: MESSAGES_FOR_CHAT,
      variables() {
        return {
          chatId: this.pickedChatId,
          first: 100,
          skip: 0
        };
      },
      subscribeToMore: {
        document: MESSAGE_CREATED,
        variables() {
          return {
            chatId: this.pickedChatId
          };
        },
        updateQuery: function (previousResult, { subscriptionData }) {
          // Here, return the new result from the previous with the new data
          console.log("previousResult: ", previousResult);
          console.log("subscriptionData: ", subscriptionData);
          if (subscriptionData.errors === null) {
            let findIndex = previousResult.messagesForChat.findIndex(el => {
              return +el.id === +subscriptionData.data.messageCreated;
            });
            console.log("findIndex: ", findIndex);
            console.log(
              "subscriptionData.data.messageCreated.messageAuthor.id: ",
              subscriptionData.data.messageCreated.messageAuthor.id
            );
            console.log("this.userId: ", this.userId);

            if (
              findIndex == -1 &&
              +subscriptionData.data.messageCreated.messageAuthor.id !==
                +this.userId
            ) {
              // TODO: добавить проверку на сообщение самого пользователя и исправить дубли
              // if (findIndex == -1) {
              previousResult.messagesForChat.push(
                subscriptionData.data.messageCreated
              );
            }
          }
          return previousResult;
        }
      }
    }
  },
  computed: {
    pickedChatId() {
      return this.$store.state.pickedChatId;
    },
    userId() {
      return this.$store.getters.user_id;
    }
  },
  watch: {
    messagesForChat() {
      setTimeout(() => {
        let chatMessages = document.querySelector(".chat-messages");
        chatMessages.visibility = "hidden";
        this.scrollToLastMessage();
        chatMessages.visibility = "visible";
      }, 100);
    }
  },
  methods: {
    scrollToLastMessage() {
      let chatMessages = document.querySelector(".chat-messages");
      chatMessages.scrollTo({
        top: chatMessages.scrollHeight,
        left: 0,
        behavior: "smooth"
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.chat-bar {
  max-height: 64px;
}
.chat-messages {
  height: calc(100vh - 140px - 128px);
  overflow-y: auto;
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
