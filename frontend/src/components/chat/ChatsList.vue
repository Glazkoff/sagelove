<template>
  <v-list subheader>
    <v-subheader>Ваши чаты (user #{{ userId }})</v-subheader>
    <div v-if="chatsForUser == null || chatsForUser.length == 0">
      <v-list-item>
        <v-list-item-content>
          Вы ещё не начали ни одного чата
        </v-list-item-content>
      </v-list-item>
    </div>
    <div v-else>
      <v-list-item
        v-for="userChat in chatsForUser"
        v-bind:key="userChat.id"
        class="chat-list-item"
        :style="{
          'background-color':
            userChat.id === pickedChatId ? 'rgba(0,0,0,.1)' : 'rgba(0,0,0,0)'
        }"
        @click="$store.commit('SET_PICKED_CHAT_ID', userChat.id)"
      >
        <v-list-item-content>
          <v-row justify="space-between">
            <v-col cols="10" style="flex-grow: unset">
              <v-row style="flex-wrap: unset">
                <v-col cols="4">
                  <v-layout
                    align-center="align-center"
                    justify-center="justify-center"
                    class="h-100"
                  >
                    <v-avatar>
                      <img
                        :src="
                          userChat.user2.photo != null &&
                          userChat.user2.photo != ''
                            ? `/media/${userChat.user2.photo}`
                            : `/media/photo_placeholder.svg`
                        "
                        alt="Avatar"
                      />
                    </v-avatar>
                  </v-layout>
                </v-col>
                <v-col class="pl-0 pr-0" cols="8">
                  <v-list-item-title class="mb-1">
                    <b>{{ userChat.user2.firstName }}</b>
                  </v-list-item-title>
                  <small>Сокращённый текст последнего сообщения</small>
                </v-col>
              </v-row>
            </v-col>
            <v-col cols="2" style="flex-grow: unset">
              <v-layout
                align-center="align-center"
                justify-center="justify-center"
                class="h-100"
              >
                <v-avatar
                  left
                  color="colorOfSea"
                  class="darken-4 white--text"
                  size="20"
                >
                  1
                </v-avatar>
              </v-layout>
            </v-col>
          </v-row>
        </v-list-item-content>
      </v-list-item>
    </div>
  </v-list>
</template>

<script>
import { CHATS_FOR_USER } from "@/graphql/chat_queries.js";

export default {
  name: "ChatsList",
  data() {
    return {
      contactList: {}
    };
  },
  apollo: {
    chatsForUser: {
      query: CHATS_FOR_USER,
      variables() {
        return { userId: this.userId };
      }
    }
  },
  computed: {
    userId() {
      return this.$store.getters.user_id;
    },
    pickedChatId() {
      return this.$store.state.pickedChatId;
    }
  }
};
</script>

<style lang="scss" scoped>
.chat-list-item {
  cursor: pointer;
  &:hover {
    background-color: rgba(0, 0, 0, 0.2);
  }
}
</style>
