from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QToolBar, QMessageBox


# MainWindow inherits from QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom MainWindow")
        self.resize(900, 500)

        # Menubar and menus
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("File")
        helpMenu = menuBar.addMenu("Help")

        # Create a custom action
        axnMine = QAction("Custom Action", self)
        axnMine.setStatusTip("Status message for a custom action")
        axnMine.triggered.connect(self.handleActionMine)
        fileMenu.addAction(axnMine)

        # Actions - two different ways of creating an action.

        axnQuit = fileMenu.addAction("Quit")
        axnQuit.triggered.connect(self.quitApp)

        axnAbout = helpMenu.addAction("About")
        axnAbout.triggered.connect(self.handleAbout)

        # Toolbar
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        toolbar.addAction(axnMine)
        toolbar.addSeparator()
        toolbar.addAction(axnAbout)
        toolbar.addSeparator()
        toolbar.addAction(axnQuit)

    # Action handler
    def quitApp(self):
        self.app.quit()

    # Action handler
    def handleActionMine(self):
        print("[event] → Triggered the action...also update the status bar")

        # Status Bar
        self.statusBar().showMessage("Updated...", 2000)

    # About handler
    def handleAbout(self):
        msg = "This is a reference application created by Cory to demo PySide6."
        print("[event] → User clicked About")
        # Status Bar
        self.statusBar().showMessage(msg, 4000)

        # And throw up a message box
        QMessageBox.information(self, "Information", msg)
