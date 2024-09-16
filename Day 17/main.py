from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dict in question_data :
    question_text = dict['text']
    question_answer = dict['answer']
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question() :
    quiz.next_question()


print('\n\n\nYou have completed the quiz')
print(f'Your final score is : {quiz.score}/{quiz.question_number}' )
