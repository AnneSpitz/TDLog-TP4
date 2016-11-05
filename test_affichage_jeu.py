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
import pandas

import game
import __main__
import customExceptions

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

#
# class MyMainWindow(QtGui.QMainWindow):
#     def __init__(self, parent=None):
#         super(MyMainWindow, self).__init__(parent)
#         self.form_widget = FormWidget(self)
#         self.setCentralWidget(self.form_widget)
#         self.initUI()
#
#     def initUI(self):
#         self.statusBar()
#
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('Event sender')
#         self.show()
#
#     def buttonClicked(self):
#         sender = self.sender()
#         self.statusBar().showMessage(sender.text() + ' was pressed')
#
#
# class FormWidget(QtGui.QWidget):
#     def __init__(self, parent):
#         super(FormWidget, self).__init__(parent)
#         # self.layout = QtGui.QVBoxLayout(self)
#         self.initButton(parent)
#
#     def initButton(self, parent):
#         grid = QtGui.QGridLayout()
#         self.setLayout(grid)
#
#         names = ['Cls', 'Bck', '', 'Close',
#                  '7', '8', '9', '/',
#                  '4', '5', '6', '*',
#                  '1', '2', '3', '-',
#                  '0', '.', '=', '+']
#
#         positions = [(i, j) for i in range(5) for j in range(4)]
#
#         for position, name in zip(positions, names):
#
#             if name == '':
#                 continue
#             button = QtGui.QPushButton(name)
#             button.clicked.connect(parent.buttonClicked)
#             grid.addWidget(button, *position)
#
#             # self.statusBar()
#
#         self.setGeometry(300, 300, 290, 150)
#
#
# def main():
#     app = QtGui.QApplication(sys.argv)
#     foo = MyMainWindow()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()


# class MainWindow(QtGui.QMainWindow):
#     def __init__(self,parent=None):
#        super(MainWindow, self).__init__(parent)
#        self.setupUi(self)
#        self.numbers = 4
#        ...

# app = QtGui.QApplication(sys.argv)
# dmw = DesignerMainWindow()
# dmw.show()
# sys.exit(app.exec_()) #this works, but pops the window right away
#
#
# def newWin():
#     app = QtGui.QApplication(sys.argv)
#     dwm = MainWindow()
#     sys.exit(app.exec_())
#     return dwn
#
# a = newWin()    # application is created now
# a.numbers = 10  # do something
# a.show()        # should pop me the window now
#
#
# class App(QtGui.QApplication):
#     def __init__(self, args):
#         QtGui.QApplication.__init__(self,args)
#         self.window = MainWindow()
#
#     def doSomething(self, ii):
#         self.window.numbers = ii
#
#     def show(self):
#         self.window.show()
#         sys.exit(self.exec_())
# a = App(sys.argv)
# a.doSomething(12) #updates numbers alternately a.window.numbers = 12
# a.show()          #pops the window!

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


class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self)
        self.setCentralWidget(self.form_widget)
        self.initUI()

    def initUI(self):
        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        sender.setText("LOL")
        self.statusBar().showMessage(sender.text() + ' was pressed')


class FormWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
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

        self.setGeometry(300, 300, 290, 150)


def main():
    app = QtGui.QApplication(sys.argv)
    foo = MyMainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
