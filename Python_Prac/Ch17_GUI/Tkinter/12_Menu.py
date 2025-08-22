from tkinter import * 


def myfunc():
    print("working")


root=Tk()
root.geometry("600x500")
root.title("Example Menu")

mymenu=Menu(root)

filemenu=Menu(mymenu,tearoff=0)
filemenu.add_command(label="New",command=myfunc)
filemenu.add_command(label="Open",command=myfunc)
filemenu.add_command(label="Save",command=myfunc)
filemenu.add_command(label="Save as..",command=myfunc)
filemenu.add_command(label="Close",command=myfunc)

filemenu.add_separator()

filemenu.add_command(label="Exit",command=quit)
mymenu.add_cascade(label="File",menu=filemenu)

editmenu=Menu(mymenu,tearoff=0)

editmenu.add_command(label="Undo",command=myfunc)
editmenu.add_separator()

editmenu.add_command(label="Cut",command=myfunc)
editmenu.add_command(label="Copy",command=myfunc)
editmenu.add_command(label="Paste",command=myfunc)
editmenu.add_command(label="Delete",command=myfunc)
editmenu.add_command(label="Select All",command=myfunc)

mymenu.add_cascade(label="Edit",menu=editmenu)

helpmenu=Menu(mymenu,tearoff=0)
helpmenu.add_command(label="Help index",command=myfunc)
helpmenu.add_command(label="About ..",command=myfunc)

mymenu.add_cascade(label="Help",menu=helpmenu)


root.config(menu=mymenu)
root.mainloop()