import gql from "graphql-tag";

export const USER_TEST_STATUS = gql`
  query ($userId: ID!) {
    user(userId: $userId) {
      id
      testStatus
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

// Статус просмотра on-boarding
export const WATCH_ON_BOARDING = gql`
  query ($userId: ID!) {
    user(userId: $userId) {
      id
      watchOnBoarding
      partnerType
    }
  }
`;
