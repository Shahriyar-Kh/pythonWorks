# Importing necessary libraries
from tkinter import *
from PIL import ImageTk, Image

# Creating the Tkinter root window
root = Tk()

# Loading images
img1 = ImageTk.PhotoImage(Image.open('E:\Python_Prac\Ch17_GUI_Tkinter\Tkinter1\m1.jpeg'))
img2 = ImageTk.PhotoImage(Image.open('E:\Python_Prac\Ch17_GUI_Tkinter\Tkinter1\m2.jpeg'))
img3 = ImageTk.PhotoImage(Image.open('E:\Python_Prac\Ch17_GUI_Tkinter\Tkinter1\m3.png'))
img4 = ImageTk.PhotoImage(Image.open('E:\Python_Prac\Ch17_GUI_Tkinter\Tkinter1\m4.jpeg'))
img5 = ImageTk.PhotoImage(Image.open('E:\Python_Prac\Ch17_GUI_Tkinter\Tkinter1\m5.jpeg'))

# Creating a list to hold the loaded images
img_list = [img1, img2, img3, img4, img5]

# Displaying the first image
my_label = Label(root, image=img_list[0])
my_label.grid(row=0, column=0, columnspan=3)

# Function to move forward through images
def forword(img_num):
    global my_label
    global btn_forward
    global btn_backward

    my_label.grid_forget()  # Remove the current image from the screen
    my_label = Label(image=img_list[img_num - 1])  # Load the next image
    btn_forward = Button(root, text=">>", command=lambda: forword(img_num + 1))  # Update forward button
    btn_backward = Button(root, text="<<", command=lambda: backword(img_num - 1))  # Update backward button
    if img_num == len(img_list):
        btn_forward = Button(root, text=">>", state=DISABLED)  # Disable forward button if last image

    my_label.grid(row=0, column=0, columnspan=3)  # Display the new image
    btn_backward.grid(row=1, column=0)  # Display the backward button
    btn_forward.grid(row=1, column=2)  # Display the forward button

# Function to move backward through images
def backword(img_num):
    global my_label
    global btn_forward
    global btn_backward

    my_label.grid_forget()  # Remove the current image from the screen
    my_label = Label(image=img_list[img_num - 1])  # Load the previous image
    btn_forward = Button(root, text=">>", command=lambda: forword(img_num + 1))  # Update forward button
    btn_backward = Button(root, text="<<", command=lambda: backword(img_num - 1))  # Update backward button
    if img_num == 1:
        btn_backward = Button(root, text="<<", state=DISABLED)  # Disable backward button if first image

    my_label.grid(row=0, column=0, columnspan=3)  # Display the new image
    btn_backward.grid(row=1, column=0)  # Display the backward button
    btn_forward.grid(row=1, column=2)  # Display the forward button

# Creating buttons
btn_forward = Button(root, text=">>", command=lambda: forword(2))
btn_exit = Button(root, text="Exit program", command=root.quit)
btn_backward = Button(root, text="<<", command=lambda: backword(1))

# Displaying buttons
btn_forward.grid(row=1, column=2)
btn_exit.grid(row=1, column=1)
btn_backward.grid(row=1, column=0)

# Running the Tkinter event loop
root.mainloop()
