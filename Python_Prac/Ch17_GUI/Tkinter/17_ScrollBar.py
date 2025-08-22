from tkinter import *

root=Tk()
root.geometry("300x350")
root.title("Scroll Bar")

#For Connecting scrollbar to a widget 
# 1. widget (vscrollcommond = scrollbar.set)
# 2. scrollbar.config (commond =widget.yview)

Scrollbar1=Scrollbar(root)

Scrollbar1.pack(side=RIGHT,fill="both")

lbox=Listbox(root,yscrollcommand=Scrollbar1.set)

for i in range(300):
    lbox.insert(END,f"{i}")

lbox.pack(fill="both")

Scrollbar1.config(command=lbox.yview)

Scrollbar2=Scrollbar(root)
Scrollbar2.pack(side=RIGHT,fill="both")

text=Text(root,yscrollcommand=Scrollbar2.set)
text.pack(fill="both")

Scrollbar2.config(command=text.yview)



root.mainloop()