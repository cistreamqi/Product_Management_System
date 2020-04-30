import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
from AddProductDialog import AddProductDialog
from DropProductDialog import DropProductDialog
from ProductStorageViewer import ProductStorageViewer
from UserManage import UserManage

class AdminHome(QWidget):
    def __init__(self):
        super().__init__()
        self.setUpUI()

    def setUpUI(self):
        self.resize(900, 600)
        self.setWindowTitle("欢迎使用产品管理系统")
        self.layout = QHBoxLayout()
        self.buttonlayout = QVBoxLayout()
        self.setLayout(self.layout)

        font = QFont()
        font.setPixelSize(15)
        self.userManageButton = QPushButton("用户管理")
        self.addProductButton = QPushButton("添加产品")
        self.dropProductButton = QPushButton("删除产品")

        # Zgg
        self.ruKuXinXiButton = QPushButton("入库信息管理")
        self.chuKuXinXiButton = QPushButton("出库信息管理")
        self.xinXiTongJiButton = QPushButton("信息统计")
        self.weiBaoFangShiButton = QPushButton("维保方式管理")
        self.weiBaoJiLuButton = QPushButton("维保记录管理")
        self.guZhangZhenDuanButton = QPushButton("故障诊断与处理")
        self.zhiShiKuButton = QPushButton("知识库管理")

        self.userManageButton.setFont(font)
        self.addProductButton.setFont(font)
        self.dropProductButton.setFont(font)
        # Zgg
        self.ruKuXinXiButton.setFont(font)
        self.chuKuXinXiButton.setFont(font)
        self.xinXiTongJiButton.setFont(font)
        self.weiBaoFangShiButton.setFont(font)
        self.weiBaoJiLuButton.setFont(font)
        self.guZhangZhenDuanButton.setFont(font)
        self.zhiShiKuButton.setFont(font)

        self.userManageButton.setFixedWidth(130)
        self.userManageButton.setFixedHeight(40)
        self.addProductButton.setFixedWidth(130)
        self.addProductButton.setFixedHeight(40)
        self.dropProductButton.setFixedWidth(130)
        self.dropProductButton.setFixedHeight(40)

        # Zgg
        self.ruKuXinXiButton.setFixedWidth(130)
        self.chuKuXinXiButton.setFixedWidth(130)
        self.xinXiTongJiButton.setFixedWidth(130)
        self.weiBaoFangShiButton.setFixedWidth(130)
        self.weiBaoJiLuButton.setFixedWidth(130)
        self.guZhangZhenDuanButton.setFixedWidth(130)
        self.zhiShiKuButton.setFixedWidth(130)

        self.ruKuXinXiButton.setFixedHeight(40)
        self.chuKuXinXiButton.setFixedHeight(40)
        self.xinXiTongJiButton.setFixedHeight(40)
        self.weiBaoFangShiButton.setFixedHeight(40)
        self.weiBaoJiLuButton.setFixedHeight(40)
        self.guZhangZhenDuanButton.setFixedHeight(40)
        self.zhiShiKuButton.setFixedHeight(40)

        self.buttonlayout.addWidget(self.addProductButton)
        self.buttonlayout.addWidget(self.dropProductButton)

        self.buttonlayout.addWidget(self.ruKuXinXiButton)
        self.buttonlayout.addWidget(self.chuKuXinXiButton)
        self.buttonlayout.addWidget(self.xinXiTongJiButton)
        self.buttonlayout.addWidget(self.weiBaoFangShiButton)
        self.buttonlayout.addWidget(self.weiBaoJiLuButton)
        self.buttonlayout.addWidget(self.guZhangZhenDuanButton)
        self.buttonlayout.addWidget(self.zhiShiKuButton)

        self.buttonlayout.addWidget(self.userManageButton)

        self.layout.addLayout(self.buttonlayout)
        self.storageView = ProductStorageViewer()
        self.layout.addWidget(self.storageView)

        self.addProductButton.clicked.connect(self.addProductButtonClicked)
        self.dropProductButton.clicked.connect(self.dropProductButtonClicked)
        self.userManageButton.clicked.connect(self.userManage)

        self.userManageButton.clicked.connect(self.ruKuXinXiButtonClicked)
        self.userManageButton.clicked.connect(self.chuKuXinXiButtonClicked)
        self.userManageButton.clicked.connect(self.xinXiTongJiButtonClicked)
        self.userManageButton.clicked.connect(self.weiBaoFangShiButtonClicked)
        self.userManageButton.clicked.connect(self.weiBaoJiLuButtonClicked)
        self.userManageButton.clicked.connect(self.guZhangZhenDuanButtonClicked)
        self.userManageButton.clicked.connect(self.zhiShiKuButtonClicked)


    def addProductButtonClicked(self):
        addDialog = AddProductDialog(self)
        #addDialog.add_Product_success_signal.connect(self.storageView.searchButtonClicked)
        addDialog.show()
        addDialog.exec_()

    def dropProductButtonClicked(self):
        dropDialog = DropProductDialog(self)
        #dropDialog.drop_Product_successful_signal.connect(self.storageView.searchButtonClicked)
        dropDialog.show()
        dropDialog.exec_()

    def userManage(self):
        UserDelete=UserManage(self)
        UserDelete.show()
        UserDelete.exec_()

    def ruKuXinXiButtonClicked(self):
        pass

    def chuKuXinXiButtonClicked(self):
        pass

    def xinXiTongJiButtonClicked(self):
        pass

    def weiBaoFangShiButtonClicked(self):
        pass

    def weiBaoJiLuButtonClicked(self):
        pass

    def guZhangZhenDuanButtonClicked(self):
        pass

    def zhiShiKuButtonClicked(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./Images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = AdminHome()
    mainMindow.show()
    sys.exit(app.exec_())
