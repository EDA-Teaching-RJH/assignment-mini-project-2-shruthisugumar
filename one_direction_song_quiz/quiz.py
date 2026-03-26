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