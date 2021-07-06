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
