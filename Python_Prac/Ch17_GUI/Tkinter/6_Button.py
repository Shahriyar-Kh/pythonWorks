# Import the Tkinter module
from tkinter import*

# Create the main Tkinter window
root=Tk()

# Set the size of the window
root.geometry("600x400")

# Set the title of the window
root.title("Button GUI")

# Function to print a message
def hello():
    print("Hello GUI in python")

# Function to print a name
def name():
    print("My name is shahriyar khan")

# Create a frame for organizing widgets
f1=Frame(root,bg="grey",borderwidth=4,relief=SUNKEN)

# Pack the frame onto the window with specified options
f1.pack(side=LEFT,anchor="nw")

# Create a button to trigger the hello() function
b1=Button(f1,fg="blue",text="Print now",command=hello)

# Pack the button onto the frame with specified options
b1.pack(side=LEFT,padx=10)

# Create a button to trigger the name() function
b2=Button(f1,fg="blue",text="Tell me name now",command=name)

# Pack the button onto the frame with specified options
b2.pack(side=LEFT,padx=10)

# Create a button without any command
b3=Button(f1,fg="blue",text="Print me now")

# Pack the button onto the frame with specified options
b3.pack(side=LEFT,padx=10)

# Start the Tkinter event loop
root.mainloop()
