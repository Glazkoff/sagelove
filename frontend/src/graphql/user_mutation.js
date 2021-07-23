import gql from "graphql-tag";

// Запрос на редактирование поля "Обо мне" пользователя в личном кабинете
export const EDIT_ABOUT_ME = gql`
  mutation ($userId: ID!, $aboutMe: String!) {
    updateUserInformation(userId: $userId, aboutMe: $aboutMe) {
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
