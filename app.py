# app.py
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from login_dialog import LoginDialog

from main_window_admin import Ui_MainWindow as AdminMainWindow
from main_window_user import Ui_MainWindow as UserMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginDialog() ### 수정필요

    #if login.adminlogin.exec_() == LoginDialog.Accepted: # 수정 예정
    login.exec_()

    if login.loginmode == "user":
        user_email = login.usrlogin.email
        MainWindow = QMainWindow()
        ui=UserMainWindow()
        ui.setupUi(MainWindow, user_email=user_email)  # 사용자 이메일을 전달
        MainWindow.show()
        sys.exit(app.exec_())

    elif login.loginmode == "admin":
        MainWindow = QMainWindow()
        ui=AdminMainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    elif login.loginmode=="signup":
        sys.exit(app.exec_())

    else:
        sys.exit(0)


    
    '''elif login.usrlogin.exec_() == LoginDialog.Accepted:
        MainWindow = QMainWindow()
        ui=UserMainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())'''