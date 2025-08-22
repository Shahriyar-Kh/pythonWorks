from tkinter import *

def button(bfram,btext,bfont,p_pdx,p_pdy,p_side):
    b=Button(bfram,text=btext,font=bfont)
    b.pack(side=p_side,padx=p_pdx,pady=p_pdy)
    b.bind("<Button-1>",click)

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
button(f,"-","Lusida 28 bold",15,10,LEFT)
button(f,"+","Lusida 28 bold",12,10,LEFT)
button(f,"*","Lusida 28 bold",12,10,LEFT)
button(f,"/","Lusida 28 bold",15,10,LEFT)
f.pack()

f=Frame(root,bg="grey")
button(f,"9","Lusida 30 bold",10,10,LEFT)
button(f,"8","Lusida 30 bold",10,10,LEFT)
button(f,"7","Lusida 30 bold",10,10,LEFT)
button(f,"=","Lusida 26 bold",10,10,LEFT)
f.pack()

f=Frame(root,bg="grey")
button(f,"6","Lusida 30 bold",10,10,LEFT)
button(f,"5","Lusida 30 bold",10,10,LEFT)
button(f,"4","Lusida 30 bold",10,10,LEFT)
button(f,"C","Lusida 24 bold",10,10,LEFT)
f.pack()

f=Frame(root,bg="grey")
button(f,"3","Lusida 30 bold",10,10,LEFT)
button(f,"2","Lusida 30 bold",10,10,LEFT)
button(f,"1","Lusida 30 bold",10,10,LEFT)
button(f,"%","Lusida 22 bold",10,10,LEFT)
f.pack()

f=Frame(root,bg="grey")
button(f,"0","Lusida 30 bold",10,10,LEFT)
f.pack()
root.mainloop()
