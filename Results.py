import tkinter
import os


class Results:
    def __init__(self, question_num, mistakes, answer, name, num1, num2, mode):
        self.name = name
        self.score = question_num
        self.window = tkinter.Tk()
        self.window.title("Results")
        self.window.geometry("600x400")
        self.window.maxsize(600, 400)
        self.window.minsize(600, 400)
        self.text = "You lose! You lost on question " + str(question_num) + "\n\nThis is the correct answer of question " + str(question_num) + " :\n"
        if mode == "Adding":
            self.text += str(num1) + "+" + str(num2) + "=" + str(answer)
        elif mode == "Subtracting":
            self.text += str(num1) + "−" + str(num2) + "=" + str(answer)
        elif mode == "Multiplying":
            self.text += str(num1) + "×" + str(num2) + "=" + str(answer)
        elif mode == "Dividing":
            if answer == "undefined":
                self.text += str(num1) + "÷" + str(num2) + "=" + answer
            elif num1 / num2 == round(num1 / num2):
                self.text += str(num1) + "÷" + str(num2) + "=" + str(answer)
            else:
                self.text += str(num1) + "÷" + str(num2) + "≑" + str(answer)
        self.text += "\n\n You made " + str(mistakes) + " mistake(s) in total.\n\n"
        if not os.path.isfile("Data\\High_score.txt"):
            file = open("Data\\High_score.txt", "w", encoding="utf8")
            file.write("0")
            file.close()
        file = open("Data\\High_score.txt", "r", encoding="utf8")
        try:
            self.highest_score = int(file.read())
        except ValueError:
            file.close()
            self.highest_score = 0
            file = open("Data\\High_score.txt", "w", encoding="utf8")
            file.write("0")
        finally:
            file.close()
        if question_num > self.highest_score:
            self.text += "You broke the highest question number reached record!"
            file = open("Data\\High_score.txt", "w", encoding="utf8")
            file.write(str(question_num))
            file.close()
        file = open("Data\\Score.txt", "a", encoding="utf8")
        file.write(self.name + " " * (20 - len(self.name)) + "| " + str(self.score) + "\n")
        file.close()
        self.Results = tkinter.Label(self.window, text=self.text, font=('times', 16, 'normal'))
        self.Results.pack()
        self.exit_button = tkinter.Button(self.window, text="Exit", command=self.close)
        self.exit_button.pack()
        self.window.mainloop()

    def close(self):
        self.window.destroy()
