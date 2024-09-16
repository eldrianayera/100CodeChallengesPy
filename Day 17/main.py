from question_model import Question
from data import question_data

question_bank = []

for dict in question_data :
    question_text = dict['text']
    question_answer = dict['answer']
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

