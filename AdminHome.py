import sys

import qdarkstyle
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QStackedWidget

from PyQt5.QtCore import QSize, Qt

from UI.AddProductBatchDetailView import AddProductBatchDetailWidget
from UI.SelectProductBatchView import SelectProductBatchWidget
from Thread.SearchProductBatchThread import SearchProductBatchDetailThread


class AdminHome(QWidget):
    """登录后的主界面，该界面采用侧边栏+内容区相结合的方式"""
    def __init__(self):
        super(AdminHome, self).__init__()
        # 设置窗口大小和标题
        self.resize(900, 600)
        self.setWindowTitle("欢迎使用产品管理系统")
        # 导入QListWidget的qss样式
        with open("./QListWidgetQSS.qss", 'r') as f:
            self.list_style = f.read()
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        # 左侧选项表
        self.left_widget = QListWidget()
        self.left_widget.setStyleSheet(self.list_style)
        self.main_layout.addWidget(self.left_widget)
        # 右侧内容区
        self.right_widget = QStackedWidget(self)
        self.main_layout.addWidget(self.right_widget)

        self.__setUpUI()

    def __setUpUI(self):
        """加载界面UI"""
        # list和右边窗口的index对应绑定
        self.left_widget.currentRowChanged.connect(self.display)
        # 去掉边框
        self.left_widget.setFrameShape(QListWidget.NoFrame)
        # 隐藏滚动条
        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str = ['产品批次查询', '产品批次新建', '删除产品', '入库信息管理', '出库信息管理', '信息统计', '维护方式管理', '维护记录管理', '故障诊断与处理', '知识库管理', '用户管理']
        # 根据list_str设置对应UI
        url_list = ["self.setSelectProductBatchDetailView", "self.addProductBatchDetailView", "self.test", "self.test", "self.test", "self.test", "self.test", "self.test", "self.test", "self.test", "self.test", "self.test"]

        for i in range(len(list_str)):
            # 左侧选项的添加
            self.item = QListWidgetItem(list_str[i], self.left_widget)
            self.item.setSizeHint(QSize(30, 60))
            self.item.setTextAlignment(Qt.AlignCenter)
            # 根据对应函数设置右侧显示内容
            eval(url_list[i] + "()")


    def display(self, i):
        self.right_widget.setCurrentIndex(i)

    def setRightWidget(self, layout):
        """
        设置右部QStackWidget中的内容
        :param layout: 含有相应视图的右部布局
        :return:
        """
        widget = QWidget()
        widget.setLayout(layout)
        self.right_widget.addWidget(widget)

    def setRightWidget1(self, myWidget):
        """
        设置右部QStackWidget中的内容
        :param layout: 含有相应视图的右部布局
        :return:
        """
        widget = QWidget()
        myWidget.setupUi(widget)
        self.right_widget.addWidget(widget)

    def addProductBatchDetailView(self):
        self.tt = AddProductBatchDetailWidget()
        self.setRightWidget1(self.tt)

    def setSelectProductBatchDetailView(self):
        """设置产品批次查询的UI"""
        self.myWidget = SelectProductBatchWidget()
        self.table_thread = SearchProductBatchDetailThread()
        self.table_thread.update_date.connect(self.updateSearchProductBatchDetailWidget)
        self.table_thread.start()
        self.setRightWidget1(self.myWidget)

    def updateSearchProductBatchDetailWidget(self):
        """
        更新产品批次查询的视图
        :return:
        """
        print(11111)
        self.myWidget.queryModel.select()

    def test(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./Images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = AdminHome()
    mainMindow.show()
    sys.exit(app.exec_())


