import gql from "graphql-tag";

export const USER_TEST_STATUS = gql`
  query ($userId: ID!) {
    user(userId: $userId) {
      id
      testStatus
    }
  }
`;

// Статус просмотра поздравления о прохождении тестировании пользователем и
// информация о результатах тестов и об оплате
export const USER_AFTER_TEST_STATUS = gql`
  query ($userId: ID!) {
    user(userId: $userId) {
      id
      congratulationsAfterTest
      testResultDemo
    }
  }
`;

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

// Запрос на получение информации о пользователе для личного кабинета
export const USER_INFORMATION = gql`
  query ($userId: ID!) {
    user(userId: $userId) {
      id
      firstName
      aboutMe
      dateOfBirth
      gender
      photoURL
      phoneNumber
    }
  }
`;

//Получение целей пользователя по id
export const USER_AIMS = gql`
  query ($userId: ID!) {
    user(userId: $userId) {
      id
      partnerType
      purposeMeet
      numberFotoHistoryByFelling
    }
  }
`;

// Запрос на получение имени  пользователя для шапки
export const USER_NAME = gql`
  query ($userId: ID!) {
    user(userId: $userId) {
      id
      firstName
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
