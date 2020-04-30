import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *
import qdarkstyle
from SignIn import SignInWidget
from SignUp import SignUpWidget
import sip
from AdminHome import AdminHome
#from UserHome import UserHome
from ChangePasswordDialog import ChangePasswordDialog


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.widget = SignInWidget()

        #self.resize(900, 600)

        self.setWindowTitle("产品管理系统")
        self.setCentralWidget(self.widget)
        bar = self.menuBar()
        self.Menu = bar.addMenu("菜单栏")

        self.signUpAction = QAction("注册", self)
        self.signInAction = QAction("登录", self)
        self.ChangePasswordAction =QAction("修改密码",self)
        #self.signInAction = QAction("登录", self)
        self.quitSignInAction = QAction("退出登录", self)
        self.quitAction = QAction("退出系统", self)
        self.Menu.addAction(self.signUpAction)
        self.Menu.addAction(self.signInAction)
        self.Menu.addAction(self.ChangePasswordAction)
        #self.Menu.addAction(self.signInAction)
        self.Menu.addAction(self.quitSignInAction)
        self.Menu.addAction(self.quitAction)

        #self.signUpAction.setEnabled(True)
        # Zgg
        self.signUpAction.setEnabled(False)

        self.ChangePasswordAction.setEnabled(True)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(False)
        self.widget.is_admin_signal.connect(self.adminSignIn)
        self.widget.is_User_signal[str].connect(self.UserSignIn)
        self.Menu.triggered[QAction].connect(self.menuTriggered)

        # Zgg 全屏
        self.showFullScreen()
        #self.showMaximized()

    def adminSignIn(self):
        sip.delete(self.widget)
        self.widget = AdminHome()
        self.setCentralWidget(self.widget)
        self.ChangePasswordAction.setEnabled(False)
        self.signUpAction.setEnabled(True)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(True)

    def UserSignIn(self, UserId):
        sip.delete(self.widget)
        #self.widget = UserHome(UserId)
        self.setCentralWidget(self.widget)

        # Zgg 普通用户登陆后可以修改密码
        self.ChangePasswordAction.setEnabled(True)

        #self.signUpAction.setEnabled(True)
        # Zgg 普通用户无法注册
        self.signUpAction.setEnabled(False)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(True)

    def menuTriggered(self, q):
        if(q.text()=="修改密码"):
            changePsdDialog=ChangePasswordDialog(self)
            changePsdDialog.show()
            changePsdDialog.exec_()
        if (q.text() == "注册"):
            sip.delete(self.widget)
            self.widget = SignUpWidget()
            self.setCentralWidget(self.widget)
            #self.widget.User_signup_signal[str].connect(self.UserSignIn)
            self.signUpAction.setEnabled(False)
            self.ChangePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(True)
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "退出登录"):
            sip.delete(self.widget)
            self.widget = SignInWidget()
            self.setCentralWidget(self.widget)
            self.widget.is_admin_signal.connect(self.adminSignIn)
            #self.widget.is_User_signal[str].connect(self.UserSignIn)
            self.signUpAction.setEnabled(True)
            self.ChangePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(False)
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "登录"):
            sip.delete(self.widget)
            self.widget = SignInWidget()
            self.setCentralWidget(self.widget)
            self.widget.is_admin_signal.connect(self.adminSignIn)
            self.widget.is_User_signal[str].connect(self.UserSignIn)
            self.signUpAction.setEnabled(True)
            self.ChangePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(False)
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "退出系统"):
            qApp = QApplication.instance()
            qApp.quit()
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./Images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = Main()
    mainMindow.show()
    sys.exit(app.exec_())
