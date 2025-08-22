# Import necessary libraries
from tkinter import *
from PIL import Image, ImageTk

# Create the Tkinter window
shary_root = Tk()

# Set the window size
shary_root.geometry("800x1200")

# Set minimum window size
shary_root.minsize(200, 300)

# Set maximum window size
shary_root.maxsize(600, 700)

# Try loading the PNG image with error handling
try:
    # Create a label for PNG example
    label1 = Label(text="PNG Example")
    label1.pack()

    # Load the PNG image
    photo1 = PhotoImage(file="E:\Python_Prac\Ch17_GUI_Tkinter\m2.png")
    
    # Create a label widget to display the PNG image
    label2 = Label(image=photo1)
    label2.pack()
except:
    # Print error message if image loading fails
    print("Error loading PNG image")

# Try loading the JPG image with error handling
try:
    # Create a label for JPG example
    label3 = Label(text="JPEG Example")
    label3.pack()
    
    # Open the JPG image
    open_image = Image.open("E:\Python_Prac\Ch17_GUI_Tkinter\m4.jpeg")
    
    # Convert the image for Tkinter
    con_image = ImageTk.PhotoImage(open_image)
    
    # Create a label widget to display the JPG image
    photo2 = Label(image=con_image)
    photo2.pack()
except:
    # Print error message if image loading fails
    print("Error loading JPG image")

# Run the Tkinter event loop
shary_root.mainloop()
