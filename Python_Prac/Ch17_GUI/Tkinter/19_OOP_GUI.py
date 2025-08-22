from tkinter import *
import tkinter.messagebox as tmsg
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.title("OOP GUI")

    def labels(self):
        self.lb1=Label(self,"Enter First Number:",font="Arial 12 bold ",fg='blue')
        self.lb2=Label(self,"Enter Second Number:",font="Arial 12 bold ",fg='blue')
        self.lb1.pack()
        self.lb2.pack()

    def Entries(self):
        self.num1_var=IntVar()
        self.num2_var=IntVar()

        num1_entry=Entry(self,textvariable=self.num1_var).pack()  
        num1_entry=Entry(self,textvariable=self.num2_var).pack()

    def buttons(self):
        Button(self,text="Add",font="Arial 12 bold",bg="black",fg='white',relief=SUNKEN,command=add).pack()
        Button(self,text="Minus",font="Arial 12 bold",bg="black",fg='white',relief=SUNKEN,command=minus).pack()
        Button(self,text="Multifly",font="Arial 12 bold",bg="black",fg='white',relief=SUNKEN,command=multifly).pack()
        Button(self,text="Divide",font="Arial 12 bold",bg="black",fg='white',relief=SUNKEN,divide).pack()

def add():
        sum=obj.num1_var+obj.num2
        tmsg.showinfo("Addition",f"Addition of {obj.num1} + {obj.num2} = {sum}")

if __name__=="__main__":
    obj=GUI()
    obj.labels()
    obj.Entries()
    obj.buttons()
    obj.mainloop()
