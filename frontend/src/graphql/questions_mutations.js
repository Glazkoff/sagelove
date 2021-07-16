import gql from "graphql-tag";

// Запрос на редактирование поля "Обо мне" пользователя в личном кабинете
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
        }
        questionWithOption {
          id
        }
      }
    }
  }
`;
