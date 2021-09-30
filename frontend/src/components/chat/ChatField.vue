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
      <v-btn color="pink" text @click="dialog = true">Заблокировать</v-btn>
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
                  <small>{{ formatDate(message.createdAt) }}</small>
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
    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-title class="lightBlue pa-4 pr-12 custom-relative">
          <h4>Заблокировать пользователя</h4>
          <v-icon
            @click="dialog = false"
            color="#013351"
            class="custom-absolute d-flex justify-end cross"
            >mdi-close</v-icon
          >
        </v-card-title>

        <v-card-text class="pa-4">
          <p class="mb-0">
            Вы уверены, что хотите заблокировать пользователя? После блокировки
            вы не сможете отправлять сообщения пользователю "{{
              chat.user2 != undefined ? chat.user2.firstName : ""
            }}"
          </p>
        </v-card-text>

        <v-card-actions class="pb-4">
          <v-btn
            color="colorOfSea"
            class="my-button wide-padding white--text"
            large
            @click="onBlock()"
            >Заблокировать</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import ChatMessageInput from "./ChatMessageInput.vue";
import { MESSAGES_FOR_CHAT, CHAT } from "@/graphql/chat_queries.js";
import { MESSAGE_CREATED } from "@/graphql/chat_subscriptions.js";
import { BLOCK_USER_MATCH } from "@/graphql/accounts_mutations.js";
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
          if (subscriptionData.errors === null) {
            let findIndex = previousResult.messagesForChat.findIndex(el => {
              return +el.id === +subscriptionData.data.messageCreated.id;
            });

            if (
              findIndex == -1 &&
              +subscriptionData.data.messageCreated.messageAuthor.id !==
                +this.userId
            ) {
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
  data() {
    return {
      dialog: false
    };
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
    },
    onBlock() {
      this.$apollo
        .mutate({
          mutation: BLOCK_USER_MATCH,
          variables: {
            user2: this.chat.user2.id,
            user1: this.userId
          }
        })
        .then(() => {
          this.dialog = false;
        })
        .catch(err => {
          console.log(err);
        });
    },
    two(num) {
      return ("0" + num).slice(-2);
    },
    formatDate(date_time) {
      if (!date_time) return null;
      //now_day_time - дата и время сегодня в конкретный момент (29.09.21 23:16:58)
      const now_day_time = new Date();
      //today - дата сегодня в полночь (29.09.21 00:00:00)
      const today = now_day_time.setHours(0, 0, 0, 0);
      //time_zone - зона пользователя
      const time_zone = Number(new Date().getTimezoneOffset());
      // date_in_milisecond - дата в миллисекундах, посчитанная в time zone пользователя
      const date_in_milisecond =
        new Date(date_time).valueOf() - time_zone * 60 * 1000;
      // date - date_in_milisecond в привычном для даты виде (29.09.21 23:16:58)
      const date = new Date(date_in_milisecond);
      // date_zero - date в полночь (29.09.21 00:00:00)
      const date_zero = new Date(
        date.setFullYear(
          date.getUTCFullYear(),
          date.getUTCMonth(),
          date.getUTCDate()
        )
      ).setHours(0, 0, 0, 0);
      //если дата сообщения в полночь равна нынешнему дню в полночь, возвращать только время
      if (date_zero == today) {
        return (
          this.two(date.getUTCHours()) + ":" + this.two(date.getUTCMinutes())
        );
      } else {
        return (
          this.two(date.getUTCDate()) +
          "." +
          this.two(date.getUTCMonth() + 1) +
          "." +
          date.getUTCFullYear() +
          " " +
          this.two(date.getUTCHours()) +
          ":" +
          this.two(date.getUTCMinutes())
        );
      }

      // const now = new Date();
      // const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
      // const [date, time_bad] = date_time.split("T");
      // const [year, month, day] = date.split("-");
      // const [time] = time_bad.split(".");
      // const date_format = new Date(year, month, day);
      // if (date_format == today) {
      //   return time;
      // } else {
      //   // return `${day}.${month}.${year}` + " " + time;
      //   return time_zone;
      //   //1632949200000
      //   // return today;
      //   //1635454800000
      //   // return date_format;
      // }
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
</style>
