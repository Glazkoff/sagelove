<template>
  <v-container fluid style="padding: 0" class="h-100">
    <v-row class="h-100" no-gutters>
      <v-col cols="3" class="h-100 scrollable">
        <ChatsList></ChatsList>
      </v-col>
      <v-col cols="9" class="h-100">
        <ChatField></ChatField>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ChatsList from "@/components/chat/ChatsList.vue";
import ChatField from "@/components/chat/ChatField.vue";

export default {
  name: "Chat",
  components: {
    ChatsList,
    ChatField
  }
};
</script>

<style lang="scss" scoped>
.scrollable {
  overflow-y: scroll;
  max-height: calc(100vh - 64px);
}
</style>
