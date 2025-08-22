import tkinter as tk
from PIL import Image, ImageTk

class GUIApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x1200")
        self.master.minsize(200, 300)
        self.master.maxsize(600, 700)
        self.create_widgets()

    def create_widgets(self):
        # Create a label for PNG example
        self.label1 = tk.Label(self.master, text="PNG Example")
        self.label1.pack()

        # Load and display the PNG image
        try:
            self.photo1 = tk.PhotoImage(file="E:\Python_Prac\Ch17_GUI_Tkinter\m2.png")
            self.label2 = tk.Label(self.master, image=self.photo1)
            self.label2.pack()
        except Exception as e:
            print("Error loading PNG image:", e)

        # Create a label for JPEG example
        self.label3 = tk.Label(self.master, text="JPEG Example")
        self.label3.pack()

        # Load and display the JPEG image
        try:
            self.open_image = Image.open("E:\Python_Prac\Ch17_GUI_Tkinter\m4.jpeg")
            self.con_image = ImageTk.PhotoImage(self.open_image)
            self.label4 = tk.Label(self.master, image=self.con_image)
            self.label4.pack()
        except Exception as e:
            print("Error loading JPEG image:", e)

def main():
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
