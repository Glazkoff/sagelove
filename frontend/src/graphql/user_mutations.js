import gql from "graphql-tag";

// Запрос на редактирование поля "Обо мне" пользователя в личном кабинете
export const EDIT_ABOUT_ME = gql`
  mutation ($userId: ID!, $aboutMe: String!, $photo: Upload) {
    updateUserInformation(userId: $userId, aboutMe: $aboutMe, photo: $photo) {
      ok
    }
  }
`;

// Обновление статуса просмотра поздравления о прохождении тестировании пользователем
export const UPDATE_USER_CONGRATULATIONS_STATUS = gql`
  mutation ($congratulationsAfterTest: Boolean!, $userId: ID!) {
    updateUserCongratulationStatus(
      congratulationsAfterTest: $congratulationsAfterTest
      userId: $userId
    ) {
      user {
        id
        congratulationsAfterTest
      }
    }
  }
`;

//  Обновление результатов по тесту и сведений об оплате
export const UPDATE_USER_TEST_RESULT_DEMO = gql`
  mutation ($testResultDemo: String!, $userId: ID!) {
    updateUserTestResultDemo(testResultDemo: $testResultDemo, userId: $userId) {
      user {
        id
        testResultDemo
      }
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

export const SET_USER_PHOTO = gql`
  mutation ($userId: ID!, $photo: Upload!) {
    setUserPhotoMutation(userId: $userId, photo: $photo) {
      user {
        id
        photo
      }
    }
  }
`;
