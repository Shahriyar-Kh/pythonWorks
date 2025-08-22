from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newfile():
    global file
    root.title("Untitled - Notepad")
    file=None
    textArea.delete(1.0,END)

def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[
        ("All Files","*.*"),("Text Documents","*.txt")])
    
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        textArea.delete(1.0,END)
        f=open(file,"r")
        textArea.insert(1.0,f.read())

def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])

        if file == "":
            file=None
        else:
            #save as new file
            f=open(file,"w")
            f.write(textArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+ "- Notepad")
            print("file saved")


def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():

    textArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by shary khan")
root=Tk()
root.title("NotePade")
root.geometry("600x900")

#Create textArea
textArea=Text(root,font="Locida 12")
file=None
textArea.pack(expand=True,fill=BOTH)


#Create menueBar
menuBar=Menu(root)

#create file menu
fileMenu=Menu(menuBar,tearoff=0)
#adding file
fileMenu.add_command(label="New",command=newfile)
fileMenu.add_command(label="Open",command=openfile)
fileMenu.add_command(label="Save",command=savefile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

menuBar.add_cascade(label="File",menu=fileMenu)


#create Editmenu
editMenu=Menu(menuBar)
#adding element
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

menuBar.add_cascade(label="Edit",menu=editMenu)

#Create help menu
helpMenu=Menu(menuBar,tearoff=0)

helpMenu.add_command(label="About notepade",command=about)

menuBar.add_cascade(label="Help",menu=helpMenu)


#add scrollbare
Scroll_B=Scrollbar(textArea)
Scroll_B.pack(side=RIGHT,fill=Y)
Scroll_B.config(command=textArea.yview)

textArea.config(yscrollcommand=Scroll_B.set)


root.config(menu=menuBar)
root.mainloop()