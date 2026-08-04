# 일반 사용자 vs admin 으로 로그인 (일반사용자)
from PyQt5.QtWidgets import QDialog,QVBoxLayout,QFormLayout,\
    QLineEdit,QPushButton, QMessageBox
from db_helper import DB,DB_CONFIG

class UserLogin(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("사용자 로그인")
        self.db=DB(**DB_CONFIG)

        self.email=QLineEdit()
        self.pw=QLineEdit()
        self.pw.setEchoMode(QLineEdit.Password)

        form=QFormLayout()
        form.addRow("이메일", self.email)
        form.addRow("비밀번호", self.pw)

        self.btn_login=QPushButton("로그인🔐")
        self.btn_login.clicked.connect(self.try_login)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.btn_login)
        self.setLayout(layout)     

    def try_login(self):
        email=self.email.text().strip()
        pw=self.pw.text().strip()
        if not email or not pw:
            QMessageBox.warning(self, "오류","아이디와 비밀번호를 모두 입력하세요")
            return
        ok=self.db.verify_account(email,pw)
        if ok:
            self.email=email
            self.accept()
        else:
            QMessageBox.critical(self,"실패", "아이디 혹은 비밀번호가 틀립니다")