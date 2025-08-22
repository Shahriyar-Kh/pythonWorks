from tkinter import *
import tkinter.messagebox as tmsg

def apply():
    tmsg.showinfo("Application subject",f"Recieved  your Application to Apply '{var.get()}'.  \nThanks for Applying")

def Order():
    tmsg.showinfo("Order Recieved",f"Recieved your Order {var1.get()}.\nThanks  for Ordering")
root=Tk()
root.geometry("400x500")
root.title("Radio Button")

Label(root,text="What would like to have You sri?",font="Arial 14 bold").pack(anchor=W)

var=StringVar()
var.set("rad")
Radiobutton(root,text="Python",pady=10,variable=var, value="Python").pack(anchor=W)
Radiobutton(root,text="Html",pady=10,variable=var, value="Html").pack(anchor=W)
Radiobutton(root,text="Java",pady=10,variable=var, value="Java").pack(anchor=W)

Button(root,text="Apply Now",command=apply).pack(anchor=W)

var1=StringVar()
var1.set("radio")
food=["Rice","Chiken","lamb","Chapli kabab"]
for i in food:
    Radiobutton(root,text=i,variable=var1,value=i).pack(anchor=W)
Button(root,text="Order now",command=Order).pack(anchor=W)




root.mainloop()

