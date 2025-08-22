from tkinter import *

# Function to print the form values
def getvals():
    print("Received Form")
    print(f"Name: {name.get()}\nPhone: {phone.get()}\nGender: {gender.get()}\nEmergency Contact: {emergency.get()}\nPayment Mode: {payment_mode.get()}\nFood Service: {food_service.get()}")

# Create the Tkinter window
root = Tk()
root.geometry("600x400")
root.title("Travels Form")

# Labels for form fields
Label(root, text="Shahriyar Khan Travels Form", foreground="blue", font="Arial 14 bold", pady=20).grid(row=0, column=4)
Label(root, text="Name", font="Arial 12 bold").grid(row=2, column=2)
Label(root, text="Phone", font="Arial 12 bold").grid(row=4, column=2)
Label(root, text="Gender", font="Arial 12 bold").grid(row=6, column=2)
Label(root, text="Emergency Contact", font="Arial 12 bold").grid(row=8, column=2)
Label(root, text="Payment Mode", font="Arial 12 bold").grid(row=10, column=2)
Label(root, text="Food Service", font="Arial 12 bold").grid(row=12, column=2)

# Variables to store form values
name = StringVar()
phone = IntVar()
gender = StringVar()
emergency = IntVar()
payment_mode = StringVar()
food_service = IntVar()

# Entry widgets for user input
Entry(root, textvariable=name).grid(row=2, column=4)
Entry(root, textvariable=phone).grid(row=4, column=4)
Entry(root, textvariable=gender).grid(row=6, column=4)
Entry(root, textvariable=emergency).grid(row=8, column=4)
Entry(root, textvariable=payment_mode).grid(row=10, column=4)

# Checkbutton widget for food service
Checkbutton(root, text="Want to prebook your meals?", variable=food_service).grid(row=12, column=4)

# Submit button
Button(root, text="Submit to Shary Travels", command=getvals).grid(row=14, column=4)

# Start the Tkinter event loop
root.mainloop()
