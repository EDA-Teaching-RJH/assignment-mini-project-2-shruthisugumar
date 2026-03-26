from quiz import QuizGame

quiz = QuizGame("question.txt")
quiz.load_questions()
print("Questions loaded:", len(quiz.questions))