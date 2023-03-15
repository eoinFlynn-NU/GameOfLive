from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.initUI()


    def initUI(self):

        self.master.title("Colours")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        for w in range(self.width):
            for h in range(self.height):
                canvas.create_rectangle(w*10, h*10, w*10 + 50, h*10 + 50, outline="#000", fill="#fb0")
        # canvas.create_rectangle(30, 10, 120, 80,
        #     outline="#fb0", fill="#fb0")
        # canvas.create_rectangle(150, 10, 240, 80,
        #     outline="#f50", fill="#f50")
        # canvas.create_rectangle(270, 10, 370, 80,
        #     outline="#05f", fill="#05f")
        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example(10,10)
    root.geometry("400x100+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()