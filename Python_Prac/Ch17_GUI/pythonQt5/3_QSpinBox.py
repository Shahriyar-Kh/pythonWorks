import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #Set title
        self.setWindowTitle("Spin Box")
        #set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        #create one label
        lbl1=qtw.QLabel("You Picked!")
        #change the font size of lbl1
        lbl1.setFont(qtg.QFont("Arial bold",14))
        #set lbl on screen
        self.layout().addWidget(lbl1)

        #create spinbox
        spbox1=qtw.QSpinBox(self,
                            value=10,
                            maximum=100,
                            minimum=0,
                            singleStep=5,
                            prefix="Your Order Is ",
                            suffix=" Rs")
        #set on screen
        self.layout().addWidget(spbox1)


        #create Pushbutton
        btn_pick=qtw.QPushButton("Picked Me!",clicked=lambda:picked_it())
        self.layout().addWidget(btn_pick)

        def picked_it():
            lbl1.setText(f"You Picked {spbox1.value()}")



        #show the custom app
        self.show()
#create the instance of QApplicatiobn which manages the GUI application's control flow
app=qtw.QApplication([])

#create instance of custom class
mw=MainWindow()

#Run appliation
app.exec_()