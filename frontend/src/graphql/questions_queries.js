import gql from "graphql-tag";

export const QUESTION_GROUP = gql`
  query ($questionGroupOrder: ID!) {
    questionGroup(questionGroupOrder: $questionGroupOrder) {
      id
      order
      prevGroupOrder
      nextGroupOrder
      nameGroupQuestion
      questionsWithScale {
        id
        questionText
        answerWithScale {
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
  query ($userId: ID!, $questionGroupOrder: ID!) {
    userGroupScaleAnswers(
      userId: $userId
      questionGroupOrder: $questionGroupOrder
    ) {
      id
      answer
      answerScaleLine {
        id
      }
    }
  }
`;

export const USER_GROUP_OPTION_ANSWERS = gql`
  query ($userId: ID!, $questionGroupOrder: ID!) {
    userGroupOptionAnswers(
      userId: $userId
      questionGroupOrder: $questionGroupOrder
    ) {
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
      nextGroupOrder
      order
    }
  }
`;
