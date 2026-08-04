# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - untitledhzfDmy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import QRect, QCoreApplication, QMetaObject,QSize,Qt
from PyQt5.QtWidgets import (
    QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,\
    QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QPushButton, 
    QMessageBox, QStackedWidget, QSizePolicy, QSpacerItem, QLayout,
    QMenuBar, QStatusBar,QHeaderView,QScrollArea
)
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtGui import QIcon, QPixmap
from db_helper import DB, DB_CONFIG


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, user_email=None):  # 사용자 이메일을 전달받는 매개변수 추가
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        self.db=DB(**DB_CONFIG)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #ffffff;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo_label=QLabel()
        pixmap=QPixmap('subway.png')
        scaled_pixmap = pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_label.setPixmap(scaled_pixmap)
        self.verticalLayout.addWidget(self.logo_label, alignment=Qt.AlignCenter)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.user_email = user_email  # 사용자 이메일을 저장할 변수 추가

        print(f"로그인된 사용자 ID: {self.user_email}")
        
        # Tab 1
        self.tab_1 = QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tab_1.setStyleSheet("QWidget { background-color: #feffe0; }") 
        tab_1_layout = QVBoxLayout(self.tab_1)
        tab_1_layout.setContentsMargins(20, 20, 20, 20)


        self.p2lab = QLabel(self.tab_1)
        self.p2lab.setObjectName("p2lab")
        self.p2lab.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 12pt; font-weight: bold;")

        tab_1_layout.addWidget(self.p2lab)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #self.p2spacer = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum) #40,20
        #self.horizontalLayout_2.addItem(self.p2spacer)

        self.itemname = QLabel()
        self.itemname.setObjectName("itemname")
        self.horizontalLayout_2.addWidget(self.itemname)

        self.name_insert = QLineEdit()
        self.name_insert.setObjectName("name_insert")
        self.name_insert.setStyleSheet("background-color: #ffffff; border: 1px solid #D3D3D3; border-radius: 4px; padding: 2px;")
        self.horizontalLayout_2.addWidget(self.name_insert)
        
        self.itemnum = QLabel()
        self.itemnum.setObjectName("itemnum")
        self.horizontalLayout_2.addWidget(self.itemnum)
        self.num_insert = QLineEdit()
        self.num_insert.setObjectName("num_insert")
        self.num_insert.setStyleSheet("background-color: #ffffff; border: 1px solid #D3D3D3; border-radius: 4px; padding: 2px;")
        self.num_insert.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.horizontalLayout_2.addWidget(self.num_insert)

        self.add_btn = QPushButton()
        self.add_btn.setObjectName("add_btn")
        self.add_btn.setIcon(QIcon('free_icon_add.png'))
        self.add_btn.setFixedSize(40, 40)
        self.add_btn.setIconSize(QSize(30, 30))
        self.add_btn.setStyleSheet("background-color: #feffe0; border: none;") 

        self.horizontalLayout_2.addWidget(self.add_btn)

        tab_1_layout.addLayout(self.horizontalLayout_2)
        self.add_btn.clicked.connect(self.order_item)

        scroll_area = QScrollArea(self.tab_1)
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("border: none;")

        scroll_content = QWidget()
        scroll_content.setStyleSheet("background-color: transparent;")
        self.gridLayout = QGridLayout(scroll_content)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(10)

        # 메뉴 1: 스테이크 & 치즈
        layout_1 = QVBoxLayout()
        layout_1.setSpacing(5)
        self.steak = QLabel()
        pixmap = QPixmap('steak_and_cheese.png')
        self.steak.setPixmap(pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.steak_name = QLabel("스테이크 & 치즈")
        self.steak_name.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.steak_name.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 10pt; font-weight: bold;")
        layout_1.addWidget(self.steak, alignment=Qt.AlignCenter)
        layout_1.addWidget(self.steak_name, alignment=Qt.AlignCenter)
        self.gridLayout.addLayout(layout_1, 0, 0)

        # 메뉴 2: 치킨데리야끼
        layout_2 = QVBoxLayout()
        layout_2.setSpacing(5)
        self.chickentery = QLabel()
        pixmap = QPixmap('chicken_teriyaki.png')
        self.chickentery.setPixmap(pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.chickentery_name = QLabel("치킨 데리야끼")
        self.chickentery_name.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.chickentery_name.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 10pt; font-weight: bold;")
        layout_2.addWidget(self.chickentery, alignment=Qt.AlignCenter)
        layout_2.addWidget(self.chickentery_name, alignment=Qt.AlignCenter)
        self.gridLayout.addLayout(layout_2, 1, 0)

        # 메뉴 3: 피자섭
        layout_3 = QVBoxLayout()
        layout_3.setSpacing(5)
        self.pizzasub = QLabel()
        pixmap = QPixmap('pizzasub.png')
        self.pizzasub.setPixmap(pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.pizzasub_name = QLabel("피자썹")
        self.pizzasub_name.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.pizzasub_name.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 10pt; font-weight: bold;")
        layout_3.addWidget(self.pizzasub, alignment=Qt.AlignCenter)
        layout_3.addWidget(self.pizzasub_name, alignment=Qt.AlignCenter)
        self.gridLayout.addLayout(layout_3, 2, 0)

        # 메뉴 4: 써브웨이 클럽
        layout_4 = QVBoxLayout()
        layout_4.setSpacing(5)
        self.subway_club = QLabel()
        pixmap = QPixmap('subway_club.png')
        self.subway_club.setPixmap(pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.subway_club_name = QLabel("써브웨이 클럽")
        self.subway_club_name.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.subway_club_name.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 10pt; font-weight: bold;")
        layout_4.addWidget(self.subway_club, alignment=Qt.AlignCenter)
        layout_4.addWidget(self.subway_club_name, alignment=Qt.AlignCenter)
        self.gridLayout.addLayout(layout_4, 0, 1)


        # 메뉴 5. 로티세리비비큐
        layout_5 = QVBoxLayout()
        layout_5.setSpacing(5)
        self.rotisseri_bbq = QLabel()
        pixmap = QPixmap('rotisseri_bbq.png')
        self.rotisseri_bbq.setPixmap(pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.rotisseri_bbq_name = QLabel("로티세리 바비큐")
        self.rotisseri_bbq_name.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.rotisseri_bbq_name.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 10pt; font-weight: bold;")
        layout_5.addWidget(self.rotisseri_bbq, alignment=Qt.AlignCenter)
        layout_5.addWidget(self.rotisseri_bbq_name, alignment=Qt.AlignCenter)
        self.gridLayout.addLayout(layout_5, 1, 1)
        

        layout_6 = QVBoxLayout()
        layout_6.setSpacing(5)
        self.roasted_chicken = QLabel()
        pixmap = QPixmap('roasted_chicken.png')
        self.roasted_chicken.setPixmap(pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.roasted_chicken_name = QLabel("로스티드 치킨")
        self.roasted_chicken_name.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.roasted_chicken_name.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 10pt; font-weight: bold;")
        layout_6.addWidget(self.roasted_chicken, alignment=Qt.AlignCenter)
        layout_6.addWidget(self.roasted_chicken_name, alignment=Qt.AlignCenter)
        self.gridLayout.addLayout(layout_6, 2, 1)


        layout_7 = QVBoxLayout()
        layout_7.setSpacing(5)
        self.shrimp = QLabel()
        pixmap = QPixmap('shrimp.png')
        self.shrimp.setPixmap(pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.shrimp_name = QLabel("쉬림프")
        self.shrimp_name.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.shrimp_name.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 10pt; font-weight: bold;")
        layout_7.addWidget(self.shrimp, alignment=Qt.AlignCenter)
        layout_7.addWidget(self.shrimp_name, alignment=Qt.AlignCenter)
        self.gridLayout.addLayout(layout_7, 3, 0)

        

        scroll_area.setWidget(scroll_content)
        tab_1_layout.addWidget(scroll_area)
        self.tabWidget.addTab(self.tab_1, "")

        self.verticalLayout.addWidget(self.tabWidget)
        #self.stackedWidget.raise_()
        #self.itemTable.raise_()

        # Tab 2
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_2.setStyleSheet("QWidget { background-color: #feffe0; }") 

        self.p3lab_2 = QLabel(self.tab_2)
        self.p3lab_2.setObjectName("p3lab_2")
        self.p3lab_2.setGeometry(QRect(20, 20, 280, 43))
        self.p3lab_2.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 12pt; font-weight: bold;")
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget.setStyleSheet("""
                    QTabWidget::pane {
                        border: 1px solid #D3D3D3; /* 본문 테두리선 */
                        background-color: #feffe0; /* 본문 배경색 (원하는 색상으로 변경) */
                    }
                    
                    QTabBar{
                        background-color: #feffe0; /* 본문 배경색 (원하는 색상으로 변경) */
                    }
                    
                    QTabBar::tab {
                        background-color: #f7f5bc;   /* 기본 탭 배경 */
                        font-family: "Malgun Gothic";
                        color: #333333;              /* 기본 글자 색상 */
                        font-size: 13pt;             /* 글자 크기 */
                        padding: 10px 10px;          /* 탭 여백 */
                        min-height: 80px;
                        min-width: 30px;
                        border-top-left-radius: 6px;
                        border-top-right-radius: 6px;
                    }
                    QTabBar::tab:selected {
                        background-color: #02ad07;   /* 선택된 탭 배경 (초록) */
                        color: white;                /* 선택된 탭 글자 (흰색) */
                        font-weight: bold;
                    }
                    QTabBar::tab:hover:!selected {
                        background-color: #B0BEC5;   /* 선택 안된 탭 마우스 호버 */
                    }
                """)
        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        #self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

        #self.load_items()
        #self.load_customers()
        #self.load_orders()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))

        '''self.selectWork.setText(QCoreApplication.translate("MainWindow", "수행할 작업을 선택하세요", None))
        self.add_new.setText(QCoreApplication.translate("MainWindow", "", None))
        self.delete_cur.setText(QCoreApplication.translate("MainWindow", "", None))'''
        self.p2lab.setText(QCoreApplication.translate("MainWindow", "주문할 상품 정보를 입력하세요", None))
        self.itemname.setText(QCoreApplication.translate("MainWindow", "상품명", None))
        #self.itemprice.setText(QCoreApplication.translate("MainWindow", "가격", None))
        self.itemnum.setText(QCoreApplication.translate("MainWindow", "수량", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", "", None))
        '''self.p3lab.setText(QCoreApplication.translate("MainWindow", "삭제할 상품 정보를 입력하세요", None))
        self.itemname_d.setText(QCoreApplication.translate("MainWindow", "상품명", None))
        self.num_d.setText(QCoreApplication.translate("MainWindow", "수량", None))
        self.del_btn.setText(QCoreApplication.translate("MainWindow", "삭제", None))'''
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", "메뉴", None))
        self.steak_name.setText(QCoreApplication.translate("MainWindow", "스테이크 앤 치즈", None))
        self.chickentery_name.setText(QCoreApplication.translate("MainWindow", "치킨 데리야끼", None))
        self.pizzasub_name.setText(QCoreApplication.translate("MainWindow", "피자썹", None))
        self.subway_club_name.setText(QCoreApplication.translate("MainWindow", "써브웨이 클럽", None))

        self.p3lab_2.setText(QCoreApplication.translate("MainWindow", "총 주문 현황", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", "Mypage", None))
        

    def load_orders(self):
        rows = self.db.fetch_order()
        self.orderTable.setRowCount(len(rows))
        for r, (clientname, itemname, num, orderdate) in enumerate(rows):
            self.orderTable.setItem(r, 0, QTableWidgetItem(clientname))
            self.orderTable.setItem(r, 1, QTableWidgetItem(itemname))
            self.orderTable.setItem(r, 2, QTableWidgetItem(str(num)))
            self.orderTable.setItem(r, 3, QTableWidgetItem(str(orderdate)))
        self.orderTable.resizeColumnsToContents()

    def load_items(self):
        rows = self.db.fetch_item()
        self.itemTable.setRowCount(len(rows))
        for r, (id,name, price, stock) in enumerate(rows):
            self.itemTable.setItem(r, 0, QTableWidgetItem(name))
            self.itemTable.setItem(r, 1, QTableWidgetItem(str(price)))
            self.itemTable.setItem(r, 2, QTableWidgetItem(str(stock)))
        self.itemTable.resizeColumnsToContents()

    def load_customers(self):
        rows = self.db.fetch_account()
        self.customTable.setRowCount(len(rows))
        for r, (userID, name, email, addr) in enumerate(rows):
            self.customTable.setItem(r, 0, QTableWidgetItem(str(userID)))
            self.customTable.setItem(r, 1, QTableWidgetItem(name))
            self.customTable.setItem(r, 2, QTableWidgetItem(email))
            self.customTable.setItem(r, 3, QTableWidgetItem(addr))
        self.customTable.resizeColumnsToContents()

    def order_item(self): # order_item(self,client,item,num,orderdate)
        name = self.name_insert.text().strip()
        stock = self.num_insert.text().strip()

        # email
        if not name or not stock:
            QMessageBox.warning(None, "오류", "주문할 상품 이름과 수량을 모두 입력하세요.")
            return
        ok = self.db.order_item(self.user_email, name, stock)
        if ok:
            QMessageBox.information(None, "완료", "주문되었습니다.")
            self.name_insert.clear()
            self.num_insert.clear()
            #self.load_orders()
            #self.stackedWidget.setCurrentIndex(0)
        else:
            QMessageBox.critical(None, "실패", "주문 중 오류가 발생했습니다.")

    def del_item(self):
        delname = self.name_d_insert.text().strip()
        delnum = self.num_d_insert.text().strip()
        if not delname or not delnum:
            QMessageBox.warning(None, "오류", "삭제할 상품 이름과 수량을 모두 입력하세요.")
            return
        ok = self.db.del_item(delname, delnum)
        if ok:
            QMessageBox.information(None, "완료", "삭제되었습니다.")
            self.name_d_insert.clear()
            self.num_d_insert.clear()
            self.load_items()
            #self.stackedWidget.setCurrentIndex(0)
        else:
            QMessageBox.critical(None, "실패", "삭제 중 오류가 발생했습니다.")

    #def btn_func1(self):
        #self.stackedWidget.setCurrentIndex(1)

    #def btn_func2(self):
        #self.stackedWidget.setCurrentIndex(2)