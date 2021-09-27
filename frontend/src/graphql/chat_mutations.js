import gql from "graphql-tag";

export const CREATE_MESSAGE = gql`
  mutation ($authorId: ID!, $chatId: ID!, $messageText: String!) {
    createMessage(
      authorId: $authorId
      chatId: $chatId
      messageText: $messageText
    ) {
      message {
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
  }
`;
