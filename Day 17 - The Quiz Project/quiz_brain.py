class QuizeBrain:
    def __init__(self, q_list):
        self.number_questions = 0
        self.number_of_correct=0
        self.questions_list = q_list

    def Still_Has_Question(self):
        return self.number_questions < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.number_questions]
        self.number_questions += 1
        user_answer = input(f"Q. {self.number_questions} : {current_question.text} (True / False) :").capitalize()
        correct_answer = current_question.answer
        self.chack_answer(user_answer, correct_answer)

    def chack_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print('You got it right')
            self.number_of_correct += 1
        else:
            print("that's wrong.")
        print(f'the correct answer was : {correct_answer}')
        print(f"you current score is {self.number_of_correct} / {self.number_questions}")
        print('\n')



