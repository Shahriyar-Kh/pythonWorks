from tkinter import *


root=Tk()
my_fram=LabelFrame(root,text="This is the Fram",padx=50,pady=50)
my_fram.pack(padx=10,pady=10,fill=BOTH)

b=Button(my_fram,text="Click me")
b.pack()

root.mainloop()