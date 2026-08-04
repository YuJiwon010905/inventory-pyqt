# app.py
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from login_dialog import LoginDialog

from main_window_admin import Ui_MainWindow as AdminMainWindow
#from main_window_user import Ui_MainWindow as UserMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginDialog() ### 수정필요

    # 지금은 관리자모드만 구현되어 있어서, 관리자 버전 로그인이 실행되도록 제작함.
    # 사용자 로그인 기능 및 사용자 버전은 추후 구현 예정.
    if login.adminlogin.exec_() == LoginDialog.Accepted: # 사용자 로그인 성공시도 추후 구현 예정.지금은 관리자만 가능
        MainWindow = QMainWindow()
        ui=AdminMainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    else:
        sys.exit(0)


    
    '''elif login.usrlogin.exec_() == LoginDialog.Accepted:
        MainWindow = QMainWindow()
        ui=UserMainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())'''