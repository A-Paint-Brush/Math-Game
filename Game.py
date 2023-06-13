import tkinter
import tkinter.messagebox
import math
import random
import Timer
import Results


class Game:
    def __init__(self, mode, digits, seconds, name):
        self.mistakes = 0
        self.r = random.Random()
        self.Random = False
        self.mode = mode
        self.digits = digits
        self.seconds = seconds
        self.name = name
        self.message_show = False
        if self.mode == "Random":
            self.Random = True
        self.window = tkinter.Tk()
        self.window.title("Math + − × ÷ Game")
        self.window.geometry("600x400")
        self.window.maxsize(600, 400)
        self.window.minsize(600, 400)
        self.question_number = tkinter.Label(self.window, text="", font=('times', 16, 'normal'))
        self.question_number.place(x=0, y=0)
        self.question = tkinter.Label(self.window, text="", font=('times', 16, 'normal'))
        self.question.place(x=0, y=35)
        self.timer = tkinter.Label(self.window, text="", font=('times', 50, 'normal'))
        self.timer.place(x=280, y=140)
        self.message = tkinter.Label(self.window, text="", font=('times', 20, 'normal'))
        self.message.place(x=256, y=310)
        self.answer = tkinter.StringVar()
        self.Entry = tkinter.Entry(self.window, width="600", textvariable=self.answer)
        self.Entry.place(x=0, y=355)
        self.Entry.bind('<Return>', self.Check)
        self.submit = tkinter.Button(self.window, text="Submit", command=self.Check)
        self.submit.pack(side="bottom")
        self.question_num = 0
        self.start()
        self.window.mainloop()

    def start(self):
        self.question_num += 1
        if self.Random:
            self.number = self.r.randint(1, 4)
            if self.number == 1:
                self.mode = "Adding"
            elif self.number == 2:
                self.mode = "Subtracting"
            elif self.number == 3:
                self.mode = "Multiplying"
            else:
                self.mode = "Dividing"
        self.gameloop()

    def generate(self):
        if self.digits == 1:
            self.number1 = self.r.randint(0, 9)
        else:
            self.number1 = str(self.r.randint(1, 9))
            for i in range(0, self.digits - 1):
                self.number1 += str(self.r.randint(0, 9))
        if self.mode == "Dividing":
            if self.r.randint(1, self.digits) == 1:
                self.number2 = str(self.r.randint(0, 9))
            else:
                self.number2 = str(self.r.randint(1, 9))
        else:
            if self.digits == 1:
                self.number2 = self.r.randint(0, 9)
            else:
                self.number2 = str(self.r.randint(1, 9))
        if self.mode == "Dividing":
            for i in range(0, self.r.randint(1, self.digits) - 1):
                self.number2 += str(self.r.randint(0, 9))
        else:
            for i in range(0, self.digits - 1):
                self.number2 += str(self.r.randint(0, 9))
        self.number1 = int(self.number1)
        self.number2 = int(self.number2)
        if self.mode == "Dividing" and self.number1 < self.number2:
            self.generate()

    def gameloop(self):
        self.generate()
        self.count_time = Timer.Timer()
        self.count_time.reset()
        self.repeat()

    def repeat(self):
        self.remaining_time = math.floor(self.seconds - self.count_time.get_time())
        self.question_number.config(text="Question " + str(self.question_num))
        if self.mode == "Adding":
            self.question.config(text=str(self.number1) + "+" + str(self.number2) + "=?")
        elif self.mode == "Subtracting":
            self.question.config(text=str(self.number1) + "−" + str(self.number2) + "=?")
        elif self.mode == "Multiplying":
            self.question.config(text=str(self.number1) + "×" + str(self.number2) + "=?")
        elif self.mode == "Dividing":
            self.zero = False
            try:
                round(self.number1 / self.number2)
            except ZeroDivisionError:
                self.zero = True
                self.question.config(text=str(self.number1) + "÷" + str(self.number2) + "=?")
            if not self.zero:
                if self.number1 / self.number2 == round(self.number1 / self.number2):
                    self.question.config(text=str(self.number1) + "÷" + str(self.number2) + "=?")
                else:
                    self.question.config(text=str(self.number1) + "÷" + str(self.number2) + "≑?")
        if len(str(self.remaining_time)) == 3:
            self.timer.place(x=247, y=140)
        elif len(str(self.remaining_time)) == 2:
            self.timer.place(x=265, y=140)
        else:
            self.timer.place(x=280, y=140)
        self.timer.config(text=self.remaining_time)
        if self.remaining_time <= 0:
            self.window.after_cancel(self.loop)
            if self.message["text"] != "":
                self.window.after_cancel(self.message_wait)
            self.message.config(text="")
            self.answer.set("")
            tkinter.messagebox.showwarning("Time's up!", "You did not enter the correct answer before the timer ran "
                                                         "out, "
                                                         "so you lose!")
            self.window.destroy()
            if self.mode == "Adding":
                Results.Results(self.question_num, self.mistakes, self.number1 + self.number2, self.name, self.number1, self.number2, self.mode)
            elif self.mode == "Subtracting":
                Results.Results(self.question_num, self.mistakes, self.number1 - self.number2, self.name, self.number1, self.number2, self.mode)
            elif self.mode == "Multiplying":
                Results.Results(self.question_num, self.mistakes, self.number1 * self.number2, self.name, self.number1, self.number2, self.mode)
            elif self.mode == "Dividing":
                self.zero = False
                try:
                    self.number1 / self.number2
                except ZeroDivisionError:
                    self.zero = True
                if self.zero:
                    Results.Results(self.question_num, self.mistakes, "undefined", self.name, self.number1, self.number2, self.mode)
                else:
                    Results.Results(self.question_num, self.mistakes, round(self.number1 / self.number2), self.name, self.number1, self.number2, self.mode)
            return None
        if not self.remaining_time <= 0:
            self.loop = self.window.after(10, self.repeat)

    def Check(self, event=None):
        if self.mode == "Adding":
            if self.Entry.get() == str(self.number1 + self.number2):
                self.Correct()
            else:
                self.showmessage = False
                if self.message_show:
                    self.window.after_cancel(self.message_wait)
                self.Message("Wrong!")
        elif self.mode == "Subtracting":
            if self.Entry.get() == str(self.number1 - self.number2):
                self.Correct()
            else:
                self.showmessage = False
                if self.message_show:
                    self.window.after_cancel(self.message_wait)
                self.Message("Wrong!")
        elif self.mode == "Multiplying":
            if self.Entry.get() == str(self.number1 * self.number2):
                self.Correct()
            else:
                self.showmessage = False
                if self.message_show:
                    self.window.after_cancel(self.message_wait)
                self.Message("Wrong!")
        elif self.mode == "Dividing":
            self.zero = False
            try:
                self.number1 / self.number2
            except ZeroDivisionError:
                if self.Entry.get() == 'undefined':
                    self.Correct()
                    return None
                else:
                    self.showmessage = False
                    if self.message_show:
                        self.window.after_cancel(self.message_wait)
                    self.Message("Wrong!")
                    return None
            if self.Entry.get() == str(round(self.number1 / self.number2)):
                self.Correct()
            else:
                self.showmessage = False
                if self.message_show:
                    self.window.after_cancel(self.message_wait)
                self.Message("Wrong!")

    def Correct(self):
        if self.message["text"] != "":
            self.window.after_cancel(self.message_wait)
        self.message.config(text="")
        self.window.after_cancel(self.loop)
        self.answer.set("")
        tkinter.messagebox.showinfo("Answer Correct",
                                    "The answer you entered is correct! Click 'ok' to proceed to the next question.")
        self.start()

    def Message(self, message):
        if not self.showmessage:
            self.message_show = True
            self.mistakes += 1
            self.answer.set("")
            self.showmessage = True
            self.message.config(text=message)
            self.message_wait = self.window.after(3000, self.Message, None)
        else:
            self.message_show = False
            self.message.config(text="")
            self.window.after_cancel(self.message_wait)
