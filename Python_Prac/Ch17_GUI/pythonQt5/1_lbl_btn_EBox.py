# Import necessary modules from PyQt5
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

# Define a custom MainWindow class that inherits from QWidget
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()  # Call the constructor of the QWidget class
        
        #set title to the window 
        self.setWindowTitle("MY GUI")
        #set size of window
        self.setGeometry(300,150,400,200)
        #set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        #create label 
        l1=qtw.QLabel("Hello Word!")
        #changin font size of label
        l1.setFont(qtg.QFont("Helvetica",24))
        #set the widget on layout
        self.layout().addWidget(l1)

        #create entry box
        e1=qtw.QLineEdit()
        #name to entrybox
        e1.setObjectName("name_feild")
        e1.setText("")
        #set the entrybox on layout
        self.layout().addWidget(e1)
        #Create the buuton
        btn_press=qtw.QPushButton("Press Me!",clicked=lambda:press_it())
        #Set on layout 
        self.layout().addWidget(btn_press)


        #create label 
        l2=qtw.QLabel("You Selected")
        #changin font size of label
        l2.setFont(qtg.QFont("Helvetica",24))
        #set the widget on layout
        self.layout().addWidget(l2)

        #Create a comboBox
        combo1=qtw.QComboBox(self)#if you want to add item at running time the after self, ,editable=True,insertPolicy=qtw.QComboBox.InsertAtTop)

        #add items to comboBox
        combo1.addItem("Banana","Good Fruit")#first itemname second itemData
        #add multiple items at atime
        combo1.addItems(["Mango","Ornage","Aple"])
        #add item at specifice positions
        combo1.insertItem(3,"Aro")#first index second itemname
        #add multiple item at specific positios
        combo1.insertItems(4,["one","tow","Three"])

        #add combo widget on screen
        self.layout().addWidget(combo1)


        btn_select=qtw.QPushButton("Press Me!",clicked=lambda:select())
        #Set on layout 
        self.layout().addWidget(btn_select)

        # Show the MainWindow widget
        self.show()
        def press_it():
            #add the name to label
            l1.setText(f"Hello {e1.text()}")
            e1.setText("")

        def select():
            #show itemname
            l2.setText(f"You Selected {combo1.currentText()}!")
            #show ItemDate
            #l2.setText(f"You Selected {combo1.currentData}")
            #Show itemindex
            #l2.setText(f"You Selected {combo1.currentIndex}")


# Create a QApplication instance, which manages the GUI application's control flow
app = qtw.QApplication([])

# Create an instance of MainWindow, which is a QWidget
mw = MainWindow()

# Run the application's event loop until the application is exited
app.exec_()
