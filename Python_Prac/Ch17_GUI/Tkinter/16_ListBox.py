from tkinter import *
 
def Add_items():
    global i
    lbox.insert(ACTIVE,f"{i}")
    i+=1
i=0

root=Tk()
root.title("List Box")
root.geometry("500x600")

lbox=Listbox(root)
lbox.insert(END,"Item 1")
lbox.pack()

Button(root,text="Add Item",command=Add_items).pack()
root.mainloop()