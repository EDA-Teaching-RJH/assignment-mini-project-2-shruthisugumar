class Question:
    def __init__(self, song, question, options, answer):

        self.song = song
        self.question = question
        self.options = options
        self.answer = answer

    def display(self):

        print("\n" + self.options)
        
        for option in self.options:
            print(option)