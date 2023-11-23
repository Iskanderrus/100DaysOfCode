from data import question_data
from models import Question, Quiz


questions_data = question_data
score = 0
questions = [Question(question=question['text'], correct_answer=question['answer']) for question in questions_data]

for x in range(len(questions)):
    quiz = Quiz(questions_list=questions)
    quiz.chose_question()
    quiz.ask_user()
    score += quiz.assessment()
print(f'You score {score} correct answers out of {len(question_data)}')