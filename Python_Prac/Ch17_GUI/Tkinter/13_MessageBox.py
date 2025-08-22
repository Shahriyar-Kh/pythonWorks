from tkinter import * 
import tkinter.messagebox as tmsg

def myfunc():
    print("working")

def help():
    tmsg.showinfo("Help","Shary can help you")

def Ratus():
    value=tmsg.askquestion("Ask Experience","You Used this gui ... was your Experience Good?")
    print(value)
    if value=="yes":
        msg="Rate us on apstore please"
    else:
        msg="Tell us what was wrong .we will call you soon"
    tmsg.showinfo("Experience",msg)
def sharybefriend():
    ans=tmsg.askretrycancel("friend making shary","Sorry shary does not make you friend")

    if ans:
        tmsg.showinfo("Retry","Retry karni per be nhi")
    else:
        tmsg.showinfo("Retry","Very Good for canceling")

root=Tk()
root.geometry("600x500")
root.title("Example Menu")

mymenu=Menu(root)
helpmenu=Menu(mymenu,tearoff=0)
helpmenu.add_command(label="Help index",command=myfunc)
helpmenu.add_command(label="About ..",command=help)
helpmenu.add_command(label="Rate us ..",command=Ratus)
helpmenu.add_command(label="Shary Befriend ..",command=sharybefriend)

mymenu.add_cascade(label="Help",menu=helpmenu)


root.config(menu=mymenu)
root.mainloop()