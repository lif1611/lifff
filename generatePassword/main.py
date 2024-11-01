from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

from table import*
import sys
import pickle

app=QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

sys.exit(app.exec())