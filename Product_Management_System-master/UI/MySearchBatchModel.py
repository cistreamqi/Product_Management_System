import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import (QApplication, QHeaderView, QStyle, QStyleOptionButton, QTableView)
from PyQt5.QtCore import (pyqtSignal, Qt, QAbstractTableModel, QModelIndex, QRect, QVariant)

from Utils import openDB


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


class MySearchTableModel(QAbstractTableModel):
    def __init__(self, table, headerRow, parent=None):
        """
        hsj 初始化TableModel
        :param table: 查询的表
        :param headerRow: 查询显示界面的标题
        :param parent:
        """
        super(MySearchTableModel, self).__init__(parent)

        self.table = table
        self.setTableInformation()

        # 总数据
        self.totalData = self.getData()

        # hsj 每页显示的信息数, 总页数
        self.perPageNum = 10
        self.currentPage = 0
        self.data_list = []
        self.totalPage = self.getTotalPage()
        # print(self.totalPage)

        self.initList()

        # self.data_list = self.getData()
        # Keep track of which object are checked
        # self.headerRow = ["批次号", "ID", "产品编号", "交付日期", "交付单位", "交付人员", "接收单位", "接收人员", "创建人员ID", "创建时间", "修改人员ID", "修改时间", "备注"]
        self.headerRow = headerRow
        self.checkList = ['Unchecked' for i in range(len(self.data_list))]

    def setTableInformation(self):
        """
        hsj 设置表相关信息
        :return:
        """
        if self.table == "T_Product_BatchDetail":
            self.tableKey = "BatchNO"
            self.tableLength = 13
            # 要查询的第二张表的名字
            self.tableForeign = "T_Product"
            self.tableForeignKey = "ProductNO"
            self.tableForeignKeyPosition = 2
            self.tableForeignLength = 14
        elif self.table == "T_Product":
            self.tableKey = "ProductNO"
            self.tableLength = 14
            self.tableForeign = "T_Product_Component"
            self.tableForeignKey = "ID"
            self.tableForeignKeyPosition = 1  # 在本表中是根据本表主键在外表中查询
            self.tableForeignLength = 18
        elif self.table == "T_Product_ComponentType":
            self.tableKey = "ID"
            self.tableLength = 8
        elif self.table == "T_Product_Component":
            self.tableKey = "ID"
            self.tableLength = 18

    def initList(self):
        """
        hsj 初始化界面数据
        :return:
        """
        if len(self.totalData) <= self.perPageNum:
            self.data_list = self.totalData
        else:
            self.data_list = self.totalData[:self.perPageNum]

    def delete(self):
        """
        hsj 删除选中的数据
        :return:
        """
        db = openDB()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                # sql = "DELETE FROM T_Product_BatchDetail WHERE BatchNO = '%s'" % (self.data_list[i][0])
                sql = "DELETE FROM %s WHERE %s = '%s'" % (self.table, self.tableKey,self.data_list[i][0])
                query.exec(sql)
                # sql = "DELETE FROM T_Product WHERE ProductNO = '%s'" % (self.data_list[i][2])
                # query.exec(sql)
                # sql = "DELETE FROM T_Product_Component WHERE ProductID = '%s'" % (self.data_list[i][2])
                # query.exec(sql)
        db.commit()
        self.refreshPage()

    def deleteProduct(self):
        """
        hsj 删除选中的产品，并且关联删除
        :return:
        """
        db = openDB()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "DELETE FROM T_Product_BatchDetail WHERE ProductNO = '%s'" % (self.data_list[i][0])
                query.exec(sql)
                sql = "DELETE FROM T_Product_Component WHERE ProductNO = '%s'" % (self.data_list[i][0])
                query.exec(sql)
                sql = "DELETE FROM T_Product WHERE ProductNO = '%s'" % (self.data_list[i][0])
                query.exec(sql)
        db.commit()
        self.refreshPage()

    def deleteCompoment(self):
        """
        hsj 删除选中的组件及关联删除
        :return:
        """
        db = openDB()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "DELETE FROM %s WHERE %s = '%s'" % (self.table, self.tableKey, self.data_list[i][0])
                query.exec(sql)
                # sql = "DELETE FROM T_Product WHERE ProductNO = '%s'" % (self.data_list[i][2])
                # query.exec(sql)
                sql = "DELETE FROM %s WHERE ParentID = '%s' AND ProductNO = '%s'" % (self.table, self.data_list[i][0], self.data_list[i][1])
                print(sql)
                query.exec(sql)
                # sql = "DELETE FROM T_Product_Component WHERE ProductID = '%s'" % (self.data_list[i][2])
                # query.exec(sql)
        db.commit()
        self.refreshPage()

    def selectSingleTableForeign(self):
        """
        hsj 查询单个外键表信息
        :return:
        """
        list = []
        db = openDB()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "SELECT * FROM %s WHERE %s = '%s'" % (self.tableForeign, self.tableForeignKey, self.data_list[i][self.tableForeignKeyPosition])
                query.exec(sql)
                break
        if query.next():
            list = [str(query.value(i)) for i in range(self.tableForeignLength)]
        # print(list)
        return list

    def selectSingleTable(self):
        """
        hsj 查询单个表信息
        :return:
        """
        list = []
        db = openDB()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "SELECT * FROM %s WHERE %s = '%s'" % (self.table, self.tableKey, self.data_list[i][0])
                query.exec(sql)
                break
        if query.next():
            list = [str(query.value(i)) for i in range(self.tableLength)]
        # print(list)
        return list

    def searchTable(self, select_condition, content):
        """
        hsj 根据条件查询信息，并返回界面
        :param select_condition: 列名
        :param content: 具体查询条件
        :return:
        """
        list = []
        db = openDB()
        query = QSqlQuery()
        sql = "SELECT * FROM %s WHERE %s = '%s' ORDER BY %s" % (self.table, select_condition, content, self.tableKey)
        # print(sql)
        query.exec(sql)
        while query.next():
            list.append([str(query.value(i)) for i in range(self.tableLength)])
        # print(list)
        self.searchRefreshPage(list)
        self.update()

    def getData(self):
        """
        获取所有数据
        :return:
        """
        results = []
        db = openDB()
        query = QSqlQuery()
        sql = "SELECT * FROM %s ORDER BY %s" % (self.table, self.tableKey)
        # print(sql)
        a = query.exec(sql)
        # print('a', a)
        while(query.next()):
            results.append([query.value(i) for i in range(self.tableLength)])
        # print(results)
        return results

    def update(self):
        self.beginResetModel()
        self.checkList = ['Unchecked' for i in range(len(self.data_list))]
        # print(self.data_list)
        self.endResetModel()

    def getTotalPage(self):
        """
        hsj 得到总页数
        :return:
        """
        return len(self.totalData) // self.perPageNum + 1

    def prePage(self):
        """
        上一页数据及页面更新
        :return:
        """
        self.currentPage = self.currentPage - 1
        self.setCurrentData()
        self.update()


    def nextPage(self):
        """
        hsj 下一页数据及页面更新
        :return:
        """
        self.currentPage = self.currentPage + 1
        self.setCurrentData()
        # print("---------------",len(self.data_list))
        self.update()

    def lastPage(self):
        """
        hsj 最后一页数据及页面更新
        :return:
        """
        self.currentPage = self.currentPage + 1
        self.data_list = self.totalData[self.currentPage * self.perPageNum:]
        self.update()

    def setCurrentData(self):
        """
        hsj 设置当前页码的数据
        :return:
        """
        self.data_list = self.totalData[self.currentPage * self.perPageNum:(self.currentPage + 1) * self.perPageNum]

    def refreshPage(self):
        """
        hsj 添加，删除后，刷新当前页内的信息
        :return:
        """
        self.totalData = self.getData()
        self.totalPage = self.getTotalPage()
        self.data_list = self.totalData[self.currentPage * self.perPageNum:(self.currentPage + 1) * self.perPageNum]

    def searchRefreshPage(self, list_data):
        """
        hsj 查询后更新界面
        :return:
        """
        self.totalData = list_data
        self.totalPage = self.getTotalPage()
        self.currentPage = 0
        self.initList()



    # hsj 下面是一般不需要调用，且不需要更改的方法
    def rowCount(self, QModelIndex):
        # print(len(self.data_list))
        return len(self.data_list)

    def columnCount(self, QModelIndex):
        return len(self.headerRow)

    def data(self, index, role):
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return self.data_list[row][col]
        elif role == Qt.CheckStateRole:
            if col == 0:
                return Qt.Checked if self.checkList[row] == 'Checked' else Qt.Unchecked
        elif role == Qt.ToolTipRole:
            if col == 0:
                return self.checkList[row]
        elif role == Qt.TextAlignmentRole:
            return QVariant(Qt.AlignCenter)
        return QVariant()

    def setData(self, index, value, role):
        row = index.row()
        col = index.column()
        if role == Qt.CheckStateRole and col == 0:
            self.checkList[row] = 'Checked' if value == Qt.Checked else 'Unchecked'
            # print(self.checkList)
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
        self.update()
        self.beginResetModel()
        if isOn:
            self.checkList = ['Checked' for i in range(len(self.data_list))]
        else:
            self.checkList = ['Unchecked' for i in range(len(self.data_list))]
        self.endResetModel()


if __name__ == '__main__':
    a = QApplication(sys.argv)
    tableView = QTableView()
    headerRow = ["批次号", "ID", "产品编号", "交付日期", "交付单位", "交付人员", "接收单位", "接收人员", "创建人员ID", "创建时间", "修改人员ID", "修改时间", "备注"]
    myModel = MySearchTableModel("T_Product_BatchDetail", headerRow)
    tableView.setModel(myModel)
    header = CheckBoxHeader()
    tableView.setHorizontalHeader(header)
    header.clicked.connect(myModel.headerClick)
    tableView.showMaximized()
    tableView.show()
    a.exec_()