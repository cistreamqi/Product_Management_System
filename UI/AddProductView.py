# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddProductView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QDialog

from Utils import openDB


class AddProductWidget(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog

        Dialog.setObjectName("Dialog")
        Dialog.resize(824, 748)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(50, 30, 50, 30)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.productNO = QtWidgets.QLineEdit(Dialog)
        self.productNO.setObjectName("productNO")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.productNO)
        self.iDLabel = QtWidgets.QLabel(Dialog)
        self.iDLabel.setObjectName("iDLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.iDLabel)
        self.ID = QtWidgets.QLineEdit(Dialog)
        self.ID.setObjectName("ID")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ID)
        self.productModelIDLabel = QtWidgets.QLabel(Dialog)
        self.productModelIDLabel.setObjectName("productModelIDLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.productModelIDLabel)
        self.productModelID = QtWidgets.QLineEdit(Dialog)
        self.productModelID.setObjectName("productModelID")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.productModelID)
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.life = QtWidgets.QLineEdit(Dialog)
        self.life.setObjectName("life")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.life)
        self.Label_3 = QtWidgets.QLabel(Dialog)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.startDate = QtWidgets.QLineEdit(Dialog)
        self.startDate.setObjectName("startDate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.startDate)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.daysbefore = QtWidgets.QLineEdit(Dialog)
        self.daysbefore.setObjectName("daysbefore")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.daysbefore)
        self.Label_5 = QtWidgets.QLabel(Dialog)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.isUsedCountLimit = QtWidgets.QLineEdit(Dialog)
        self.isUsedCountLimit.setObjectName("isUsedCountLimit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.isUsedCountLimit)
        self.Label_6 = QtWidgets.QLabel(Dialog)
        self.Label_6.setObjectName("Label_6")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Label_6)
        self.maxUsedCount = QtWidgets.QLineEdit(Dialog)
        self.maxUsedCount.setObjectName("maxUsedCount")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.maxUsedCount)
        self.Label_7 = QtWidgets.QLabel(Dialog)
        self.Label_7.setObjectName("Label_7")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.Label_7)
        self.havaUsedCount = QtWidgets.QLineEdit(Dialog)
        self.havaUsedCount.setObjectName("havaUsedCount")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.havaUsedCount)
        self.Label_8 = QtWidgets.QLabel(Dialog)
        self.Label_8.setObjectName("Label_8")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.Label_8)
        self.createID = QtWidgets.QLineEdit(Dialog)
        self.createID.setObjectName("createID")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.createID)
        self.Label_9 = QtWidgets.QLabel(Dialog)
        self.Label_9.setObjectName("Label_9")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.Label_9)
        self.createTime = QtWidgets.QLineEdit(Dialog)
        self.createTime.setObjectName("createTime")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.createTime)
        self.Label_10 = QtWidgets.QLabel(Dialog)
        self.Label_10.setObjectName("Label_10")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.Label_10)
        self.updateID = QtWidgets.QLineEdit(Dialog)
        self.updateID.setObjectName("updateID")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.updateID)
        self.Label_11 = QtWidgets.QLabel(Dialog)
        self.Label_11.setObjectName("Label_11")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.Label_11)
        self.updateTime = QtWidgets.QLineEdit(Dialog)
        self.updateTime.setObjectName("updateTime")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.updateTime)
        self.remarkLabel = QtWidgets.QLabel(Dialog)
        self.remarkLabel.setObjectName("remarkLabel")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.remarkLabel)
        self.remark = QtWidgets.QTextEdit(Dialog)
        self.remark.setObjectName("remark")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.remark)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
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
        self.label.setText(_translate("Dialog", "新建产品"))
        self.Label.setText(_translate("Dialog", "产品编号:"))
        self.iDLabel.setText(_translate("Dialog", "ID："))
        self.productModelIDLabel.setText(_translate("Dialog", "ProductModelID："))
        self.Label_2.setText(_translate("Dialog", "寿命(天)："))
        self.Label_3.setText(_translate("Dialog", "寿命起始日期："))
        self.Label_4.setText(_translate("Dialog", "距到期提醒(天)："))
        self.Label_5.setText(_translate("Dialog", "使用次数限制:"))
        self.Label_6.setText(_translate("Dialog", "最多使用次数："))
        self.Label_7.setText(_translate("Dialog", "已经使用次数："))
        self.Label_8.setText(_translate("Dialog", "创建人员："))
        self.Label_9.setText(_translate("Dialog", "创建时间："))
        self.Label_10.setText(_translate("Dialog", "更新人员："))
        self.Label_11.setText(_translate("Dialog", "更新时间："))
        self.remarkLabel.setText(_translate("Dialog", "备注："))
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
        hsj 新建产品界面的保存按钮事件
        :return:
        """
        productNO = self.productNO.text()
        ID = self.ID.text()
        ProductModelID = self.productModelID.text()
        life = self.life.text()
        startDate = self.startDate.text()
        daysBefore = self.daysbefore.text()
        isUsedCountLimit = self.isUsedCountLimit.text()
        maxUsedCount = self.maxUsedCount.text()
        haveUsedCount = self.maxUsedCount.text()
        createID = self.createID.text()
        createTime = self.createTime.text()
        updateID = self.createID.text()
        updateTime = self.updateTime.text()
        remark = self.remark.toPlainText()

        # 如果必要的信息都不为空
        if productNO == "" or life == "" or startDate == "" or daysBefore == "":
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(productNO)
            if num == 0:
                return
            import time
            createTime = time.strftime("%Y-%m-%d %H:%M:%S")
            insert_sql = "INSERT INTO T_Product VALUES ('%s', '--', '--', '%s', '%s', '%s', '%s', '%s', '%s', '--', '%s', '--', '%s', '%s')" % (productNO, life, startDate, daysBefore, isUsedCountLimit, maxUsedCount, haveUsedCount, createTime, createTime, remark)
            self.query.exec(insert_sql)
            self.db.commit()
            confirm = QMessageBox.information(QDialog(), "提示", "产品新建成功！", QMessageBox.Yes, QMessageBox.Yes)
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
        productNO = self.productNO.text()
        ID = self.ID.text()
        ProductModelID = self.productModelID.text()
        life = self.life.text()
        startDate = self.startDate.text()
        daysBefore = self.daysbefore.text()
        isUsedCountLimit = self.isUsedCountLimit.text()
        maxUsedCount = self.maxUsedCount.text()
        haveUsedCount = self.maxUsedCount.text()
        createID = self.createID.text()
        createTime = self.createTime.text()
        updateID = self.createID.text()
        updateTime = self.updateTime.text()
        remark = self.remark.toPlainText()

        # 如果必要的信息都不为空
        if productNO == "" or life == "" or startDate == "" or daysBefore == "":
            print(QMessageBox.information(QDialog(), "提示", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(productNO)
            if num == 0:
                return
            import time
            updateTime = time.strftime("%Y-%m-%d %H:%M:%S")
            insert_sql = "INSERT INTO T_Product VALUES ('%s', '--', '--', '%s', '%s', '%s', '%s', '%s', '%s', '--', '%s', '--', '%s', '%s')" % (productNO, life, startDate, daysBefore, isUsedCountLimit, maxUsedCount, haveUsedCount, createTime, updateTime, remark)
            self.query.exec(insert_sql)
            self.db.commit()
            confirm = QMessageBox.information(QDialog(), "提示", "产品更改成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                self.dialog.close()

    def checkOn(self, productNO):
        """
        检查产品号是否合理
        :return:
        """
        self.db = openDB()
        self.query = QSqlQuery()
        sql = "SELECT * FROM T_Product WHERE ProductNO = '%s'" % productNO
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.information(QDialog(), "提示", "产品已存在，请更换后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        return 1

    def updateData(self, list, queryModel):
        """
        修改产品批次信息
        :param list:
        :return:
        """
        self.label.setText("修改产品信息")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda :self.updateButtonEvent(queryModel))
        self.productNO.setText(list[0])
        self.ID.setText(list[1])
        self.productModelID.setText(list[2])
        self.life.setText(list[3])
        self.startDate.setText(list[4])
        self.daysbefore.setText(list[5])
        self.isUsedCountLimit.setText(list[6])
        self.maxUsedCount.setText(list[7])
        self.maxUsedCount.setText(list[8])
        self.createID.setText(list[9])
        self.createTime.setText(list[10])
        self.createID.setText(list[11])
        self.updateTime.setText(list[12])
        self.remark.setText(list[13])

