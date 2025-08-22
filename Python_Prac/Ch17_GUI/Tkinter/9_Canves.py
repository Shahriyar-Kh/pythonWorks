from  tkinter import *

root=Tk()
root.geometry('400x300')
root.title("Canves Examples")

Can_widget=Canvas(root,width=600,height=400,bg="grey")
Can_widget.pack(anchor="center",expand=True)

#Draw a red line
#line point x1,y1 and x2,y2
Can_widget.create_line((0,0),(400,300),width=4, fill='red')
Can_widget.create_line((0,300),(400,0),width=4, fill='red')

#draw rectangel
Can_widget.create_rectangle(100,100,400,300,fill='green')


#draw oval
Can_widget.create_oval(50,150,200,350,fill='purple')
root.mainloop()

Can_widget.create_image