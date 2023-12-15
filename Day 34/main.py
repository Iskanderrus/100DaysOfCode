from data import get_questions
from models import Quiz
from ui import QuizInterface

questions_bank = get_questions()
score = 0

quiz = Quiz(questions_list=questions_bank)
ui = QuizInterface(quiz)
