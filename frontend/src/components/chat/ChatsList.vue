<template>
  <v-list subheader>
    <v-subheader>Ваши чаты</v-subheader>
    <v-list-item
      avatar
      v-for="index in 10"
      v-bind:key="index"
      class="chat-list-item"
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
                      src="https://cdn.vuetifyjs.com/images/john.jpg"
                      alt="Avatar"
                    />
                  </v-avatar>
                </v-layout>
              </v-col>
              <v-col class="pl-0 pr-0" cols="8">
                <v-list-item-title class="mb-1">
                  <b>Алина #{{ index }}</b>
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
      <!--  -->
    </v-list-item>
  </v-list>
</template>

<script>
export default {
  name: "ChatsList",
  data() {
    return {
      contactList: {}
    };
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
