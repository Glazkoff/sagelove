import gql from "graphql-tag";

// Запрос на редактирование поля "Обо мне" пользователя в личном кабинете
export const EDIT_ABOUT_ME = gql`
  mutation ($userId: ID!, $aboutMe: String!) {
    updateUserInformation(userId: $userId, aboutMe: $aboutMe) {
      ok
    }
  }
`;

//Изменение статуса просмотра on-boarding
export const UPDATE_WATCH_ON_BOARDING = gql`
  mutation ($userId: ID!, $watchOnBoarding: Boolean!) {
    updateWatchOnBoarding(userId: $userId, watchOnBoarding: $watchOnBoarding) {
      user {
        id
        watchOnBoarding
      }
    }
  }
`;

//Общая мутация, которая используется при:
//Создании целей у пользователя при регистрации;
//Изменении целей в кабинете пользователя;
export const UPDATE_USER_AIMS = gql`
  mutation (
    $partnerType: String!
    $purposeMeet: String!
    $numberFotoHistoryByFelling: Int!
    $userId: ID!
  ) {
    updateAimsForUser(
      aimsData: {
        partnerType: $partnerType
        purposeMeet: $purposeMeet
        numberFotoHistoryByFelling: $numberFotoHistoryByFelling
        userId: $userId
      }
    ) {
      user {
        partnerType
        purposeMeet
        numberFotoHistoryByFelling
      }
    }
  }
`;

// Обновление статуса прохождения теста пользователем
export const UPDATE_USER_TEST_STATUS = gql`
  mutation ($testStatus: String!, $userId: ID!) {
    updateUserTestStatus(testStatus: $testStatus, userId: $userId) {
      user {
        id
        testStatus
      }
    }
  }
`;
