import random
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.list_number = 0
        self.question_list = q_list
        self.score = 0
    def still_has_question(self):
        return self.list_number == 5

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.list_number += 1
        random_number = random.randint(0, 11)
        self.question_number = random_number
        user_answer = input(f"Q.{self.list_number}: {current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.list_number}")
        print("\n")