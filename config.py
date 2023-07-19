from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("people_db.db")

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS people (id integer primary key AUTOINCREMENT, firstname VARCHAR(40), lastname VARCHAR(40), phone VARCHAR(20))")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

    def add_new_data_query(self, firstname, lastname, phone):
        sql_query = "INSERT INTO people (firstname, lastname, phone) VALUES (?, ?, ?)"
        self.execute_query_with_params(sql_query, [firstname, lastname, phone])

    def update_data_query(self, firstname, lastname, phone, id):
        sql_query = "UPDATE people SET firstname=?, lastname=?, phone=? WHERE id=?"
        self.execute_query_with_params(sql_query, [firstname, lastname, phone, id])

    def delete_data_query(self, id):
        sql_query = "DELETE FROM people WHERE id=?"
        self.execute_query_with_params(sql_query, [id])
