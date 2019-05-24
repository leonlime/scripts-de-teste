#!/usr/bin/env python

from PySide2 import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import sys

class MainWindow(QMainWindow):

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("introducao pyside2")

		self.fieldName = QLineEdit() # campo de texto
		lbName = QLabel('nome: ')

		layout = QGridLayout() # usa o grid layout onde podemos colocar wigets
		layout.addWidget(lbName, 0, 0)
		layout.addWidget(self.fieldName, 0, 1)

		widget = QWidget() # wifget principal
		widget.setLayout(layout) # seta o layout a ser usado

		self.setCentralWidget(widget)


if __name__ == '__main__':
	app = QApplication(sys.argv)

	window = MainWindow()

	window.show()

	app.exec_()







