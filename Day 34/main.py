import requests

from models import Question, Quiz

amount = int(input('How many questions do you want? Please provide a number in range 10 to 49\n'))
difficulty = input('Select difficulty level: easy, medium or hard\n')
URL = f'https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type=boolean'

respond = requests.get(url=URL)
questions = respond.json()['results']
for question in questions:
    question['question'] = question['question'].replace('&quot;', '"')
    question['question'] = question['question'].replace('&#039;', '\'')

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
