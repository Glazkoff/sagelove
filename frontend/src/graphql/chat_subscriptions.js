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

//Удаление чата
export const CHAT_DELETED = gql`
  subscription ($chatId: ID!) {
    chatDeleted(id: $chatId) {
      id
    }
  }
`;
