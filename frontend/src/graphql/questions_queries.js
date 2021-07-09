import gql from "graphql-tag";

export const QUESTION_GROUP = gql`
  query ($questionGroupId: ID!) {
    questionGroup(questionGroupId: $questionGroupId) {
      id
      orderNumber
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
          answerValue
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
