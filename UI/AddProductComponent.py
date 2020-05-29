# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddProductComponent.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QDialog

from Utils import openDB


class AddComponentWidget(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(1105, 682)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(50, 30, 30, 10)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.iDLabel = QtWidgets.QLabel(Dialog)
        self.iDLabel.setObjectName("iDLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.iDLabel)
        self.ID = QtWidgets.QLineEdit(Dialog)
        self.ID.setObjectName("ID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ID)
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.componentName = QtWidgets.QLineEdit(Dialog)
        self.componentName.setObjectName("componentName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.componentName)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.parentID = QtWidgets.QLineEdit(Dialog)
        self.parentID.setObjectName("parentID")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.parentID)
        self.Label_5 = QtWidgets.QLabel(Dialog)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.isLifeRemind = QtWidgets.QLineEdit(Dialog)
        self.isLifeRemind.setObjectName("isLifeRemind")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.isLifeRemind)
        self.Label_7 = QtWidgets.QLabel(Dialog)
        self.Label_7.setObjectName("Label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_7)
        self.startDate = QtWidgets.QLineEdit(Dialog)
        self.startDate.setObjectName("startDate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.startDate)
        self.Label_9 = QtWidgets.QLabel(Dialog)
        self.Label_9.setObjectName("Label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_9)
        self.isUsedCountLimit = QtWidgets.QLineEdit(Dialog)
        self.isUsedCountLimit.setObjectName("isUsedCountLimit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.isUsedCountLimit)
        self.Label_11 = QtWidgets.QLabel(Dialog)
        self.Label_11.setObjectName("Label_11")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_11)
        self.havaUsedCount = QtWidgets.QLineEdit(Dialog)
        self.havaUsedCount.setObjectName("havaUsedCount")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.havaUsedCount)
        self.Label_13 = QtWidgets.QLabel(Dialog)
        self.Label_13.setObjectName("Label_13")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Label_13)
        self.createTime = QtWidgets.QLineEdit(Dialog)
        self.createTime.setObjectName("createTime")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.createTime)
        self.Label_15 = QtWidgets.QLabel(Dialog)
        self.Label_15.setObjectName("Label_15")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.Label_15)
        self.updateTime = QtWidgets.QTextEdit(Dialog)
        self.updateTime.setObjectName("updateTime")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.updateTime)
        self.horizontalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(30, 30, 50, 10)
        self.formLayout_2.setHorizontalSpacing(15)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.productNO = QtWidgets.QLineEdit(Dialog)
        self.productNO.setObjectName("productNO")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.productNO)
        self.Label_3 = QtWidgets.QLabel(Dialog)
        self.Label_3.setObjectName("Label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.componentTypeID = QtWidgets.QLineEdit(Dialog)
        self.componentTypeID.setObjectName("componentTypeID")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.componentTypeID)
        self.displayOrderLabel = QtWidgets.QLabel(Dialog)
        self.displayOrderLabel.setObjectName("displayOrderLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.displayOrderLabel)
        self.displayOrder = QtWidgets.QLineEdit(Dialog)
        self.displayOrder.setObjectName("displayOrder")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.displayOrder)
        self.Label_6 = QtWidgets.QLabel(Dialog)
        self.Label_6.setObjectName("Label_6")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_6)
        self.life = QtWidgets.QLineEdit(Dialog)
        self.life.setObjectName("life")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.life)
        self.Label_8 = QtWidgets.QLabel(Dialog)
        self.Label_8.setObjectName("Label_8")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_8)
        self.daysBefore = QtWidgets.QLineEdit(Dialog)
        self.daysBefore.setObjectName("daysBefore")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.daysBefore)
        self.Label_10 = QtWidgets.QLabel(Dialog)
        self.Label_10.setObjectName("Label_10")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_10)
        self.maxUsedCount = QtWidgets.QLineEdit(Dialog)
        self.maxUsedCount.setObjectName("maxUsedCount")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.maxUsedCount)
        self.Label_12 = QtWidgets.QLabel(Dialog)
        self.Label_12.setObjectName("Label_12")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_12)
        self.createID = QtWidgets.QLineEdit(Dialog)
        self.createID.setObjectName("createID")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.createID)
        self.Label_14 = QtWidgets.QLabel(Dialog)
        self.Label_14.setObjectName("Label_14")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Label_14)
        self.updateID = QtWidgets.QLineEdit(Dialog)
        self.updateID.setObjectName("updateID")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.updateID)
        self.Label_16 = QtWidgets.QLabel(Dialog)
        self.Label_16.setObjectName("Label_16")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.Label_16)
        self.remark = QtWidgets.QTextEdit(Dialog)
        self.remark.setObjectName("remark")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.remark)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.conserveButton = QtWidgets.QPushButton(Dialog)
        self.conserveButton.setObjectName("conserveButton")
        self.horizontalLayout_2.addWidget(self.conserveButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.bindButton(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "新建产品组件"))
        self.iDLabel.setText(_translate("Dialog", "ID:"))
        self.Label_2.setText(_translate("Dialog", "组件名称："))
        self.Label_4.setText(_translate("Dialog", "父组件："))
        self.Label_5.setText(_translate("Dialog", "寿命提醒："))
        self.Label_7.setText(_translate("Dialog", "寿命起始日期："))
        self.Label_9.setText(_translate("Dialog", "使用次数限制:"))
        self.Label_11.setText(_translate("Dialog", "已经使用次数："))
        self.Label_13.setText(_translate("Dialog", "创建时间："))
        self.Label_15.setText(_translate("Dialog", "修改时间"))
        self.Label.setText(_translate("Dialog", "产品编号："))
        self.Label_3.setText(_translate("Dialog", "组件类型名称："))
        self.displayOrderLabel.setText(_translate("Dialog", "DisplayOrder:"))
        self.Label_6.setText(_translate("Dialog", "寿命(天):"))
        self.Label_8.setText(_translate("Dialog", "距到期提醒(天)："))
        self.Label_10.setText(_translate("Dialog", "最多使用次数:"))
        self.Label_12.setText(_translate("Dialog", "创建人员："))
        self.Label_14.setText(_translate("Dialog", "修改人员："))
        self.Label_16.setText(_translate("Dialog", "备注："))
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
        productNO = self.productNO.text()
        componentName = self.componentName.text()
        componentTypeID = self.componentTypeID.text()
        parentID = self.parentID.text()
        displayOrder = self.displayOrder.text()
        isLifeRemind = self.isLifeRemind.text()
        life = self.life.text()
        startDate = self.startDate.text()
        daysBefore = self.daysBefore.text()
        isUsedCountLimit = self.isUsedCountLimit.text()
        maxUsedCount = self.maxUsedCount.text()
        haveUsedCount = self.maxUsedCount.text()
        createID = self.createID.text()
        createTime = self.createTime.text()
        updateTime = self.updateTime.toPlainText()
        updateID = self.updateID.text()
        remark = self.remark.toPlainText()

        # 如果必要的信息都不为空
        if ID == "" or productNO == "" or componentName == "" or componentTypeID == "":
            print(QMessageBox.information(QDialog(), "提示", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(ID, componentName, productNO)
            if num == 0:
                return
            import time
            createTime = time.strftime("%Y-%m-%d %H:%M:%S")
            insert_sql = "INSERT INTO T_Product_Component VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '--', '%s', '--', '%s', '%s')" % (ID, productNO, componentName, componentTypeID, parentID, displayOrder, isLifeRemind, life, startDate, daysBefore, isUsedCountLimit, maxUsedCount, haveUsedCount,createTime, createTime, remark)
            self.query.exec(insert_sql)
            self.db.commit()
            confirm = QMessageBox.information(QDialog(), "提示", "组件新建成功！", QMessageBox.Yes, QMessageBox.Yes)
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
        productNO = self.productNO.text()
        componentName = self.componentName.text()
        componentTypeID = self.componentTypeID.text()
        parentID = self.parentID.text()
        displayOrder = self.displayOrder.text()
        isLifeRemind = self.isLifeRemind.text()
        life = self.life.text()
        startDate = self.startDate.text()
        daysBefore = self.daysBefore.text()
        isUsedCountLimit = self.isUsedCountLimit.text()
        maxUsedCount = self.maxUsedCount.text()
        haveUsedCount = self.maxUsedCount.text()
        createID = self.createID.text()
        createTime = self.createTime.text()
        updateTime = self.updateTime.toPlainText()
        updateID = self.updateID.text()
        remark = self.remark.toPlainText()

        # 如果必要的信息都不为空
        if ID == "" or productNO == "" or componentName == "" or componentTypeID == "":
            print(QMessageBox.information(QDialog(), "提示", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(ID, componentName, productNO)
            if num == 0:
                return
            import time
            updateTime = time.strftime("%Y-%m-%d %H:%M:%S")
            insert_sql = "INSERT INTO T_Product_Component VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '--', '%s', '--', '%s', '%s')" % (ID, productNO, componentName, componentTypeID, parentID, displayOrder, isLifeRemind, life, startDate, daysBefore, isUsedCountLimit, maxUsedCount, haveUsedCount,createTime, updateTime, remark)
            self.query.exec(insert_sql)
            self.db.commit()
            confirm = QMessageBox.information(QDialog(), "提示", "组件更新成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                self.dialog.close()

        # # 如果必要的信息都不为空
        # if componentTypeName == "" or displayOrder == "" or ID == "" or displayOrder == "":
        #     print(QMessageBox.warning(QDialog(), "警告", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
        #     return
        # else:
        #     num = self.checkOn(ID, componentTypeName)
        #     if num == 0:
        #         return
        #     import time
        #     updateTime = time.strftime("%Y-%m-%d %H:%M:%S")
        #     insert_sql = "INSERT INTO T_Product_ComponentType VALUES ('%s', '%s', '%s', '--', '%s', '--', '%s', '%s')" % (ID, componentTypeName, displayOrder, createTime, updateTime, remark)
        #     self.query.exec(insert_sql)
        #     self.db.commit()
        #     confirm = QMessageBox.information(QDialog(), "提示", "组件类型更改成功！", QMessageBox.Yes, QMessageBox.Yes)
        #     if confirm == QMessageBox.Yes:
        #         self.dialog.close()
        pass

    def checkOn(self, ID, componentName, productNO):
        """
        检查ID, 组件名称和产品号是否合理
        :return:
        """
        self.db = openDB()
        self.query = QSqlQuery()
        sql = "SELECT * FROM T_Product_Component WHERE ID = '%s'" % ID
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.information(QDialog(), "提示", "ID已存在，请更换后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        sql = "SELECT * FROM T_Product_ComponentType WHERE ComponentName = '%s'" % componentName
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.information(QDialog(), "提示", "该组件已存在！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        sql = "SELECT * FROM T_Product WHERE ProductNO = '%s'" % productNO
        self.query.exec(sql)
        if not self.query.next():
            print(QMessageBox.information(QDialog(), "提示", "产品编号不存在！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        return 1

    def updateData(self, list, queryModel):
        """
        修改产品批次信息
        :param list:
        :return:
        """
        self.label.setText("修改产品组件")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda :self.updateButtonEvent(queryModel))
        self.ID.setText(list[0])
        self.productNO.setText(list[1])
        self.componentName.setText(list[2])
        self.componentTypeID.setText(list[3])
        self.parentID.setText(list[4])
        self.displayOrder.setText(list[5])
        self.isLifeRemind.setText(list[6])
        self.life.setText(list[7])
        self.startDate.setText(list[8])
        self.daysBefore.setText(list[9])
        self.isUsedCountLimit.setText(list[10])
        self.maxUsedCount.setText(list[11])
        self.maxUsedCount.setText(list[12])
        self.createID.setText(list[13])
        self.createTime.setText(list[14])
        self.updateTime.setText(list[15])
        self.updateID.setText(list[16])
        self.remark.setText(list[17])
