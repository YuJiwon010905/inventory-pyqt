# 일반 사용자 vs admin 으로 로그인 (관리자)
from PyQt5.QtWidgets import QDialog,QVBoxLayout,QFormLayout,\
    QLineEdit,QPushButton, QMessageBox
from db_helper import DB,DB_CONFIG

class SignUp(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("회원가입")
        self.db=DB(**DB_CONFIG)

        self.signup_name=QLineEdit()
        self.signup_email=QLineEdit()
        self.signup_pw=QLineEdit()
        self.signup_addr=QLineEdit()

        self.signup_pw.setEchoMode(QLineEdit.Password)

        form=QFormLayout()
        form.addRow("이름", self.signup_name)
        form.addRow("이메일",self.signup_email)
        form.addRow("비밀번호", self.signup_pw)
        form.addRow("주소", self.signup_addr)

        self.btn_signup=QPushButton("회원가입🔐")
        self.btn_signup.clicked.connect(self.try_signup)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.btn_signup)
        self.setLayout(layout)     

    def try_signup(self):
        name=self.signup_name.text().strip()
        email=self.signup_email.text().strip()
        pw=self.signup_pw.text().strip()
        addr=self.signup_addr.text().strip()

        if not name or not email or not pw or not addr:
            QMessageBox.warning(self, "오류","회원가입 정보를 모두 입력하세요")
            return
        ok=self.db.insert_account(name,email,pw,addr)
        if ok:
            QMessageBox.information(self, "성공","회원가입이 완료되었습니다! 😊")
            self.accept()
        else:
            QMessageBox.critical(self,"실패", "잠시 후 다시 시도해보세요")