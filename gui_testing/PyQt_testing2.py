import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a Title
        self.setWindowTitle('Ashmit\'s OP Program')

        # Set QFormLayout
        formLayout = qtw.QFormLayout()
        self.setLayout(formLayout)

        # Create A Label to Greet
        myLabel = qtw.QLabel('Hello World!')
        myLabel.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(myLabel)

        # Create an Entry box
        f_name = qtw.QLineEdit(self,
                               placeholderText='First Name:')
        l_name = qtw.QLineEdit(self,
                               placeholderText='Last Name:')

        # Create a Button
        helloButton = qtw.QPushButton('Enter', clicked=lambda: command())
        self.layout().addWidget(helloButton)

        # Add rows to app
        formLayout.addRow(myLabel)
        formLayout.addRow(f_name)
        formLayout.addRow(l_name)
        formLayout.addRow(helloButton)


        # Button Command
        def command():
            myLabel.setText(f'Hello {f_name.text()} {l_name.text()}!')


        # Show the app
        self.show()



app = qtw.QApplication([])
mw = MainWindow()

# Run the app
app.exec_()










