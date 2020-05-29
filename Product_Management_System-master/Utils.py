from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QMessageBox, QDialog


def openDB():
    db = QSqlDatabase.addDatabase("QSQLITE")
    # db.setDatabaseName("../db/ProductManagement_new.db")
    db.setDatabaseName("./db/ProductManagement_new.db")  # 整合框架时使用
    db.open()
    return db


