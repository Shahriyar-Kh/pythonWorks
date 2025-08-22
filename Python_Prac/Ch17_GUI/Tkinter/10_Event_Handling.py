from tkinter import *

def shary(Event):
    print(f"You Click on the Button at {Event.x},{Event.y}")
root=Tk()
root.geometry("400x300")


widg_btn=Button(root,text="Click me Please",fg="White",bg="Black")
widg_btn.pack()

widg_btn.bind("<Button-1>",shary)
widg_btn.bind("<Double-1>",quit)






root.mainloop()