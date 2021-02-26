# Name: Ryan White 
# Student Number: 10554949  

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from admin import load_data, save_data

class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("Would you rather")
        self.geometry("600x400")
        self.questions = load_data(onError=self.onInvalidData)
        self.show_mature = messagebox.askyesno(message="Would you like to see mature content")
        if  self.show_mature:
            self.filtered = self.questions
        else:
            self.filtered = [question for question in self.questions if not question['mature']]
        if not len(self.filtered):
            messagebox.showerror(message="There are no questions available")
            self.destroy()
        self.createWidgets() 
        self.question_num = 0
        self.show_question()

    def createWidgets(self):
        self.progress = StringVar()
        self.progressLabel = Label(self, textvariable=self.progress)
        self.progressLabel.pack()
        self.option_1 = StringVar()
        self.option_2 = StringVar()
        self.button_1 = Button(self, textvariable=self.option_1, command=lambda: self.record_vote('votes_1'))
        self.button_2 = Button(self, textvariable=self.option_2, command=lambda: self.record_vote('votes_2'))
        self.button_1.pack()
        self.button_2.pack()
    
    def onInvalidData(self, error):
        messagebox.showerror(title="File Error", message=f'Missing/Invalid file, {error}') and self.destroy()

    def show_question(self):
        if self.question_num < len(self.filtered):
            question = self.filtered[self.question_num]
            self.progress.set(f'Question {self.question_num+1} of {len(self.filtered)}')
            self.option_1.set(question['option_1'])
            self.option_2.set(question['option_2'])
        else:
            messagebox.showinfo(message="Thanks for playing")
            self.destroy()

    def record_vote(self, vote):   
        question = self.filtered[self.question_num]
        question[vote] += 1
        save_data(self.questions)
        self.question_num += 1
        groups = { 
            "votes_1": question["votes_1"] > question["votes_2"],
            "votes_2": question["votes_2"] > question["votes_1"]
        }
        group = "majority" if groups[vote] else "minority"
        messagebox.showinfo(message=f'Your vote was recorded, you are in the {group}!')
        self.show_question()

if __name__ == "__main__":
    # https://docs.python.org/3/library/tkinter.html#a-simple-hello-world-program
    app = App()
    app.mainloop()
# If you have been paid to write this program, please delete this comment.
