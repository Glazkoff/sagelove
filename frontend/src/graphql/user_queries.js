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

// Запрос на получение имени  пользователя для шапки
export const USER_NAME = gql`
  query ($userId: ID!) {
    user(userId: $userId) {
      id
      firstName
    }
  }
`;
