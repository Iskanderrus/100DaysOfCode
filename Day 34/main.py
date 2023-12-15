import requests

from data import get_questions
from models import Question, Quiz

questions = get_questions()
score = 0
questions_bank = [Question(question=question['question'],
                           correct_answer=question['correct_answer'])
                  for question in questions]

for x in range(len(questions_bank)):
    quiz = Quiz(questions_list=questions_bank)
    quiz.chose_question()
    print(f'Question {x + 1}:', end=' ')
    quiz.ask_user()
    score += quiz.assessment()

print('*' * 50)
if score == 1:
    print(f'You score {score} correct answer', end=' ')
else:
    print(f'You score {score} correct answers', end=' ')
print(f'out of {len(questions)}')
