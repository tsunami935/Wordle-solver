import tkinter
import wordle

class WordleWindow:
    def __init__(self):
        self.master = tkinter.Tk()
        self.master.title("Wordle Solver")
        self.guesser = wordle.Wordle()
        self.reset()
        self.enter = tkinter.Button(self.master, height=2, width=12, text="Enter", bg="white", command=self.guess).pack(side="left")
        self.button_colors = {"white": 0, "yellow": 1, "green": 2, 0:"white", 1:"yellow", 2:"green"}

    def guess(self):
        hint = ""
        for button in self.buttons:
            hint += str(self.button_colors[button['bg']])
        if self.word['text']:
            self.guesser.process_hints(self.word['text'], hint)
        self.word['text'] = self.guesser.guess()

    def reset(self):
        try:
            self.__getattribute__("buttons")
            pass
        except:
            self.word = tkinter.Label(self.master, height=2, width=20, text="")
            self.word.pack(side="top")
            self.buttons = []
            for i in range(5):
                button = tkinter.Button(self.master, height=2, width=4, bg="white", command=lambda a=i :self.toggle_button_color(a))
                self.buttons.append(button)
                button.pack(side="left")

    def toggle_button_color(self, index):
        try:
            button = self.buttons[index]
            button['bg']=self.button_colors[(self.button_colors[button['bg']]+1)%3]
        except:
            return

def main():
    window = WordleWindow()
    window.master.mainloop()
    
if __name__ == "__main__":
    main()