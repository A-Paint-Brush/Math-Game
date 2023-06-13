import tkinter
import os


class Score:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("434x400")
        self.window.title("Highscore Table")
        self.window.maxsize(434, 400)
        self.window.minsize(434, 400)
        self.backbtn = tkinter.Button(self.window, text="Exit", command=self.back)
        self.backbtn.pack()
        self.Content = tkinter.Frame(self.window, width=400, height=360, bg="#FFFFFF")
        self.Content.pack()
        self.Scrollbar = tkinter.Scrollbar(self.Content)
        self.Scrollbar.pack(side="right", fill="y")
        self.Table = tkinter.Text(self.Content, bg="#FFFFFF", width=100, yscrollcommand=self.Scrollbar.set)
        self.Table.pack()
        self.Scrollbar.config(command=self.Table.yview)
        if not os.path.isfile("Data\\Score.txt"):
            file = open("Data\\Score.txt", "w", encoding="utf8")
            file.close()
        file = open("Data\\Score.txt", "r", encoding="utf8")
        if file.read() == "":
            self.Table.insert("end", "\nEmpty")
        else:
            file.seek(0)
            self.Table.insert("end", "Username            | Score\n" + file.read())
        file.close()
        self.Table.config(state="disabled")
        self.window.mainloop()

    def back(self):
        self.window.destroy()
