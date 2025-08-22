from tkinter import *
import tkinter.messagebox as tmsg



def food():
    
    with open("food.txt",'a') as file:
        file.write(f"{cust_name.get()}\t\t{myslider.get()}\n")
        tmsg.showinfo("Rate Us",f"Thank you {myslider.get()} Rate Us to Ordered Food")


root=Tk()
root.geometry("400x500")
root.title("Slider")

Label(root,text="Name of the Customer").pack()

cust_name=StringVar()
cust_entry=Entry(root,textvariable=cust_name,font="Arial 14 bold").pack()

Label(root,text="Rate us Ordered food!",fg='green').pack()
myslider=Scale(root,from_=0,to=10,orient=HORIZONTAL,tickinterval=5,highlightbackground='blue',highlightthickness=5)

myslider.pack()
Button(root,text="Rate Us",command=food).pack()
root.mainloop()