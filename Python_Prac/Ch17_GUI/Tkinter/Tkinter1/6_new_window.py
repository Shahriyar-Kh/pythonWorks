from tkinter import*

#creat first window
root=Tk()
root.title("Cites")
root.geometry("300x600")


def peshawer():
    root2=Toplevel()
    root2.title("Details")
    
    Label(root2,text="Peshawer is the capital of the KPK").pack()
    root2.mainloop()

btn=Button(root,text="Peshwer",padx=10,pady=10,command=peshawer).pack()


root.mainloop()