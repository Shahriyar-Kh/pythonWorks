
#important label options /attribute 
"""
1. Text-adds the Text
2. bd-background
3. fg-foreground 
4. font -set the font
5. padx -  xpading
6. ypad - ypading
7.  relief - border style 
    7.1 sunken  best mota GUI
    7.2 raised
    7.3 GROOVE
    7.4 RIDGE
8. 
"""
#important pack options/atributes
"""
1. ANCHOR 
    1.1 NW
    1.2 NS
2. slice
    2.1 TOP
     2.2 bottom
    2.3 LEFT
    2.4 RIGHT
3. fill
4.padx
5.pady
"""
# Import the Tkinter module
from tkinter import *

# Create the main Tkinter window
root = Tk()

# Set the size of the window
root.geometry("600x500")

# Set the title of the window
root.title("My GUI Programming with Shary")

# Create a label widget with multiple options/attributes
title_label = Label(
    text="""
    What is Tkinter?
    Tkinter is the inbuilt python module that is used to create GUI applications.\n 
    It is one of the most commonly used modules for creating GUI applications in Python as it is simple and easy to work with.\n
    You don’t need to worry about the installation of the Tkinter module separately as it comes with Python already. 
    It gives an object-oriented interface to the Tk GUI toolkit. \n
    Some other Python Libraries available for creating our own GUI applications are
    """,
    bg="blue",  # Background color
    fg="white",  # Foreground color (text color)
    padx=20,  # Horizontal padding
    pady=20,  # Vertical padding
    font="Arial 5 bold",  # Font and size
    borderwidth=5,  # Border width
    relief=SUNKEN  # Border style (sunken)
)

# Pack the label widget onto the window with specified options/attributes
title_label.pack(
    side="left",  # Position of the widget relative to its parent
    anchor=NE,  # Positioning anchor (North-East)
    fill=X,  # How the widget expands to fill the available space (horizontally)
    padx=20,  # Horizontal padding
    pady=20  # Vertical padding
)

# Start the Tkinter event loop
root.mainloop()
