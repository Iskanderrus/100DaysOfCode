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
        self.question = None
        self.user_respond = None
        self.questions = questions_list

    def chose_question(self):
        """ Function to select a question from the list of question models """
        self.question = choice(self.questions)
        self.questions.remove(self.question)
        question_text = self.question.question
        return question_text

    def ask_user(self):
        """ Function to ask a question by requesting user to prompt 't' for True or 'f' for False
        :return boolean value or a warning message
        """
        print(self.question.question)
        user_respond = input("Is it True or False? (t/f):\n")
        if user_respond.strip().lower() == 't':
            self.user_respond = True
        elif user_respond.strip().lower() == 'f':
            self.user_respond = False
        else:
            self.user_respond = 'Wrong entry.'
        return self.user_respond

    def assessment(self):
        """ Function to make assessment of the provided answer. Counts score. """
        if self.user_respond == 'Wrong entry.':
            print('You provided not a valid respond. Try again.')
            self.questions.append(self.question)
            return 0
        elif distutils.util.strtobool(self.question.correct_answer) == self.user_respond:
            print(f'You are right! Correct answer is: {self.question.correct_answer}\n')
            return 1
        else:
            print(f'Sorry. That\'s wrong. Correct answer is: {self.question.correct_answer}\n')
            return 0
