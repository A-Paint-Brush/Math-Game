import tkinter
import os
from functools import partial
import Score
import Name


class Settings:
    def __init__(self):
        if not os.path.isfile("Data\\Score.txt"):
            file = open("Data\\Score.txt", "w", encoding="utf8")
            file.close()
        if not os.path.isfile("Data\\High_score.txt"):
            file = open("Data\\High_score.txt", "w", encoding="utf8")
            file.write("0")
            file.close()
        self.buttons = ['Adding', 'Subtracting', 'Multiplying', 'Dividing', 'Random']
        self.mode = None
        self.window = tkinter.Tk()
        self.window.title("Settings — Page 1")
        self.window.geometry("434x400")
        self.window.maxsize(434, 400)
        self.window.minsize(434, 400)
        self.high_scores = tkinter.Button(self.window, text="High Scores Table", command=self.open_table)
        self.high_scores.pack()
        self.label = tkinter.Label(self.window, text='''Please select the number of digits you want
the numbers in the math questions to have
by dragging the slider below.''')
        self.label.pack()
        self.slider = tkinter.Scale(self.window, from_=1, to=10, orient="horizontal")
        self.slider.pack()
        self.label2 = tkinter.Label(self.window, text='''Please select the number of seconds you
will have to answer each math question by
dragging the slider below.''')
        self.label2.pack()
        self.slider2 = tkinter.Scale(self.window, from_=1, to=180, orient="horizontal")
        self.slider2.pack()
        self.slider2.set(15)
        self.label3 = tkinter.Label(self.window, text='''Please select the type of math questions you want
to get by clicking on one of the buttons below.''')
        self.label3.pack()
        for label in range(0, len(self.buttons)):
            tkinter.Button(self.window,
                           text=self.buttons[label],
                           width=9,
                           bg="#FFFFFF",
                           command=partial(self.setmode, self.buttons[label])).place(x=label*75+30, y=250)
        self.window.mainloop()

    def open_table(self):
        self.window.destroy()
        Score.Score()

    def setmode(self, mode):
        self.mode = mode
        self.slidervalue1 = self.slider.get()
        self.slidervalue2 = self.slider2.get()
        self.window.destroy()
        Name.Name(self.mode, self.slidervalue1, self.slidervalue2 + 1)
