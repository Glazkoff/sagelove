import gql from "graphql-tag";

//  Заблокировать метч
export const BLOCK_USER_MATCH = gql`
  mutation ($user1: ID!, $user2: ID!) {
    blockUserMatch(user1: $user1, user2: $user2) {
      ok
    }
  }
`;

//  Поиск партеров по всем плгоритмам
export const CREATE_DATINGS_ALGORITHMS = gql`
  mutation ($userFirst: ID!) {
    createDatingsAlgorithmFirst(userFirst: $userFirst) {
      ok
      countMatch
    }
    createDatingsAlgorithmSecond(userFirst: $userFirst) {
      ok
      countMatch
    }
    createDatingsAlgorithmThird(userFirst: $userFirst) {
      ok
      countMatch
    }
    createDatingsAlgorithmFourth(userFirst: $userFirst) {
      ok
      countMatch
    }
  }
`;

//  Поиск партеров по первому алгоритму
export const CREATE_DATINGS_ALGORITHM_FIRST = gql`
  mutation ($userFirst: ID!) {
    createDatingsAlgorithmFirst(userFirst: $userFirst) {
      ok
      countMatch
    }
  }
`;

//  Поиск партеров по второму алгоритму
export const CREATE_DATINGS_ALGORITHM_SECOND = gql`
  mutation ($userFirst: ID!) {
    createDatingsAlgorithmSecond(userFirst: $userFirst) {
      ok
      countMatch
    }
  }
`;

//  Поиск партеров по третьему алгоритму
export const CREATE_DATINGS_ALGORITHM_THIRD = gql`
  mutation ($userFirst: ID!) {
    createDatingsAlgorithmThird(userFirst: $userFirst) {
      ok
      countMatch
    }
  }
`;

//  Поиск партеров по истории по ощущениям
export const CREATE_DATINGS_ALGORITHM_FOURTH = gql`
  mutation ($userFirst: ID!) {
    createDatingsAlgorithmFourth(userFirst: $userFirst) {
      ok
      countMatch
    }
  }
`;
