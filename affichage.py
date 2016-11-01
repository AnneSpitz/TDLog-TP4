#!/usr/bin/python
# -*- coding: utf-8 -*-

# /////////////////////////////////////////////////////
#
# TP3 du module de Techniques de Développement LOGiciel
#
# Groupe 3
# TP réalisé par RIU Clément et SPITZ Anne
#
# Rendu le 26 octobre 2016
#
# /////////////////////////////////////////////////////


import sys
from PyQt4 import QtGui, QtCore

"""
class MyMainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):

        super(MyMainWindow, self).__init__(parent)
        self.a = QtGui.QStatusBar(self)
        self.form_widget = Example(self)
        self.setCentralWidget(self.form_widget)


class Example(QtGui.QWidget):
    def __init__(self, parent):
        super(Example, self).__init__()

        #self.a = QtGui.QStatusBar(self)
        self.initUI()




    def initUI(self):

        grid = QtGui.QGridLayout()
        self.setLayout(grid)


        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QtGui.QPushButton(name)
            button.clicked.connect(self.buttonClicked)
            grid.addWidget(button, *position)
        #grid.addWidget(self.a)
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

    def buttonClicked(self,parent):

        sender = self.sender()
        self.a.showMessage(sender.text() + ' was pressed')
"""

"""
class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.setLayout(self.a)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QtGui.QPushButton(name)
            button.clicked.connect(self.buttonClicked)
            self.a.addWidget(button, *position)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('TRY HARD')
        self.show()

    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')





        class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        btn1 = QtGui.QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
"""
"""
def main():
    app = QtGui.QApplication(sys.argv)
    foo = MyMainWindow()
    ex = Example(foo)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


"""
import sys


class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self)
        self.setCentralWidget(self.form_widget)
        self.initUI()

    def initUI(self):
        """
        btn1 = QtGui.QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        """
        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()


    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
"""
class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.setLayout(self.a)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QtGui.QPushButton(name)
            button.clicked.connect(self.buttonClicked)
            self.a.addWidget(button, *position)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('TRY HARD')
        self.show()"""


class FormWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        #self.layout = QtGui.QVBoxLayout(self)
        self.initButton(parent)

    def initButton(self, parent):
        grid = QtGui.QGridLayout()
        self.setLayout(grid)


        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QtGui.QPushButton(name)
            button.clicked.connect(parent.buttonClicked)
            grid.addWidget(button, *position)

    #self.statusBar()

        self.setGeometry(300, 300, 290, 150)


def main():
    app = QtGui.QApplication(sys.argv)
    foo = MyMainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
