# 일반 사용자 vs admin 으로 로그인
from PyQt5.QtWidgets import QDialog,QVBoxLayout,QLabel,QPushButton
from db_helper import DB,DB_CONFIG

from userlogin import *
from adminlogin import *
from signup import *

class LoginDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login")
        self.db=DB(**DB_CONFIG)
        self.usrlogin=UserLogin()
        self.adminlogin=AdminLogin()
        self.signup=SignUp()
        self.loginmode=''

        self.btn_usr=QPushButton("사용자🙂")
        self.btn_admin=QPushButton("관리자🛡️")
        ## 회원가입
        self.btn_signup=QPushButton("회원가입🙌")

        self.btn_usr.clicked.connect(self.try_userlogin) #사용자 로그인
        self.btn_admin.clicked.connect(self.try_adminlogin) # 관리자 로그인
        self.btn_signup.clicked.connect(self.try_signup)

        mode_layout=QVBoxLayout()
        mode_layout.addWidget(QLabel("로그인 모드를 선택하세요"))  
        mode_layout.addWidget(self.btn_usr)
        mode_layout.addWidget(self.btn_admin)
        mode_layout.addWidget(self.btn_signup)
        self.setLayout(mode_layout)

    def try_userlogin(self): # user login 을 선택할 경우
        # 아니 근데 이거 로그인 창 닫아도 MAIN 함수가 실행되는 부분에 대해 해결 필요
        if self.usrlogin.exec_()==QDialog.Accepted:
            self.loginmode="user"
        self.accept()


    def try_adminlogin(self): # admin login 을 선택할 경우
        #self.loginmode="admin"
        if self.adminlogin.exec_()==QDialog.Accepted:
            self.loginmode="admin"
        self.accept()

    # 회원가입을 선택하는 경우
    def try_signup(self):
        if self.signup.exec_()==QDialog.Accepted: # 회원가입 정보를 올바르게 잘 입력 시
            self.loginmode="signup" 
        # 그러면 다시 로그인 창으로 넘어가서 로그인 정상적으로 하면 됨.