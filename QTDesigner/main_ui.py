import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from dialog_ui import Ui_Dialog


if __name__ == "__main__":  
	app = QApplication(sys.argv) 
	form = QWidget()
	w = Ui_Dialog()
	w.setupUi(form)
	form.show()
	sys.exit(app.exec())