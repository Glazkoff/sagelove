import gql from "graphql-tag";

// Запрос на редактирование поля "Обо мне" пользователя в личном кабинете
export const EDIT_ABOUT_ME = gql`
  mutation ($userId: ID!, $aboutMe: String!) {
    updateUserInformation(userId: $userId, aboutMe: $aboutMe) {
      ok
    }
  }
`;
