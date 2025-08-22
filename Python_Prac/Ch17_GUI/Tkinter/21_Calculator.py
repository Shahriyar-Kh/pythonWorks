from tkinter import *

def click(event):
    global scvalue
    btext= event.widget.cget("text")
    if btext=="=":
        if scvalue.get().isdigit():
            Value=int(scvalue.get())
        else:
            try:
                Value=eval(scvalue.get())
            except Exception as e:
                print(e)
                Value="Error"
    
        scvalue.set(Value)
        screen.update()
    elif btext=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+btext)
        screen.update()
root=Tk()

root.geometry("600x900")

root.title("Shary Calculater")

scvalue=StringVar()
scvalue.set("")

screen=Entry(root,textvariable=scvalue,font="Locida 40 bold")
screen.pack(fill="x",pady=20,padx=20)

f=Frame(root,bg="grey")
b=Button(f,text="-",font="locida 28 bold")
b.pack(side="left",padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="+",font="locida 28 bold")
b.pack(side="left",padx=12,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="*",font="locida 28 bold")
b.pack(side="left",padx=12,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="/",font="locida 28 bold")
b.pack(side="left",padx=15,pady=10)
b.bind("<Button-1>",click)

f.pack()


f=Frame(root,bg="grey")
b=Button(f,text="9",font="locida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="8",font="locida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="7",font="locida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="=",font="locida 26 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="6",font="locida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="5",font="locida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="4",font="locida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="C",font="locida 24 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="3",font="locida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="2",font="locida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="1",font="locida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="%",font="locida 22 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="0",font="locida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()
root.mainloop()
