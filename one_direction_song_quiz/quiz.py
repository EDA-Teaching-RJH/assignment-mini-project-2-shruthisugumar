import re
import random 
import question import Question 

class QuizGame:
    def __init__(self, filename):

    self.filename = filename
    self.questions = []
    self.score = 0 
    self.curent_question_index = 0

    def load_questions(self):
        with open(self.filename, "r") as file:
            
            for line in file:
                song, question, options, answer = line.strip().split("|")
                options_list = options.split(",")
                q = Question(song, question, options_list, answer)
                self.questions.append(q)

    def check_answer(self, user_answer, correct_answer):
        pattern = r"^[abcABC]$"
        if not re.match(pattern,user_answer):
            print("Enter a, b or c")
            return False
        return user_answer.lower() == correct_answer
    
    def start_quiz(self):
        random.shuffle(self.questions)
        self.score = 0 
        self.current_question_index = 0
        self ask_questions()

    def ask_questions(self):
        while self.current_question_index < len(self.questions):
            q = self.questions[self.current_question_index]
            q.display()
            print("(type pause to stop quiz)")
            user_answer = input("answer: ")
            if user_answer.lower() == "pause":
                self.save_progress()
                print("Quiz Paused.")
                return
            if self.check_answer(user_answer, q.answer):
                print("Correct!")
                self.score += 1
            else: 
                print("Incorrect :(")
            self.current_question_index +=1
        print("Your final score:", self.score)
        self.save_score()

    def save_score(self):
        with open("results.txt", "a") as f:
            f.write(str(self.score) + "\n")
        
    def save_progress(self):
        with open("progress.txt", "w") as f:
            f.write(str(self.current_question_index) + "," + str(self.score))

    def resume_quiz(self): 
        with open("progress.txt", "r") as f: 
            data = f.read().split(",")
            self.current_question_index = int(data[0])
            self.score = int(data[1])
        self.ask_questions()
            