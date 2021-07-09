<template>
  <v-layout align-center="align-center" justify-center="justify-center">
    <v-flex class="text-center width-window">
      <h1 v-if="!isPaid" class="title mb-5 mt-5 mb-sm-10 mt-sm-10">
        Поздравляем!
      </h1>
      <h1 v-if="isPaid" class="title mb-5 mt-5 mb-sm-10 mt-sm-10">
        Знакомства
      </h1>
      <p v-if="!isPaid && !wasFound">
        {{ textResultTest }}
      </p>
      <p v-if="!isPaid && !wasFound">
        Дайте нам немного времени и как только наш умный алгоритм просчитает
        совпадение, мы Вас проинформируем. Обычно на это уходит не более 6 часов
      </p>

      <v-row
        class="custom-relative"
        v-if="!isPaid || (isPaid && persons.length == 0)"
      >
        <h2
          v-if="(!isPaid && !wasFound) || (isPaid && persons.length == 0)"
          z-index="11"
          class="
            title
            darkBlue--text
            text-center
            custom-absolute
            d-flex
            justify-center
            align-center
          "
        >
          Совсем скоро мы найдем для вас интересных людей
        </h2>
        <div
          z-index="10"
          v-if="!isPaid && wasFound"
          class="custom-absolute d-flex justify-center align-center flex-column"
        >
          <p class="text-center ml-5 mr-5 ml-sm-12 mr-sm-12">
            Мы нашли варианты интересных людей, которые полностью совпадают с
            твоими критериями поиска, если ты хочешь с ними познакомиться и
            выбрать с кем будешь общаться, внеси клубный взнос в размере
            10000руб
          </p>
          <v-btn
            color="colorOfSea my-button wide-padding"
            dark
            large
            @click="isPaid = true"
            >Оплатить</v-btn
          >
        </div>

        <v-col
          v-for="i in 8"
          :key="i"
          class="
            col-12 col-sm-6
            custom-sceleton
            d-flex
            justify-start
            align-start
            flex-row
          "
        >
          <div class="circle"></div>
          <div class="custom-wrap">
            <div class="line line-title"></div>
            <div class="line line-description"></div>
            <div class="line line-description"></div>
          </div>
        </v-col>
      </v-row>

      <!-- Если оплачено, то показываются профили -->
      <v-row v-if="isPaid && wasFound">
        <v-col
          v-for="person in persons"
          :key="person.id"
          class="
            col-12 col-sm-6
            custom-sceleton
            d-flex
            justify-center
            align-start
            flex-row
            text-left
          "
        >
          <img
            :to="{ name: 'DatingsPerson', params: { id: person.id } }"
            class="custom-img"
            src="https://picsum.photos/200"
            alt="Ававтар"
          />
          <div class="custom-wrap user">
            <p class="font-weight-bold mb-1">
              <router-link
                :to="{ name: 'DatingsPerson', params: { id: person.id } }"
                class="link"
                >{{ person.user_name }}</router-link
              >
            </p>
            <p class="mb-1">{{ countAge(person.user_birthday) }}</p>
            <v-btn color="colorOfSea my-button" dark large>Написать</v-btn>
          </div>
        </v-col>
      </v-row>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: "DatingsStatus",
  data() {
    return {
      isPaid: false,
      wasFound: true,
      persons: [
        { id: 1, user_name: "Иван", user_birthday: "1987-06-15", url_foto: "" },
        {
          id: 2,
          user_name: "Кирилл",
          user_birthday: "1995-03-13",
          url_foto: ""
        },
        {
          id: 3,
          user_name: "Григорий",
          user_birthday: "1997-08-17",
          url_foto: ""
        },
        { id: 4, user_name: "Егор", user_birthday: "2000-12-01", url_foto: "" },
        {
          id: 5,
          user_name: "Никита",
          user_birthday: "1969-02-05",
          url_foto: ""
        },
        {
          id: 6,
          user_name: "Антон",
          user_birthday: "1991-06-25",
          url_foto: ""
        },
        {
          id: 7,
          user_name: "Евгений",
          user_birthday: "1984-04-29",
          url_foto: ""
        },
        {
          id: 8,
          user_name: "Александр",
          user_birthday: "1995-05-05",
          url_foto: ""
        },
        {
          id: 9,
          user_name: "Василий",
          user_birthday: "2001-09-16",
          url_foto: ""
        }
      ],
      textResultTest:
        "Вы смелы и решительны. Вы можете принимать решения в зависимости от ситуации: то завоевать весь мир, то бросить все дела и переключить внимание на что-то очень важное. Вы не боятесь общественного мнения, у Вас есть свое мнение на любой счет."
    };
  },
  methods: {
    countAge(dateString) {
      var today = new Date();
      var birthDate = new Date(dateString);
      var age = today.getFullYear() - birthDate.getFullYear();
      var m = today.getMonth() - birthDate.getMonth();
      if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
      }

      return this.yearsOldWord(age);
    },
    yearsOldWord(age) {
      let txt;
      let count;
      count = age % 100;
      if (count >= 5 && count <= 20) {
        txt = "лет";
      } else {
        count = count % 10;
        if (count == 1) {
          txt = "год";
        } else if (count >= 2 && count <= 4) {
          txt = "года";
        } else {
          txt = "лет";
        }
      }
      return `${age} ${txt}`;
    }
  }
};
</script>

<style lang="scss" scoped>
.width-window {
  max-width: 600px;
}

.custom-relative {
  position: relative;
}

.custom-absolute {
  height: 100%;
  position: absolute;
}
.custom-img {
  width: 80px;
  height: 80px;
  margin-right: 1rem;
  border-radius: 50%;
}

.custom-sceleton {
  & .circle {
    width: 80px;
    height: 80px;
    margin-right: 1rem;
    background-color: var(--v-lightLightBlue-base);
    border-radius: 50%;
  }
  & .custom-wrap {
    margin-top: 1rem;
    &.user {
      margin-top: 0 !important;
    }

    & .line {
      width: 5rem;
      height: 0.75rem;
      border-radius: 1rem;
      background-color: var(--v-lightLightBlue-base);
      margin-bottom: 0.5rem;
      &.line-title {
        margin-bottom: 0.75rem;
      }
      &.line-description {
        min-width: 10rem;
      }
    }
  }
}
@media (max-width: 600px) {
  .custom-sceleton {
    width: 100%;
    & .custom-wrap {
      width: calc(100% - 96px);
      &.user {
        width: auto !important;
      }
      & .line {
        width: 80px;
        &.line-description {
          width: 100%;
        }
      }
    }
  }
}
</style>
