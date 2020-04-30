import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
import time
from PyQt5.QtSql import *


class AddProductDialog(QDialog):
    add_Product_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(AddProductDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("添加书籍")

    def setUpUI(self):
        # 书名，书号，作者，分类，添加数量.出版社,出版日期
        # 书籍分类：哲学类、社会科学类、政治类、法律类、军事类、经济类、文化类、教育类、体育类、语言文字类、艺术类、历史类、地理类、天文学类、生物学类、医学卫生类、农业类
        ProductCategory = ["哲学", "社会科学", "政治", "法律", "军事", "经济", "文化", "教育", "体育", "语言文字", "艺术", "历史"
            , "地理", "天文学", "生物学", "医学卫生", "农业"]
        self.resize(300, 400)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Label控件
        self.titlelabel = QLabel("  添加书籍")
        self.ProductNameLabel = QLabel("书    名:")
        self.ProductIdLabel = QLabel("书    号:")
        self.authNameLabel = QLabel("作    者:")
        self.categoryLabel = QLabel("分    类:")
        self.publisherLabel = QLabel("出 版 社:")
        self.publishDateLabel = QLabel("出版日期:")
        self.addNumLabel = QLabel("数    量:")

        # button控件
        self.addProductButton = QPushButton("添 加")

        # lineEdit控件
        self.ProductNameEdit = QLineEdit()
        self.ProductIdEdit = QLineEdit()
        self.authNameEdit = QLineEdit()
        self.categoryComboBox = QComboBox()
        self.categoryComboBox.addItems(ProductCategory)
        self.publisherEdit = QLineEdit()
        self.publishTime = QDateTimeEdit()
        self.publishTime.setDisplayFormat("yyyy-MM-dd")
        # self.publishDateEdit = QLineEdit()
        self.addNumEdit = QLineEdit()

        self.ProductNameEdit.setMaxLength(10)
        self.ProductIdEdit.setMaxLength(6)
        self.authNameEdit.setMaxLength(10)
        self.publisherEdit.setMaxLength(10)
        self.addNumEdit.setMaxLength(12)
        self.addNumEdit.setValidator(QIntValidator())

        # 添加进formlayout
        self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.ProductNameLabel, self.ProductNameEdit)
        self.layout.addRow(self.ProductIdLabel, self.ProductIdEdit)
        self.layout.addRow(self.authNameLabel, self.authNameEdit)
        self.layout.addRow(self.categoryLabel, self.categoryComboBox)
        self.layout.addRow(self.publisherLabel, self.publisherEdit)
        self.layout.addRow(self.publishDateLabel, self.publishTime)
        self.layout.addRow(self.addNumLabel, self.addNumEdit)
        self.layout.addRow("", self.addProductButton)

        # 设置字体
        font = QFont()
        font.setPixelSize(20)
        self.titlelabel.setFont(font)
        font.setPixelSize(14)
        self.ProductNameLabel.setFont(font)
        self.ProductIdLabel.setFont(font)
        self.authNameLabel.setFont(font)
        self.categoryLabel.setFont(font)
        self.publisherLabel.setFont(font)
        self.publishDateLabel.setFont(font)
        self.addNumLabel.setFont(font)

        self.ProductNameEdit.setFont(font)
        self.ProductIdEdit.setFont(font)
        self.authNameEdit.setFont(font)
        self.publisherEdit.setFont(font)
        self.publishTime.setFont(font)
        self.categoryComboBox.setFont(font)
        self.addNumEdit.setFont(font)

        # button设置
        font.setPixelSize(16)
        self.addProductButton.setFont(font)
        self.addProductButton.setFixedHeight(32)
        self.addProductButton.setFixedWidth(140)

        # 设置间距
        self.titlelabel.setMargin(8)
        self.layout.setVerticalSpacing(10)

        self.addProductButton.clicked.connect(self.addProductButtonCicked)

    def addProductButtonCicked(self):
        ProductName = self.ProductNameEdit.text()
        ProductId = self.ProductIdEdit.text()
        authName = self.authNameEdit.text()
        ProductCategory = self.categoryComboBox.currentText()
        publisher = self.publisherEdit.text()
        publishTime = self.publishTime.text()
        addProductNum = self.addNumEdit.text()
        if (
                ProductName == "" or ProductId == "" or authName == "" or ProductCategory == "" or publisher == "" or publishTime == "" or addProductNum == ""):
            print(QMessageBox.warning(self, "警告", "有字段为空，添加失败", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            addProductNum = int(addProductNum)
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName('./db/ProductManagement.db')
            db.open()
            query = QSqlQuery()
            # 如果已存在，则update Product表的现存量，剩余可借量，不存在，则insert Product表，同时insert buyordrop表
            sql = "SELECT * FROM Product WHERE ProductId='%s'" % (ProductId)
            query.exec_(sql)
            if (query.next()):
                sql = "UPDATE Product SET NumStorage=NumStorage+%d,NumCanBorrow=NumCanBorrow+%d WHERE ProductId='%s'" % (
                    addProductNum, addProductNum, ProductId)
            else:
                sql = "INSERT INTO Product VALUES ('%s','%s','%s','%s','%s','%s',%d,%d,0)" % (
                    ProductName, ProductId, authName, ProductCategory, publisher, publishTime, addProductNum, addProductNum)
            query.exec_(sql)
            db.commit()
            # 插入droporinsert表
            timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            sql = "INSERT INTO buyordrop VALUES ('%s','%s',1,%d)" % (ProductId, timenow, addProductNum)
            query.exec_(sql)
            db.commit()
            print(QMessageBox.information(self, "提示", "添加书籍成功!", QMessageBox.Yes, QMessageBox.Yes))
            self.add_Product_success_signal.emit()
            self.close()
            self.clearEdit()
        return

    def clearEdit(self):
        self.ProductNameEdit.clear()
        self.ProductIdEdit.clear()
        self.authNameEdit.clear()
        self.addNumEdit.clear()
        self.publisherEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./Images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = AddProductDialog()
    mainMindow.show()
    sys.exit(app.exec_())
