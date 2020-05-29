import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import (QApplication, QHeaderView, QStyle, QStyleOptionButton, QTableView)
from PyQt5.QtCore import (pyqtSignal, Qt, QAbstractTableModel, QModelIndex, QRect, QVariant)


class CheckBoxHeader(QHeaderView):
    clicked = pyqtSignal(bool)

    _x_offset = 3
    _y_offset = 0
    _width = 20
    _height = 20

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(CheckBoxHeader, self).__init__(orientation, parent)
        self.isOn = False

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super(CheckBoxHeader, self).paintSection(painter, rect, logicalIndex)
        painter.restore()

        self._y_offset = int((rect.height()-self._width)/2.)

        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(rect.x() + self._x_offset, rect.y() + self._y_offset, self._width, self._height)
            option.state = QStyle.State_Enabled | QStyle.State_Active
            if self.isOn:
                option.state |= QStyle.State_On
            else:
                option.state |= QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    def mousePressEvent(self, event):
        index = self.logicalIndexAt(event.pos())
        if 0 == index:
            x = self.sectionPosition(index)
            if x + self._x_offset < event.pos().x() < x + self._x_offset + self._width and self._y_offset < event.pos().y() < self._y_offset + self._height:
                if self.isOn:
                    self.isOn = False
                else:
                    self.isOn = True
                self.clicked.emit(self.isOn)
                self.update()
        super(CheckBoxHeader, self).mousePressEvent(event)


class MyModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(MyModel, self).__init__(parent)
        self.result = self.getData()
        # Keep track of which object are checked
        self.data_length = len(self.result)
        self.headerRow = ["批次号", "ID", "产品ID", "交付日期", "交付单位", "交付人员", "接收单位", "接收人员", "创建人员ID", "创建时间", "修改人员ID", "修改时间", "备注"]
        self.checkList = ['Unchecked' for i in range(self.data_length)]


    def rowCount(self, QModelIndex):
        return len(self.checkList)

    def columnCount(self, QModelIndex):
        return len(self.headerRow)

    def data(self, index, role):
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return self.result[row][col]
        elif role == Qt.CheckStateRole:
            if col == 0:
                return Qt.Checked if self.checkList[row] == 'Checked' else Qt.Unchecked
        elif role == Qt.ToolTipRole:
            if col == 0:
                return self.checkList[row]
        return QVariant()

    def setData(self, index, value, role):
        row = index.row()
        col = index.column()
        if role == Qt.CheckStateRole and col == 0:
            self.checkList[row] = 'Checked' if value == Qt.Checked else 'Unchecked'
            print(self.checkList)
        return True

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable
        return Qt.ItemIsEnabled

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.headerRow[section]

    def headerClick(self, isOn):
        self.beginResetModel()
        if isOn:
            self.checkList = ['Checked' for i in range(self.data_length)]
        else:
            self.checkList = ['Unchecked' for i in range(self.data_length)]
        self.endResetModel()

    def getData(self):
        results = []
        n = 0
        db = QSqlDatabase.addDatabase("QSQLITE")
        # db.setDatabaseName("../db/ProductManagement_new.db")
        db.setDatabaseName("./db/ProductManagement_new.db")  # 整合框架时使用
        db.open()
        query = QSqlQuery()
        sql = "SELECT * FROM T_Product_BatchDetail"
        query.exec(sql)
        while(query.next()):
            results.append([query.value(i) for i in range(14)])
        return results


if __name__ == '__main__':
    a = QApplication(sys.argv)
    tableView = QTableView()
    myModel = MyModel()
    tableView.setModel(myModel)
    header = CheckBoxHeader()
    tableView.setHorizontalHeader(header)
    header.clicked.connect(myModel.headerClick)
    tableView.showMaximized()
    tableView.show()
    a.exec_()