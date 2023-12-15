from data import get_questions
from models import Quiz
from ui import QuizInterface

questions_bank = get_questions()
score = 0

ui = QuizInterface()

for x in range(len(questions_bank)):
    quiz = Quiz(questions_list=questions_bank)
    quiz.chose_question()
    print(f'Question {x + 1}:', end=' ')
    quiz.ask_user()
    score += quiz.assessment()
    QuizInterface.score_label.itemconfig(text=f"Your Score: {score}")

print('*' * 50)
if score == 1:
    print(f'You score {score} correct answer', end=' ')
else:
    print(f'You score {score} correct answers', end=' ')
print(f'out of {len(questions_bank)}')
