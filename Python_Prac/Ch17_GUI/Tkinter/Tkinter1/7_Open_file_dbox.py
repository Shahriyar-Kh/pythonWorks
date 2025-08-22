from tkinter import *  # Import everything from the tkinter module
from tkinter import filedialog  # Import the filedialog submodule from tkinter
import os  # Import the os module for file operations

root = Tk()  # Create a Tkinter root window
root.title("Open file")  # Set the title of the window

def open():  # Define a function named open
    # Prompt the user to select a file and get the file path
    filename = filedialog.askopenfilename(initialdir="E:/Python_Prac",
                                           title="Select A File",
                                           filetypes=[("All Files", "*.*"),
                                                      ("Word File", "*.docx")])
    if filename:  # If a file is selected
        try:
            os.startfile(filename)  # Open the file using the default application
        except Exception as e:  # If there's an error
            print("Error:", e)  # Print the error message

# Create a button widget to trigger the open function and pack it into the root window
btn_open = Button(root, text="Open File", command=open).pack()

root.mainloop()  # Start the Tkinter event loop to display the GUI and handle events
