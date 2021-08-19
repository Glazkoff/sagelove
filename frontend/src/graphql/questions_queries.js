import gql from "graphql-tag";

export const QUESTION_GROUP = gql`
  query ($questionGroupOrder: ID!) {
    questionGroup(questionGroupOrder: $questionGroupOrder) {
      id
      order
      prevGroupId
      nextGroupId
      nameGroupQuestion
      questionwithscaleSet {
        id
        questionText
        answerscaleSet {
          id
          leftAnswerText
          rightAnswerText
        }
      }
      questionwithoptionSet {
        id
        questionText
        answeroptionSet {
          id
          answerText
        }
      }
    }
  }
`;

export const QUESTION_GROUP_COUNT = gql`
  {
    questionGroupsCount
  }
`;

export const USER_GROUP_SCALE_ANSWERS = gql`
  query ($userId: ID!, $groupId: ID!) {
    userGroupScaleAnswers(userId: $userId, groupId: $groupId) {
      id
      answer
      answerScaleLine {
        id
      }
    }
  }
`;

export const USER_GROUP_OPTION_ANSWERS = gql`
  query ($userId: ID!, $groupId: ID!) {
    userGroupOptionAnswers(userId: $userId, groupId: $groupId) {
      id
      answer {
        id
      }
      questionWithOption {
        id
      }
    }
  }
`;

export const USER_LAST_GROUP = gql`
  query ($userId: ID!) {
    userLastGroup(userId: $userId) {
      id
      nextGroupId
      order
    }
  }
`;
