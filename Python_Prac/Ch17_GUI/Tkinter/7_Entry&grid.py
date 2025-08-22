from tkinter import*


def getval():
    file=open('form.csv','a')
    value1=userentry.get()
    value2=passentry.get()
    form=(f"{value1}\t\t\t{value2}\n")
    #file.write("Username \t\t Password\n")
    file.write(form)
    file.close()
root = Tk()
root.geometry("600x500")

# Create two labels

user = Label(root, text="Username")
password = Label(root, text="Password")

# Packing by grid method with row and column specified
user.grid()
password.grid(row=1)

#create entry widget
userentry=Entry(root,textvariable=StringVar())
passentry=Entry(root,textvariable=StringVar())

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

#Create button using shorthand
Button(text="Submit",command=getval).grid()

# Start the Tkinter event loop
root.mainloop()
