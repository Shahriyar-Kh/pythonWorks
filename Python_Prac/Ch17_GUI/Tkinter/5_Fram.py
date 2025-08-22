# Import the Tkinter module
from tkinter import *

# Create the main Tkinter window
root = Tk()

# Set the size of the window
root.geometry("600x500")

# Set the title of the window
root.title("Shary GUI")

# Create the first frame with specified options/attributes
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)

# Pack the first frame onto the window with specified options/attributes
f1.pack(side="left", fill="x")

# Create a label inside the first frame
l1 = Label(f1, text="Frame1")

# Pack the label inside the first frame with padding
l1.pack(pady=142)

# Create the second frame with specified options/attributes
f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)

# Pack the second frame onto the window with specified options/attributes
f2.pack(side="top", fill="x")

# Create a label inside the second frame
l2 = Label(f2, text="Frame2")

# Pack the label inside the second frame
l2.pack()

# Start the Tkinter event loop
root.mainloop()
