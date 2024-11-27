from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow
import sys


app = QApplication(sys.argv)

window = MainWindow(app)
window.setWindowTitle("Prototype PySide6")
window.show()

app.exec()
