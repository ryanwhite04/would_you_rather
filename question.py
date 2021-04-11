from textwrap import shorten, dedent
class Question:

    def __init__(self, option_1, option_2, mature=False, votes_1=0, votes_2=0):
        self.option_1 = option_1
        self.option_2 = option_2
        self.mature = mature
        self.votes_1 = votes_1
        self.votes_2 = votes_2

    def __contains__(self, query):
        return query in self.option_1 or query in self.option_2

    def __repl__(self):
        divisive = "This question is divisive!\n" if self.divisive else ""
        answered = "" if self.answered else "This question has not been answered\n"
        mature = "For mature audiences only\n" if self.mature else ""
        template = """\
            Would you rather...
             1) {self.option_1}?
             2) {self.option_2}?
             
            {answered}{divisive}{mature}Option 1 has {self.votes_1} ({self.ratio_1:.1%}) votes and Option 2 has {self.votes_2} ({self.ratio_1:.1%}) votes
            """
        return dedent(template.format(
                self=self,
                divisive=divisive,
                answered=answered,
                mature=mature))

    def __str__(self):
        def truncate(option):
            return shorten(option + "?", width=40, placeholder="...")
        return f'{truncate(self.option_1)} / {truncate(self.option_1)}'

    def toggle(self):
        self.mature ^= self.mature

    def vote(self, index):
        self.votes[index] += 1

    def to_dict(self):
        keys = ["option_1", "option_2", "mature", "votes_1", "votes_2"]
        return { key: self[key] for key in keys }

    @property
    def votes_total(self):
        return self.votes_1 + self.votes_2

    @property
    def ratio_1(self):
        return self.votes_1/self.votes_total if self.votes_total else 0

    @property
    def ratio_2(self):
        return self.votes_2/self.votes_total

    @property
    def answered(self):
        return self.votes_1 or self.votes_2

    @property
    def divisive(self):
        return self.answered and abs(self.ratio_1 - self.ratio_1) < 0.2

def listQuestions(questions):
    print("List of questions")
    for question in questions:
        print(question)

def viewQuestion(questions, index):
    print(questions[index].__repl__())

def addQuestion(questions, arguments):
    questions.append(Question(**arguments))

def toggleQuestion(questions, index):
    questions[index].toggle()

def deleteQuestion(questions, index):
    del questions[index]

def loadQuestions(path):
    data = load_data(path)
    return [Question(item) for item in data]

def saveQuestions(questions, path):
    save_data(path, [question.to_dict() for question in questions])

def searchQuestions(questions, query):
    # print(f'Questions containing {query}: ')
    for i, question in enumerate(questions):
        if query in q:
            print(f' {i+1}) {q}') 



