# 일반 사용자 vs admin 으로 로그인 (관리자)
from PyQt5.QtWidgets import QDialog,QVBoxLayout,QFormLayout,\
    QLineEdit,QPushButton, QMessageBox
from db_helper import DB,DB_CONFIG

class AdminLogin(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("관리자 로그인")
        self.db=DB(**DB_CONFIG)

        self.adminname=QLineEdit()
        self.pw=QLineEdit()
        self.pw.setEchoMode(QLineEdit.Password)

        form=QFormLayout()
        form.addRow("관리자명", self.adminname)
        form.addRow("비밀번호", self.pw)

        self.btn_login=QPushButton("로그인🔐")
        self.btn_login.clocked.connect(self.try_login)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.btn_login)
        self.setLayout(layout)     

    def try_login(self):
        adminname=self.adminname.text().strip()
        pw=self.pw.text().strip()
        if not adminname or not pw:
            QMessageBox.warning(self, "오류","관리자명과 비밀번호를 모두 입력하세요")
            return
        ok=self.db.verify_admin(adminname,pw)
        if ok:
            self.accept()
        else:
            QMessageBox.critical(self,"실패", "관리자명 혹은 비밀번호가 틀립니다")