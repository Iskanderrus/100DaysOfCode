import distutils
from random import choice


class Question:
    """ A model to create a question using text of the question and the correct answer containing in the resource
    data"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer


class Quiz:
    def __init__(self, questions_list):
        self.score = 0
        self.question_number = 0
        self.question = None
        self.user_respond = None
        self.questions = questions_list

    def chose_question(self):
        """ Function to select a question from the list of question models """
        while self.question_number < len(self.questions) - 1:
            self.question = self.questions[self.question_number]
            return self.question.question, self.question.correct_answer

    def assessment(self):
        """ Function to make assessment of the provided answer. Counts score. """
        if self.question.correct_answer == self.user_respond:
            self.score += 1
            return True
