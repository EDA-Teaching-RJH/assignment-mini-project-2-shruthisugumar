from questions import Question 

class QuizGame:
    def __init__(self,filename):
        self.filename = filename 
        self.questions = []
        self.score = 0
        self.currentquestion = 0 
    
    def load_questions(self):
        with open(self.filename, "r") as file:
            for line in file:
                song, question, options, answer = line.strip().split("|")
                options_list = options.split(",")
                q = Question(song, question, options_list, answer)
                self.question.append(q)
                                            