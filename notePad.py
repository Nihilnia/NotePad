from PyQt5.QtWidgets import qApp, QApplication, QTextEdit, QLabel, QPushButton, QAction
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QFileDialog, QMainWindow, QWidget
from PyQt5 import QtGui

import os, sys


class NotePad(QWidget):


    def __init__(self):

        super().__init__()
        self.userInterface()

    def userInterface(self):

        self.nieRPicture = QLabel()
        self.nieRPicture.setPixmap(QtGui.QPixmap("nieR2.png"))

        #textBox
        self.textBox = QTextEdit()

        #Items
        self.buttonClear = QPushButton("Clear")
        self.buttonSave = QPushButton("Save")
        self.buttonOpen = QPushButton("Open")


        #Layouts
        vBoxNier = QVBoxLayout()
        vBoxNier.addWidget(self.nieRPicture)

        vBoxText = QVBoxLayout()
        vBoxText.addWidget(self.textBox)

        hBoxItems = QHBoxLayout()
        hBoxItems.addWidget(self.buttonClear)
        hBoxItems.addWidget(self.buttonSave)
        hBoxItems.addWidget(self.buttonOpen)

        vBoxRight = QVBoxLayout()
        vBoxRight.addLayout(vBoxText)
        vBoxRight.addLayout(hBoxItems)

        hBoxMain = QHBoxLayout()
        hBoxMain.addLayout(vBoxNier)
        hBoxMain.addLayout(vBoxRight)

        #Click Processes
        self.buttonClear.clicked.connect(self.exitApp)
        self.buttonOpen.clicked.connect(self.openFile)
        self.buttonSave.clicked.connect(self.saveFile)

        self.setLayout(hBoxMain)
        self.show()

    

    def exitApp(self):
        self.textBox.clear()

    def saveFile(self):
        fileWay = QFileDialog.getSaveFileName(self, "Save...", os.getenv("HOME"))
        userFile = open(fileWay[0], "a", encoding = "utf-8")
        userFile.write(self.textBox.toPlainText())
        userFile.close()

    def openFile(self):
        fileWay = QFileDialog.getOpenFileName(self, "Open...", os.getenv("HOME"))
        userFile = open(fileWay[0], "r", encoding = "utf-8")
        self.textBox.setText(userFile.read())
        userFile.close()



class Menu(QMainWindow):

    def __init__(self):

        super().__init__()
        

        self.centerWindow = NotePad()
        self.setCentralWidget(self.centerWindow)
        self.userMenu()

    def userMenu(self):

        #Main Menu Items

        mainMenu = self.menuBar()

        menuFile = mainMenu.addMenu("File")
        menuAbout = mainMenu.addMenu("About")

        #Sub Options

        subOpen = QAction("Open..", self)
        subOpen.setShortcut("Ctrl+O")

        subSave = QAction("Save..", self)
        subSave.setShortcut("Ctrl+S")

        subExit = QAction("Exit..", self)
        subExit.setShortcut("Ctrl+Q")

        subNihil = QAction("Nihil", self)

        menuWhoAmI = menuAbout.addMenu("Created by")

        #Adding to main menu

        menuFile.addAction(subOpen)
        menuFile.addAction(subSave)
        menuFile.addAction(subExit)
        menuWhoAmI.addAction(subNihil)

        menuFile.triggered.connect(self.whenClicked)

        self.show()

    def whenClicked(self, action):

        if action.text() == "Open..":
            self.centerWindow.openFile()
        
        elif action.text() == "Save..":
            self.centerWindow.saveFile()

        elif action.text() == "Exit..":
            qApp.exit()



myApp = QApplication(sys.argv)

createIt = Menu()

sys.exit(myApp.exec_())