from tkinter import *

root=Tk()
root.title("Simple calculater")

e=Entry(root,relief=SUNKEN,font='Locida 16 bold')
e.grid(row=0,column=0,columnspan=3,padx=20,pady=10)
e2=Entry(root,relief=SUNKEN,font='Locida 16 bold')
e2.grid(row=1,column=0,columnspan=3,padx=20,pady=10)

def button_click(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(num))


def clear():
    e.delete(0,END)

def add():
    global f_num
    global op
    op="add"
    f_num=int(e.get())
    e.delete(0,END)
def sub():
    global f_num
    global op
    op="sub"
    f_num=int(e.get())
    e.delete(0,END)

def mul():
    global f_num
    global op
    op="mul"
    f_num=int(e.get())
    e.delete(0,END)

def div():
    global f_num
    global op
    op="div"
    f_num=int(e.get())
    e.delete(0,END)

def equal():
    second_num=int(e.get())
    e.delete(0,END)
    if op=="add":
        e.insert(0,f"{f_num} + {second_num}")
        result=f_num + second_num
        e2.delete(0,END)
        e2.insert(0,result)

    elif op=="sub":
        e.insert(0,f"{f_num} - {second_num}")
        result=f_num - second_num
        e2.delete(0,END)
        e2.insert(0,result)

    elif op=="mul":
        e.insert(0,f"{f_num} * {second_num}")
        result=f_num * second_num
        e2.delete(0,END)
        e2.insert(0,result)

    else:
        e.insert(0,f"{f_num} / {second_num}")
        result=f_num / second_num
        e2.delete(0,END)
        e2.insert(0,result)
btn_9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
btn_8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
btn_7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
btn_6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
btn_5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
btn_4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
btn_3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
btn_2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
btn_1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
btn_0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))

btn_clear=Button(root,text="Clear",padx=77,pady=20,command=clear)
btn_add=Button(root,text="+",padx=39,pady=20,command=add)
btn_sub=Button(root,text="-",padx=40,pady=20,command=sub)
btn_mul=Button(root,text="*",padx=40,pady=20,command=mul)
btn_div=Button(root,text="/",padx=40,pady=20,command=div)
btn_equal=Button(root,text="=",padx=86,pady=20,command=equal)

btn_9.grid(row=2,column=0)
btn_8.grid(row=2,column=1)
btn_7.grid(row=2,column=2)

btn_6.grid(row=3,column=0)
btn_5.grid(row=3,column=1)
btn_4.grid(row=3,column=2)

btn_3.grid(row=4,column=0)
btn_2.grid(row=4,column=1)
btn_1.grid(row=4,column=2)

btn_0.grid(row=5,column=0)
btn_clear.grid(row=5,column=1,columnspan=2)

btn_add.grid(row=6,column=0)
btn_sub.grid(row=6,column=1)
btn_mul.grid(row=6,column=2)

btn_div.grid(row=7,column=0)
btn_equal.grid(row=7,column=1,columnspan=2)


root.mainloop()