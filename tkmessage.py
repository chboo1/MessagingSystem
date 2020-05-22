from csv import reader, writer
from tkinter import Tk, Canvas
from subprocess import run
class Send_messages():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x400")
        self.root.title("Message pickle bro")
        self.c = Canvas(self.root, width=800, height=400)
        self.c.pack()
        self.text=""
        self.txt=self.c.create_text(750, 350, anchor="se", text="")
        self.root.bind("<Escape>", self.kr)
        self.root.bind("<Key>", self.write)
        self.root.mainloop()
    def write_row(self, arg):
        with open("/home/pi/.picklebro/data.csv", "a") as self.file:
            write=writer(self.file)
            write.writerow([arg, "chboo1"])
    def write(self, event):
        if event.keysym == "Return":
            self.write_row(self.text)
            self.text=""
            self.c.itemconfig(self.txt, text="")
        elif event.keysym == "BackSpace":
            self.text=self.text[:-1]
            self.c.itemconfig(self.txt, text=self.text)
        else:
            self.c.itemconfig(self.txt, text=self.text+event.char)
            self.text=self.text+event.char
    def kr(self, event):
        self.root.destroy()
runing=Send_messages()
            
            
