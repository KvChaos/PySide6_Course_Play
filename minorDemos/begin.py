from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import sys



def handleClick(isChecked):
    print( f"[Button clicked]  {isChecked}")



app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle( "First App")

btn = QPushButton()
btn.setText( "Click Me" )
btn.setCheckable(True)
btn.clicked.connect( handleClick )


window.setCentralWidget(btn)
window.show()
app.exec()





