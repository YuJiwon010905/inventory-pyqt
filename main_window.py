from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, \
    QLabel, QLineEdit, QPushButton, QMessageBox,QComboBox

from db_helper import DB,DB_CONFIG
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("관리자 모드")
        self.db=DB(**DB_CONFIG)

        # 중앙 위젯 및 레이아웃
        central=QWidget()
        self.setCentralWidget(central)
        vbox=QVBoxLayout(central)

        # 상단: 콤보박스. 콤보박스에 따라서 다른 결과 출력.
        combobox=QComboBox()