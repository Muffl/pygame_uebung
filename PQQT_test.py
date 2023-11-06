from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
 
def windows():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Test mit Muffl")
 
    label = QtWidgets.QLabel(win)
    label.setText("Dies ist ein label")
    label.move(50,50)
 
    win.show()
    sys.exit(app.exec())
 
windows()
