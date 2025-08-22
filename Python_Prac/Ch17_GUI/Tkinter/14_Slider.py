from tkinter import *
import tkinter.messagebox as tmsg



def getdoller():
    tmsg.showinfo("Amount Credited",f"we have Creidited {myslider.get()} dollers to your bank Account")
root=Tk()
root.geometry("400x500")
root.title("Slider")


Label(root,text="How many Dollers you want?",font="Arial 14 bold",fg='green').pack()
myslider=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50,highlightbackground='blue',highlightthickness=5)
myslider.set(10)

myslider.pack()
Button(root,text="Get Dollers",command=getdoller).pack()
root.mainloop()