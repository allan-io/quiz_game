from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain
question_bank = []

for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz = QuizzBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the Quiz\nYou're final score was: {quiz.score}/{quiz.question_number}")