import gql from "graphql-tag";

// Список чатов пользователя
export const MESSAGE_CREATED = gql`
  subscription ($chatId: ID!) {
    messageCreated(chatId: $chatId) {
      id
      messageText
      messageCheck
      messageAuthor {
        id
        firstName
        photo
      }
      createdAt
    }
  }
`;
