# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddKnowledgeBase.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QTableView, QHeaderView
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QDialog

#from Utils import openDB
from Utils import openDB


class AddKBMWidge(object):
    def setupUi(self, Form):
        self.form=Form
        Form.setObjectName("Form")
        Form.resize(532, 540)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(50, 20, 50, -1)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.NumLabel = QtWidgets.QLabel(Form)
        self.NumLabel.setObjectName("NumLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.NumLabel)
        self.Num = QtWidgets.QLineEdit(Form)
        self.Num.setObjectName("Num")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Num)
        self.DataitemLabel = QtWidgets.QLabel(Form)
        self.DataitemLabel.setObjectName("DataitemLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.DataitemLabel)
        self.Dataitem = QtWidgets.QLineEdit(Form)
        self.Dataitem.setObjectName("Dataitem")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Dataitem)
        self.DatatypeLabel = QtWidgets.QLabel(Form)
        self.DatatypeLabel.setObjectName("DatatypeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.DatatypeLabel)
        self.Datatype = QtWidgets.QLineEdit(Form)
        self.Datatype.setObjectName("Datatype")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Datatype)
        self.remarkLabel = QtWidgets.QLabel(Form)
        self.remarkLabel.setObjectName("remarkLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.remarkLabel)
        self.remark = QtWidgets.QTextEdit(Form)
        self.remark.setObjectName("remark")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.remark)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.conserveButton = QtWidgets.QPushButton(Form)
        self.conserveButton.setObjectName("conserveButton")
        self.horizontalLayout_4.addWidget(self.conserveButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_4.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        self.bindButton(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "新增知识分类"))
        self.NumLabel.setText(_translate("Form", "序号："))
        self.DataitemLabel.setText(_translate("Form", "数据项："))
        self.DatatypeLabel.setText(_translate("Form", "数据类型："))
        self.remarkLabel.setText(_translate("Form", "备注："))
        self.conserveButton.setText(_translate("Form", "保存"))
        self.cancelButton.setText(_translate("Form", "取消"))

    def bindButton(self, Form):
        """
        czq 按钮绑定事件
        :param Dialog: 弹窗本身
        :return:
        """
        self.conserveButton.clicked.connect(lambda: self.conserveButtonEvent(Form))
        self.cancelButton.clicked.connect(lambda: self.cancelButtonEvent(Form))

    def conserveButtonEvent(self, Form):
        """
        hsj 新建产品组件界面的保存按钮事件
        :return:
        """
        Num = self.Num.text()
        Dataitem=self.Dataitem.text()
        Datatype=self.Datatype.text()
        remark = self.remark.toPlainText()

        # 如果必要的信息都不为空
        if Num == "" or Dataitem == "" or Datatype == "" :
            print(QMessageBox.information(QDialog(), "提示", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(Num)
            if num == 0:
                return
            insert_sql = "INSERT INTO T_Knowladge_Base_Mangement VALUES ('%s', '%s', '%s', '%s')" % (Num,Dataitem,Datatype, remark)
            self.query.exec(insert_sql)
            self.db.commit()
            confirm = QMessageBox.information(QDialog(), "提示", "新建成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                Form.close()

    def cancelButtonEvent(self, Form):
        """
        取消按钮事件
        :return:
        """
        Form.close()

    def updateButtonEvent(self, queryModel):
        """
        更新界面按钮事件
        :param queryModel:
        :return:
        """
        queryModel.delete()
        print(('shank'))
        Num = self.Num.text()
        Dataitem=self.Dataitem.text()
        Datatype=self.Datatype.text()
        remark = self.remark.toPlainText()

        # 如果必要的信息都不为空
        if Num == "" or Dataitem == "" or Datatype == "" :
            print(QMessageBox.information(QDialog(), "提示", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(Num)
            if num == 0:
                return
            insert_sql = "INSERT INTO T_Knowladge_Base_Mangement VALUES ('%s', '%s', '%s', '%s')" % (Num,Dataitem,Datatype, remark)
            self.query.exec(insert_sql)
            self.db.commit()
            confirm = QMessageBox.information(QDialog(), "提示", "更改成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                self.form.close()

    def checkOn(self, Num):
        """
        检查序号是否合理
        :return:
        """
        self.db = openDB()
        self.query = QSqlQuery()
        sql = "SELECT * FROM T_Knowladge_Base_Mangement WHERE Num = '%s'" % Num
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.information(QDialog(), "提示", "序号已存在，请更换后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        self.query.exec(sql)
        return 1

    def updateData(self, list, queryModel):
        """
        修改产品批次信息
        :param list:
        :return:
        """
        self.label.setText("修改知识分类")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda :self.updateButtonEvent(queryModel))
        self.Num.setText(str(list[0]))
        self.Dataitem.setText(str(list[1]))
        self.Datatype.setText(str(list[2]))
        self.remark.setText(str(list[3]))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = AddKBMWidge()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
