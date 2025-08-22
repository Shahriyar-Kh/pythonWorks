from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("Shary GUI")
root.iconbitmap('E:\Python_Prac\Ch17_GUI_Tkinter\Tkinter1\SHK.ico')

my_img=ImageTk.PhotoImage(Image.open('E:\Python_Prac\Ch17_GUI_Tkinter\Tkinter1\m1.png'))
Label(image=my_img).pack()


exit_btn=Button(root,text="Exit Program",command=root.quit)
exit_btn.pack()


root.mainloop()