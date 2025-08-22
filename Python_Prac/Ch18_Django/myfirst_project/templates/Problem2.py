from tkinter import *


def R_size():
    root.geometry(f"{w_value.get()}x{h_value.get()}")    
root=Tk()
root.geometry("500x400")
root.title("Problem 2 Resizing window")

title_lb=Label(root,text="Resizing the window ",fg='blue',font="Arial 14 bold").grid(row=0,column=2)
width_lb=Label(root,text="Width",pady=10).grid(row=2,column=1)
height_lb=Label(root,text="Height",pady=10).grid(row=4,column=1)


w_value=IntVar()
h_value=IntVar()

w_entry=Entry(root,textvariable=w_value,relief=SUNKEN).grid(row=2,column=2)
h_entry=Entry(root,textvariable=h_value,relief=SUNKEN).grid(row=4,column=2)

Button(root,text="Resize window",command=R_size).grid(row=6,column=2)
root.mainloop()


