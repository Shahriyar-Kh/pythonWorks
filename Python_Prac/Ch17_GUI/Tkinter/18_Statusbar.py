from tkinter import *


def Uplaod():
    status_var.set("Busy.....")
    status_lb.update()
    import time
    time.sleep(2)
    status_var.set("Ready now")
root=Tk()
root.title("Status Bar")
root.geometry("400x500")

status_var=StringVar()
status_var.set("Reday")
status_lb=Label(root,textvariable=status_var,relief=SUNKEN,anchor="w")
status_lb.pack(side=BOTTOM,fill="x")

Button(root,text="Uplaod",command=Uplaod).pack()
root.mainloop()