from quiz import QuizGame

quiz = QuizGame("questions.txt")
quiz.load_questions()

while True:
    print("\nWelcome to the One Direction Quiz Game")
    print("1. Start")
    print("2. Resume Game")
    print("3. Restart Game")
    print("4. Exit")
    choice = input("Choose from Menu 1-4:")

    if choice == "1":
        quiz.start_quiz()
    elif choice == "2":
        quiz.resume_quiz()
    elif choice == "3":
        quiz.restart_quiz()
    elif choice == "4":
        break
