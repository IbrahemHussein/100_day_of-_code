from question_model import Question
from data import question_data
from quiz_brain import QuizeBrain

question_bank = []
for question in question_data:
    text = question.get('text')
    answer = question.get('answer')
    new_question = Question(text, answer)
    question_bank.append(new_question)


quize = QuizeBrain(question_bank)
while quize.Still_Has_Question():
    quize.next_question()
print("You've completed the quiz")
print(f"Your final score was : {quize.number_of_correct}/ {len(quize.questions_list)}")

