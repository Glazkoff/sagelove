<template>
  <v-layout align-center="align-center" justify-center="justify-center">
    <v-flex class="text-center width-window">
      <h1 class="title mb-5 mt-5 mb-sm-10 mt-sm-10">Ваши результаты</h1>
      <p>
        {{ textResultTest }}
      </p>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: "TestResult",
  data() {
    return {
      textResultTest:
        "Вы смелы и решительны. Вы можете принимать решения в зависимости от ситуации: то завоевать весь мир, то бросить все дела и переключить внимание на что-то очень важное. Вы не боитесь общественного мнения, у Вас есть свое мнение на любой счет."
    };
  }
};
</script>

<style lang="scss" scoped></style>
