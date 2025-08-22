from tkinter import *
from tkinter import messagebox

root=Tk()


def showinf():
    response=messagebox.showinfo("Information","Show information")
    Label(root,text=response).pack()
    
btn=Button(root,text="showinf",command=showinf).pack(padx=40,pady=40)

def showwarning():
    response2=messagebox.showwarning("Warning","Show warning")
    Label(root,text=response2).pack()
    
btn=Button(root,text="Warning",command=showwarning).pack(padx=40,pady=40)

def showError():
    response2=messagebox.showerror("Error","Show Error")
    Label(root,text=response2).pack()
    
btn=Button(root,text="Error",command=showError).pack(padx=40,pady=40)

def askquestion():
    response4=messagebox.askquestion("Question","Do you like Mango?")
    if response4=="yes":
        Label(root,text=response4+" I like Mango").pack()
    else:
        Label(root,text=response4+" I dont like Mango").pack()
    
btn=Button(root,text="Ask",command=askquestion).pack(padx=40,pady=40)

def askokcancel():
    response4=messagebox.askokcancel("Question","Want to wait or cancel?")
    if response4==1:
        Label(root,text="Yes i will be wait").pack()
    else:
        Label(root,text=response4+"No cancel").pack()
    
btn=Button(root,text="Ask2",command=askokcancel).pack(padx=40,pady=40)

root.mainloop()