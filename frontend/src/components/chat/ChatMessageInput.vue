<template>
  <v-container class="d-flex flex-row align-stretch justify-space-between">
    <div class="emoji-wrap">
      <SlideYDownTransition>
        <VEmojiPicker
          class="emoji-picker"
          @select="selectEmoji"
          v-if="emojiPickerShow"
          :i18n="i18n"
          :emojiSize="28"
          :showSearch="false"
          :emojisByRow="5"
          v-on-clickaway="closeEmojiPicker"
        />
      </SlideYDownTransition>
      <v-btn
        icon
        color="colorOfSea"
        @click="emojiPickerShow = !emojiPickerShow"
      >
        <v-icon>mdi-emoticon-happy-outline</v-icon>
      </v-btn>
    </div>
    <form id="chat-form" class="ml-2 mr-2">
      <v-textarea
        outlined
        rows="3"
        placeholder="Введите сообщение..."
        no-resize
        v-model="newMessage"
        ref="messageField"
      ></v-textarea>
    </form>
    <div class="d-flex">
      <v-spacer></v-spacer>
      <v-btn dark color="colorOfSea">Отправить</v-btn>
    </div>
  </v-container>
</template>

<script>
import { VEmojiPicker } from "v-emoji-picker";
import { mixin as clickaway } from "vue-clickaway";
import { SlideYDownTransition } from "vue2-transitions";

const i18n = {
  search: "Поиск...",
  categories: {
    Activity: "Активности",
    Flags: "Флаги",
    Foods: "Еда",
    Frequently: "Недавнее",
    Objects: "Объекты",
    Nature: "Природа",
    Peoples: "Люди",
    Symbols: "Символы",
    Places: "Места"
  }
};

export default {
  name: "ChatMessageInput",
  mixins: [clickaway],
  components: {
    VEmojiPicker,
    SlideYDownTransition
  },
  data() {
    return {
      emojiPickerShow: false,
      newMessage: "",
      i18n
    };
  },
  methods: {
    selectEmoji(emoji) {
      let input = this.$refs.messageField.$refs.input;
      let curPos = input.selectionStart;
      this.newMessage =
        this.newMessage.slice(0, curPos) +
        emoji.data +
        this.newMessage.slice(curPos);
      let selectionStart;
      let selectionEnd;
      selectionStart = selectionEnd = curPos + emoji.data.length;
      if (input.setSelectionRange) {
        console.log(input.setSelectionRange(selectionStart, selectionEnd + 2));
        input.focus();
        input.setSelectionRange(selectionStart, selectionEnd + 2);
      } else if (input.createTextRange) {
        var range = input.createTextRange();
        range.collapse(true);
        range.moveEnd("character", selectionEnd);
        range.moveStart("character", selectionStart);
        range.select();
      }
      this.closeEmojiPicker();
    },
    closeEmojiPicker() {
      this.emojiPickerShow = false;
    }
  }
};
</script>

<style lang="scss" scoped>
#chat-form {
  width: 100%;
}
.emoji-wrap {
  position: relative;
  .emoji-picker {
    position: absolute;
    bottom: 110%;
    left: 0;
  }
}
#InputSearch {
  display: none !important;
}
</style>
