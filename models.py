from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel

from ui_main import Ui_GeneralWindow
from ui_record import Ui_RecordTableWindow

from config import Data


class GW(QMainWindow):
    def __init__(self):
        super(GW, self).__init__()
        self.ui = Ui_GeneralWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        self.ui.pushButton.clicked.connect(self.open_new_people_window)
        self.ui.pushButton_2.clicked.connect(self.open_new_people_window)
        self.ui.pushButton_3.clicked.connect(self.delete_current_people)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('people')
        self.model.select()
        self.ui.tableView.setModel(self.model)

    def open_new_people_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_RecordTableWindow()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == 'Добавить данные':
            self.ui_window.BT_Save.clicked.connect(self.add_new_people)
        else:
            self.ui_window.BT_Save.clicked.connect(self.edit_current_people)

    def add_new_people(self):
        firstname = self.ui_window.LE_Name.text()
        lastname = self.ui_window.LE_Family.text()
        phone = self.ui_window.LE_Phone.text()

        self.conn.add_new_data_query(firstname, lastname, phone)

        self.view_data()
        self.new_window.close()

    def edit_current_people(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = self.ui.tableView.model().data(index)

        firstname = self.ui_window.LE_Name.text()
        lastname = self.ui_window.LE_Family.text()
        phone = self.ui_window.LE_Phone.text()

        if firstname != "" and phone != "":
            self.conn.update_data_query(firstname, lastname, phone, id)

            self.view_data()
            self.new_window.close()

    def delete_current_people(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = self.ui.tableView.model().data(index)

        self.conn.delete_data_query(id)
        self.view_data()
