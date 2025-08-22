from tkinter import *

root=Tk()
root.geometry("400x500")
root.title("GUI title")
# root.wm_iconbitmap()
root.configure(background="grey")

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="Close",command=root.destroy).pack()


root.mainloop()