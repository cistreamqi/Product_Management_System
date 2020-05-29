

from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QTableView, QHeaderView
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

class SelectrKnowledgeBase(object):
    def setupUi(self, Form):
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
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setContentsMargins(50, 20, 50, -1)
        self.formLayout_4.setHorizontalSpacing(20)
        self.formLayout_4.setVerticalSpacing(10)
        self.formLayout_4.setObjectName("formLayout_4")
        self.NumLabel = QtWidgets.QLabel(Form)
        self.NumLabel.setObjectName("NumLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.NumLabel)
        self.Num = QtWidgets.QLineEdit(Form)
        self.Num.setEnabled(False)
        self.Num.setObjectName("Num")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Num)
        self.DataitemLabel = QtWidgets.QLabel(Form)
        self.DataitemLabel.setObjectName("DataitemLabel")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.DataitemLabel)
        self.Dataitem = QtWidgets.QLineEdit(Form)
        self.Dataitem.setEnabled(False)
        self.Dataitem.setObjectName("Dataitem")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Dataitem)
        self.DatatypeLabel = QtWidgets.QLabel(Form)
        self.DatatypeLabel.setObjectName("DatatypeLabel")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.DatatypeLabel)
        self.Datatype = QtWidgets.QLineEdit(Form)
        self.Datatype.setEnabled(False)
        self.Datatype.setObjectName("Datatype")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Datatype)
        self.remarkLabel = QtWidgets.QLabel(Form)
        self.remarkLabel.setObjectName("remarkLabel")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.remarkLabel)
        self.remark = QtWidgets.QTextEdit(Form)
        self.remark.setEnabled(False)
        self.remark.setObjectName("remark")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.remark)
        self.verticalLayout.addLayout(self.formLayout_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "查看知识分类"))
        self.NumLabel.setText(_translate("Form", "序号："))
        self.DataitemLabel.setText(_translate("Form", "数据项："))
        self.DatatypeLabel.setText(_translate("Form", "数据类型："))
        self.remarkLabel.setText(_translate("Form", "备注："))


    def setData(self, list):
        """
        czq 设置单个产品查询结果
        :param list: 单个查询结果
        :return:
        """
        self.Num.setText(str(list[0]))
        self.Dataitem.setText(str(list[1]))
        self.Datatype.setText(str(list[2]))
        self.remark.setText(str(list[3]))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = SelectrKnowledgeBase()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
