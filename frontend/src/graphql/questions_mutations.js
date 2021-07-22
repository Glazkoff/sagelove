import gql from "graphql-tag";

// Мутация записи ответа пользователя на вопрос с вариантами
export const CREATE_USER_OPTION_ANSWER = gql`
  mutation ($userId: ID!, $questionId: ID!, $answerId: ID!) {
    createUserOptionAnswer(
      userId: $userId
      questionId: $questionId
      answerId: $answerId
    ) {
      userOptionAnswer {
        id
        answer {
          id
          __typename
        }
        questionWithOption {
          id
          __typename
        }
        __typename
      }
    }
  }
`;

// Мутация записи ответа пользователя на строку вопроса со шкалой
export const CREATE_USER_SCALE_ANSWER = gql`
  mutation ($answer: Int!, $questionRowId: ID!, $userId: ID!) {
    createUserScaleAnswer(
      answer: $answer
      questionRowId: $questionRowId
      userId: $userId
    ) {
      userScaleAnswer {
        id
        answer
        answerScaleLine {
          id
          __typename
        }
        __typename
      }
    }
  }
`;

// Мутация завершения тестирования
export const FINISH_USER_TESTING = gql`
  mutation ($userId: ID!) {
    finishUserTesting(userId: $userId) {
      statusOk
    }
  }
`;
