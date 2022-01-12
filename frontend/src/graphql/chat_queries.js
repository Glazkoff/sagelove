import gql from "graphql-tag";

// Список чатов пользователя
export const CHATS_FOR_USER = gql`
  query ($userId: ID!) {
    chatsForUser(userId: $userId) {
      id
      numberMessagesWhichAreNotRead
      user1 {
        id
        firstName
        photo
      }
      user2 {
        id
        firstName
        photo
      }
    }
  }
`;

// Список сообщений в конкретном чате
export const MESSAGES_FOR_CHAT = gql`
  query ($chatId: ID!, $first: Int, $skip: Int, $last: Int) {
    messagesForChat(chatId: $chatId, first: $first, skip: $skip, last: $last) {
      id
      messageText
      messageCheck
      messageAuthor {
        id
        firstName
      }
      createdAt
    }
  }
`;

// Данные о конкретном чате
export const CHAT = gql`
  query ($chatId: ID!) {
    chat(chatId: $chatId) {
      id
      user1 {
        id
        firstName
        photo
      }
      user2 {
        id
        firstName
        photo
      }
    }
  }
`;
