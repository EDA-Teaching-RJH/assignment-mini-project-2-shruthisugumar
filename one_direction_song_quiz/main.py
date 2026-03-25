from quiz import QuizGame

quiz = QuizGame("questions.txt")
quiz.load_questions()
print("Questions loaded:", len(quiz.questions))