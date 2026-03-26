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

    