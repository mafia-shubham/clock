
from tkinter import *
from tkinter.ttk import *
from time import strftime

class Time(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Clock - By 💕/shubh ")
        self.resizable(False, False)

    def edit(self):
        
        l1 = Label(self, text="   Welcome To -- Clock  ", font="Pristina 25 bold", foreground="brown", relief="groove", borderwidth=10 ).place(x=60, y=40)
        l2 = Label(self, text="_________________________________________________________________________________________________________").place(x=1, y=120)
        l3 = Label(self, text="_________________________________________________________________________________________________________").place(x=1, y=220)
        l4 = Label(self, text="🔰 Time is Gold 🔰", foreground="purple", font="Monospace 15 bold" ).place(x=100, y=250)
    
        global time_label
        time_label = Label(self, font = 'calibri 40 bold', background="black", foreground="red")
        time_label.place(x=50, y=150)
        

    def time(self):

        time_string = strftime('%H:%M:%S %p')
        time_label.config(text = time_string)
        time_label.after(1000, self.time)
    
    


if __name__=="__main__":
    window = Time()
    window.edit()
    window.time()

    window.mainloop()