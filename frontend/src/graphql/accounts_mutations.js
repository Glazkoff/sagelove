import gql from "graphql-tag";

//  Заблокировать метч
export const BLOCK_USER_MATCH = gql`
  mutation ($user1: ID!, $user2: ID!) {
    blockUserMatch(user1: $user1, user2: $user2) {
      ok
    }
  }
`;
