import gql from "graphql-tag";

// Все метчи пользователя
export const MATCHES_FOR_USER = gql`
  query ($userId: ID!) {
    matchForUser(userId: $userId) {
      id
      user1 {
        id
        firstName
        photo
        dateOfBirth
      }
      user2 {
        id
        firstName
        photo
        dateOfBirth
      }
      blocked
      algorithm
    }
  }
`;
