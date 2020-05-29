# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddComponentTypeView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QDialog

from Utils import openDB


class AddComponentTypeWidget(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 687)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLable = QtWidgets.QLabel(Dialog)
        self.titleLable.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.titleLable.setFont(font)
        self.titleLable.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLable.setIndent(-1)
        self.titleLable.setObjectName("titleLable")
        self.verticalLayout.addWidget(self.titleLable)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(50, 30, 50, -1)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.iDLabel = QtWidgets.QLabel(Dialog)
        self.iDLabel.setObjectName("iDLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.iDLabel)
        self.ID = QtWidgets.QLineEdit(Dialog)
        self.ID.setObjectName("ID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ID)
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.componentTypeName = QtWidgets.QLineEdit(Dialog)
        self.componentTypeName.setObjectName("componentTypeName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.componentTypeName)
        self.disPlayOrderLabel = QtWidgets.QLabel(Dialog)
        self.disPlayOrderLabel.setObjectName("disPlayOrderLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.disPlayOrderLabel)
        self.disPlayOrder = QtWidgets.QLineEdit(Dialog)
        self.disPlayOrder.setObjectName("disPlayOrder")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.disPlayOrder)
        self.Label_3 = QtWidgets.QLabel(Dialog)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.updateTime = QtWidgets.QLineEdit(Dialog)
        self.updateTime.setObjectName("updateTime")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.updateTime)
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.remark = QtWidgets.QTextEdit(Dialog)
        self.remark.setObjectName("remark")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.remark)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.updateID = QtWidgets.QLineEdit(Dialog)
        self.updateID.setObjectName("updateID")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.updateID)
        self.Label_5 = QtWidgets.QLabel(Dialog)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.createTime = QtWidgets.QLineEdit(Dialog)
        self.createTime.setObjectName("createTime")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.createTime)
        self.Label_6 = QtWidgets.QLabel(Dialog)
        self.Label_6.setObjectName("Label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_6)
        self.createID = QtWidgets.QLineEdit(Dialog)
        self.createID.setObjectName("createID")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.createID)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 80, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.conserveButton = QtWidgets.QPushButton(Dialog)
        self.conserveButton.setObjectName("conserveButton")
        self.horizontalLayout.addWidget(self.conserveButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.bindButton(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.titleLable.setText(_translate("Dialog", "新建组件类型"))
        self.iDLabel.setText(_translate("Dialog", "ID："))
        self.Label.setText(_translate("Dialog", "组件名称:"))
        self.disPlayOrderLabel.setText(_translate("Dialog", "DisPlayOrder："))
        self.Label_3.setText(_translate("Dialog", "修改时间："))
        self.Label_2.setText(_translate("Dialog", "备注："))
        self.Label_4.setText(_translate("Dialog", "修改人员："))
        self.Label_5.setText(_translate("Dialog", "创建时间："))
        self.Label_6.setText(_translate("Dialog", "创建人员："))
        self.conserveButton.setText(_translate("Dialog", "保存"))
        self.cancelButton.setText(_translate("Dialog", "取消"))

    def bindButton(self, Dialog):
        """
        hsj 按钮绑定事件
        :param Dialog: 弹窗本身
        :return:
        """
        self.conserveButton.clicked.connect(lambda: self.conserveButtonEvent(Dialog))
        self.cancelButton.clicked.connect(lambda: self.cancelButtonEvent(Dialog))

    def conserveButtonEvent(self, Dialog):
        """
        hsj 新建产品组件界面的保存按钮事件
        :return:
        """
        ID = self.ID.text()
        componentTypeName = self.componentTypeName.text()
        displayOrder = self.disPlayOrder.text()
        remark = self.remark.toPlainText()

        # 如果必要的信息都不为空
        if componentTypeName == "" or displayOrder == "" or ID == "" or displayOrder == "":
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(ID, componentTypeName)
            if num == 0:
                return
            import time
            createTime = time.strftime("%Y-%m-%d %H:%M:%S")
            insert_sql = "INSERT INTO T_Product_ComponentType VALUES ('%s', '%s', '%s', '--', '%s', '--', '%s', '%s')" % (ID, componentTypeName, displayOrder, createTime, createTime, remark)
            self.query.exec(insert_sql)
            self.db.commit()
            confirm = QMessageBox.information(QDialog(), "提示", "组件类型新建成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                Dialog.close()

    def cancelButtonEvent(self, Dialog):
        """
        取消按钮事件
        :return:
        """
        Dialog.close()

    def updateButtonEvent(self, queryModel):
        """
        更新界面按钮事件
        :param queryModel:
        :return:
        """
        queryModel.delete()
        ID = self.ID.text()
        componentTypeName = self.componentTypeName.text()
        displayOrder = self.disPlayOrder.text()
        remark = self.remark.toPlainText()
        createTime = self.createTime.text()
        # 如果必要的信息都不为空
        if componentTypeName == "" or displayOrder == "" or ID == "" or displayOrder == "":
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(ID, componentTypeName)
            if num == 0:
                return
            import time
            updateTime = time.strftime("%Y-%m-%d %H:%M:%S")
            insert_sql = "INSERT INTO T_Product_ComponentType VALUES ('%s', '%s', '%s', '--', '%s', '--', '%s', '%s')" % (ID, componentTypeName, displayOrder, createTime, updateTime, remark)
            self.query.exec(insert_sql)
            self.db.commit()
            confirm = QMessageBox.information(QDialog(), "提示", "组件类型更改成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                self.dialog.close()

    def checkOn(self, ID, componentTypeName):
        """
        检查批次号和产品号是否合理
        :return:
        """
        self.db = openDB()
        self.query = QSqlQuery()
        sql = "SELECT * FROM T_Product_ComponentType WHERE ID = '%s'" % ID
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.information(QDialog(), "提示", "ID已存在，请更换后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        sql = "SELECT * FROM T_Product_ComponentType WHERE ComponentTypeName = '%s'" % componentTypeName
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.information(QDialog(), "提示", "该组件类型已存在！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        return 1

    def updateData(self, list, queryModel):
        """
        修改产品批次信息
        :param list:
        :return:
        """
        self.titleLable.setText("修改组件类型")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda :self.updateButtonEvent(queryModel))
        self.ID.setText(list[0])
        self.componentTypeName.setText(list[1])
        self.disPlayOrder.setText(list[2])
        self.createID.setText(list[3])
        self.createTime.setText(list[4])
        self.updateID.setText(list[5])
        self.updateTime.setText(list[6])
        self.remark.setText(list[7])
