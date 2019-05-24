#!/usr/bin/env python

from PySide2 import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import sys

class MainWindow(QMainWindow):

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("introducao pyside2")


if __name__ == '__main__':
	app = QApplication(sys.argv)

	window = MainWindow()

	window.show()

	app.exec_()







