# 일반 사용자 vs admin 으로 로그인
from PyQt5.QtWidgets import QDialog,QVBoxLayout,QLabel,QPushButton
from db_helper import DB,DB_CONFIG

from userlogin import *
from adminlogin import *

class LoginDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login")
        self.db=DB(**DB_CONFIG)
        self.usrlogin=UserLogin()
        self.adminlogin=AdminLogin()

        self.btn_usr=QPushButton("사용자🙂")
        self.btn_admin=QPushButton("관리자🛡️")

        self.btn_usr.clicked.connect(self.try_userlogin) #사용자 로그인
        self.btn_admin.clicked.connect(self.try_adminlogin) # 관리자 로그인

        mode_layout=QVBoxLayout()
        mode_layout.addWidget(QLabel("로그인 모드를 선택하세요"))  
        mode_layout.addWidget(self.btn_usr)
        mode_layout.addWidget(self.btn_admin)
        self.setLayout(mode_layout)

    def try_userlogin(self): # user login 을 선택할 경우
        #self.usrlogin=UserLogin()
        self.loginmode="user"
        self.usrlogin.exec_()
        self.accept()


    def try_adminlogin(self): # admin login 을 선택할 경우
        #self.adminlogin=AdminLogin()
        self.loginmode="admin"
        self.adminlogin.exec_()
        self.accept()
