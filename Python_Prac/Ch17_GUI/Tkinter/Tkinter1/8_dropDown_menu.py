from tkinter import *

root=Tk()
root.title("DropDown Menu")

clicked=StringVar()
clicked.set("Monday")

# dropD=OptionMenu(root,clicked,"Monday","Tuesday").pack()

Options=[
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday"
]
drop_D_M=OptionMenu(root,clicked,*Options).pack()

def show():
    Label(root,text=clicked.get()).pack() 

btn=Button(root,text="Select Day",command=show).pack()


root.mainloop()