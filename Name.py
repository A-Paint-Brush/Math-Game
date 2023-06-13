import tkinter
import tkinter.messagebox
import Game


class Name:
    def __init__(self, mode, digits, seconds):
        self.mode = mode
        self.digits = digits
        self.seconds = seconds
        self.window = tkinter.Tk()
        self.window.title("Settings — Page 2")
        self.window.geometry("434x400")
        self.window.maxsize(434, 400)
        self.window.minsize(434, 400)
        self.Label = tkinter.Label(self.window, text='''Please enter your name, the name you enter will be used to
        save your score. It does not need to be your real name.
        You cannot enter more than 20 characters.''')
        self.Label.pack()
        self.Name = tkinter.StringVar()
        self.Input = tkinter.Entry(self.window, textvariable=self.Name)
        self.Input.pack()
        self.Submit = tkinter.Button(self.window, text="Start Game", command=self.Check)
        self.Submit.pack()
        self.window.mainloop()

    def Check(self):
        if len(self.Name.get()) > 20:
            self.Name.set("")
            tkinter.messagebox.showerror("Error", "The name you entered is too long, it cannot be more than 20 "
                                                  "characters long.")
        elif self.Name.get().count("\\") > 0:
            self.Name.set("")
            tkinter.messagebox.showerror("Error", "The name you entered contains backward slashes, which is not "
                                                  "allowed.")
        elif self.Name.get() == "" or self.Name.get().count(" ") == len(self.Name.get()):
            self.Name.set("")
            tkinter.messagebox.showerror("Error", "You didn't enter a name.")
        else:
            tkinter.messagebox.showinfo("Instructions", "Please read the following instructions before you "
                                                        "continue:\nWhen the game starts, you will see at the top of "
                                                        "the screen the question number, the math question, "
                                                        "and a textbox and a button at the bottom of the screen. You "
                                                        "will also see a timer counting down at the middle of the "
                                                        "screen. Enter your answer into the textbox at the bottom of "
                                                        "the screen and click the button or press enter to submit "
                                                        "your answer. It doesn't matter if you make a mistake, "
                                                        "but if you have not entered the correct answer by the time "
                                                        "the timer runs out, you lose! In dividing questions, "
                                                        "remember to round your answer up to the nearest whole "
                                                        "number. In a dividing question, if the divisor is zero, "
                                                        "type 'undefined'.")
            tkinter.messagebox.showwarning("Warning", "Do not close this application during gameplay. If you close "
                                                      "this application while playing, your score will not be "
                                                      "registered to the score board.")
            self.Namevalue = self.Name.get()
            self.window.destroy()
            Game.Game(self.mode, self.digits, self.seconds, self.Namevalue)
