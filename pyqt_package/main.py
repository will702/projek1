import sys
from PyQt6.QtWidgets  import QApplication,QWidget,QLineEdit ,QPushButton,QTextEdit,QBoxLayout
from PyQt6.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Type To Write'
                            )
        self.setWindowIcon('')

app = QApplication(sys.argv)
#Loops
window = MyApp()
window.show()

app.exec()