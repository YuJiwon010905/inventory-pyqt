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
        MainWindow.resize(400, 600) # desktop (400,600)
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


        '''self.p2lab = QLabel(self.tab_1)
        self.p2lab.setObjectName("p2lab")
        self.p2lab.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 12pt; font-weight: bold;")

        tab_1_layout.addWidget(self.p2lab)'''

        '''self.horizontalLayout_2 = QHBoxLayout()
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

        self.horizontalLayout_2.addWidget(self.add_btn)'''

        '''tab_1_layout.addLayout(self.horizontalLayout_2)
        self.add_btn.clicked.connect(self.order_item)'''

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
        self.steak_name = "스테이크 앤 치즈"
        self.steak_label=QLabel(self.steak_name)

        self.steak_plus_button=QPushButton()
        self.steak_plus_button.setIcon(QIcon('plus.png'))
        self.steak_plus_button.setFixedSize(30, 30)
        self.steak_plus_button.setIconSize(QSize(20, 20))
        self.steak_plus_button.setStyleSheet("background-color: #feffe0; border: none;")
        self.steak_plus_button.clicked.connect(lambda: self.order_item(self.steak_name))  # 메뉴 이름을 전달

        '''self.steak_minus_button=QPushButton()
        self.steak_minus_button.setIcon(QIcon('delete.png'))
        self.steak_minus_button.setFixedSize(30, 30)
        self.steak_minus_button.setIconSize(QSize(22, 22))
        self.steak_minus_button.setStyleSheet("background-color: #feffe0; border: none;") 
        self.steak_minus_button.clicked.connect(lambda: self.order_item(self.steak_name))  # 메뉴 이름을 전달'''


        h1 = QHBoxLayout()
        h1.addWidget(self.steak_plus_button)
        #h1.addWidget(self.steak_minus_button)

        self.steak_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.steak_label.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 10pt; font-weight: bold;")
        layout_1.addWidget(self.steak, alignment=Qt.AlignCenter)
        layout_1.addWidget(self.steak_label, alignment=Qt.AlignCenter)

        layout_1.addLayout(h1)
        
        self.gridLayout.addLayout(layout_1, 0, 0)

        # 메뉴 2: 치킨데리야끼
        layout_2 = QVBoxLayout()
        layout_2.setSpacing(5)
        self.chickentery = QLabel()
        pixmap = QPixmap('chicken_teriyaki.png')
        self.chickentery.setPixmap(pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.chickentery_name = "치킨 데리야끼"
        self.chickentery_label=QLabel(self.chickentery_name)

        self.chickentery_plus_button=QPushButton()
        self.chickentery_plus_button.setIcon(QIcon('plus.png'))
        self.chickentery_plus_button.setFixedSize(30, 30)
        self.chickentery_plus_button.setIconSize(QSize(20, 20))
        self.chickentery_plus_button.setStyleSheet("background-color: #feffe0; border: none;")
        self.chickentery_plus_button.clicked.connect(lambda: self.order_item(self.chickentery_name))  # 메뉴 이름을 전달

        '''self.chickentery_minus_button=QPushButton()
        self.chickentery_minus_button.setIcon(QIcon('delete.png'))
        self.chickentery_minus_button.setFixedSize(30, 30)
        self.chickentery_minus_button.setIconSize(QSize(22, 22))
        self.chickentery_minus_button.setStyleSheet("background-color: #feffe0; border: none;") 
        self.chickentery_minus_button.clicked.connect(lambda: self.order_item(self.chickentery_name))  # 메뉴 이름을 전달'''

        h2 = QHBoxLayout()
        h2.addWidget(self.chickentery_plus_button)
        #h2.addWidget(self.chickentery_minus_button)

        self.chickentery_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.chickentery_label.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 10pt; font-weight: bold;")
        layout_2.addWidget(self.chickentery, alignment=Qt.AlignCenter)
        layout_2.addWidget(self.chickentery_label, alignment=Qt.AlignCenter)

        layout_2.addLayout(h2)

        self.gridLayout.addLayout(layout_2, 1, 0)

        # 메뉴 3: 피자섭
        layout_3 = QVBoxLayout()
        layout_3.setSpacing(5)
        self.pizzasub = QLabel()
        pixmap = QPixmap('pizzasub.png')
        self.pizzasub.setPixmap(pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.pizzasub_name = "피자썹"
        self.pizzasub_label=QLabel(self.pizzasub_name)

        self.pizzasub_plus_button=QPushButton()
        self.pizzasub_plus_button.setIcon(QIcon('plus.png'))
        self.pizzasub_plus_button.setFixedSize(30, 30)
        self.pizzasub_plus_button.setIconSize(QSize(20, 20))
        self.pizzasub_plus_button.setStyleSheet("background-color: #feffe0; border: none;")
        self.pizzasub_plus_button.clicked.connect(lambda: self.order_item(self.pizzasub_name))  # 메뉴 이름을 전달

        '''self.pizzasub_minus_button=QPushButton()
        self.pizzasub_minus_button.setIcon(QIcon('delete.png'))
        self.pizzasub_minus_button.setFixedSize(30, 30)
        self.pizzasub_minus_button.setIconSize(QSize(22, 22))
        self.pizzasub_minus_button.setStyleSheet("background-color: #feffe0; border: none;") 
        self.pizzasub_minus_button.clicked.connect(lambda: self.order_item(self.pizzasub_name))  # 메뉴 이름을 전달'''

        h3 = QHBoxLayout()
        h3.addWidget(self.pizzasub_plus_button)
        # h3.addWidget(self.pizzasub_minus_button)


        self.pizzasub_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.pizzasub_label.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 10pt; font-weight: bold;")
        layout_3.addWidget(self.pizzasub, alignment=Qt.AlignCenter)
        layout_3.addWidget(self.pizzasub_label, alignment=Qt.AlignCenter)

        layout_3.addLayout(h3)

        self.gridLayout.addLayout(layout_3, 2, 0)

        # 메뉴 4: 써브웨이 클럽
        layout_4 = QVBoxLayout()
        layout_4.setSpacing(5)
        self.subway_club = QLabel()
        pixmap = QPixmap('subway_club.png')
        self.subway_club.setPixmap(pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.subway_club_name = "써브웨이 클럽"
        self.subway_club_label=QLabel(self.subway_club_name)

        self.subway_club_plus_button=QPushButton()
        self.subway_club_plus_button.setIcon(QIcon('plus.png'))
        self.subway_club_plus_button.setFixedSize(30, 30)
        self.subway_club_plus_button.setIconSize(QSize(20, 20))
        self.subway_club_plus_button.setStyleSheet("background-color: #feffe0; border: none;")
        self.subway_club_plus_button.clicked.connect(lambda: self.order_item(self.subway_club_name))  # 메뉴 이름을 전달

        '''self.subway_club_minus_button=QPushButton()
        self.subway_club_minus_button.setIcon(QIcon('delete.png'))
        self.subway_club_minus_button.setFixedSize(30, 30)
        self.subway_club_minus_button.setIconSize(QSize(22, 22))
        self.subway_club_minus_button.setStyleSheet("background-color: #feffe0; border: none;") 
        self.subway_club_minus_button.clicked.connect(lambda: self.order_item(self.subway_club_name))  # 메뉴 이름을 전달'''

        h4 = QHBoxLayout()
        h4.addWidget(self.subway_club_plus_button)
        #h4.addWidget(self.subway_club_minus_button)

        self.subway_club_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.subway_club_label.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 10pt; font-weight: bold;")
        layout_4.addWidget(self.subway_club, alignment=Qt.AlignCenter)
        layout_4.addWidget(self.subway_club_label, alignment=Qt.AlignCenter)

        layout_4.addLayout(h4)
        self.gridLayout.addLayout(layout_4, 0, 1)


        # 메뉴 5. 로티세리비비큐
        layout_5 = QVBoxLayout()
        layout_5.setSpacing(5)
        self.rotisseri_bbq = QLabel()
        pixmap = QPixmap('rotisseri_bbq.png')
        self.rotisseri_bbq.setPixmap(pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.rotisseri_bbq_name = "로티세리 바비큐 치킨"
        self.rotisseri_bbq_label = QLabel(self.rotisseri_bbq_name)

        self.rotisseri_bbq_plus_button=QPushButton()
        self.rotisseri_bbq_plus_button.setIcon(QIcon('plus.png'))
        self.rotisseri_bbq_plus_button.setFixedSize(30, 30)
        self.rotisseri_bbq_plus_button.setIconSize(QSize(20, 20))
        self.rotisseri_bbq_plus_button.setStyleSheet("background-color: #feffe0; border: none;")
        self.rotisseri_bbq_plus_button.clicked.connect(lambda: self.order_item(self.rotisseri_bbq_name))  # 메뉴 이름을 전달

        '''self.rotisseri_bbq_minus_button=QPushButton()
        self.rotisseri_bbq_minus_button.setIcon(QIcon('delete.png'))
        self.rotisseri_bbq_minus_button.setFixedSize(30, 30)
        self.rotisseri_bbq_minus_button.setIconSize(QSize(22, 22))
        self.rotisseri_bbq_minus_button.setStyleSheet("background-color: #feffe0; border: none;") 
        self.rotisseri_bbq_minus_button.clicked.connect(lambda: self.order_item(self.rotisseri_bbq_name))  # 메뉴 이름을 전달'''

        h5 = QHBoxLayout()
        h5.addWidget(self.rotisseri_bbq_plus_button)
        #h5.addWidget(self.rotisseri_bbq_minus_button)

        self.rotisseri_bbq_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.rotisseri_bbq_label.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 10pt; font-weight: bold;")
        layout_5.addWidget(self.rotisseri_bbq, alignment=Qt.AlignCenter)
        layout_5.addWidget(self.rotisseri_bbq_label, alignment=Qt.AlignCenter)
        layout_5.addLayout(h5)
        self.gridLayout.addLayout(layout_5, 1, 1)
        

        layout_6 = QVBoxLayout()
        layout_6.setSpacing(5)
        self.roasted_chicken = QLabel()
        pixmap = QPixmap('roasted_chicken.png')
        self.roasted_chicken.setPixmap(pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.roasted_chicken_name = "로스티드 치킨"
        self.roasted_chicken_label = QLabel(self.roasted_chicken_name)

        self.roasted_chicken_plus_button=QPushButton()
        self.roasted_chicken_plus_button.setIcon(QIcon('plus.png'))
        self.roasted_chicken_plus_button.setFixedSize(30, 30)
        self.roasted_chicken_plus_button.setIconSize(QSize(20, 20))
        self.roasted_chicken_plus_button.setStyleSheet("background-color: #feffe0; border: none;")
        self.roasted_chicken_plus_button.clicked.connect(lambda: self.order_item(self.roasted_chicken_name))  # 메뉴 이름을 전달

        '''self.roasted_chicken_minus_button=QPushButton()
        self.roasted_chicken_minus_button.setIcon(QIcon('delete.png'))
        self.roasted_chicken_minus_button.setFixedSize(30, 30)
        self.roasted_chicken_minus_button.setIconSize(QSize(22, 22))
        self.roasted_chicken_minus_button.setStyleSheet("background-color: #feffe0; border: none;") 
        self.roasted_chicken_minus_button.clicked.connect(lambda: self.order_item(self.roasted_chicken_name))  # 메뉴 이름을 전달'''

        h6 = QHBoxLayout()
        h6.addWidget(self.roasted_chicken_plus_button)
        #h6.addWidget(self.roasted_chicken_minus_button)

        self.roasted_chicken_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.roasted_chicken_label.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 10pt; font-weight: bold;")
        layout_6.addWidget(self.roasted_chicken, alignment=Qt.AlignCenter)
        layout_6.addWidget(self.roasted_chicken_label, alignment=Qt.AlignCenter)
        layout_6.addLayout(h6)
        self.gridLayout.addLayout(layout_6, 2, 1)


        layout_7 = QVBoxLayout()
        layout_7.setSpacing(5)
        self.shrimp = QLabel()
        pixmap = QPixmap('shrimp.png')

        self.shrimp_plus_button=QPushButton()
        self.shrimp_plus_button.setIcon(QIcon('plus.png'))
        self.shrimp_plus_button.setFixedSize(30, 30)
        self.shrimp_plus_button.setIconSize(QSize(20, 20))
        self.shrimp_plus_button.setStyleSheet("background-color: #feffe0; border: none;")
        self.shrimp_plus_button.clicked.connect(lambda: self.order_item(self.shrimp_name))  # 메뉴 이름을 전달

        '''self.shrimp_minus_button=QPushButton()
        self.shrimp_minus_button.setIcon(QIcon('delete.png'))
        self.shrimp_minus_button.setFixedSize(30, 30)
        self.shrimp_minus_button.setIconSize(QSize(22, 22))
        self.shrimp_minus_button.setStyleSheet("background-color: #feffe0; border: none;") 
        self.shrimp_minus_button.clicked.connect(lambda: self.order_item(self.shrimp_name))  # 메뉴 이름을 전달'''

        h7 = QHBoxLayout()
        h7.addWidget(self.shrimp_plus_button)
        #h7.addWidget(self.shrimp_minus_button)

        self.shrimp.setPixmap(pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.shrimp_name = "쉬림프"
        self.shrimp_label = QLabel(self.shrimp_name)
        self.shrimp_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.shrimp_label.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 10pt; font-weight: bold;")
        layout_7.addWidget(self.shrimp, alignment=Qt.AlignCenter)
        layout_7.addWidget(self.shrimp_label, alignment=Qt.AlignCenter)

        layout_7.addLayout(h7)
        self.gridLayout.addLayout(layout_7, 3, 0)


        scroll_area.setWidget(scroll_content)
        tab_1_layout.addWidget(scroll_area)
        self.tabWidget.addTab(self.tab_1, "")

        self.verticalLayout.addWidget(self.tabWidget)

        # Tab 2
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_2.setStyleSheet("QWidget { background-color: #feffe0; }")

        tab_2_layout = QVBoxLayout(self.tab_2)
        tab_2_layout.setContentsMargins(20, 20, 20, 20)
        tab_2_layout.setAlignment(Qt.AlignTop)

        self.p3lab_2 = QLabel("회원 정보")
        self.p3lab_2.setObjectName("p3lab_2")
        #self.p3lab_2.setGeometry(QRect(20, 20, 280, 43))
        self.p3lab_2.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 11pt; font-weight: bold;")

        name,email,pw,addr=self.db.print_account(user_email)
        self.print_name=QLabel("이름: "+ str(name))
        self.print_email=QLabel("이메일: "+str(email))
        self.print_pw=QLabel("비밀번호: "+str(pw))
        self.print_addr=QLabel("주소: "+str(addr))

        self.print_name.setStyleSheet("font-family: 'Malgun Gothic';")
        self.print_email.setStyleSheet("font-family: 'Malgun Gothic';")
        self.print_pw.setStyleSheet("font-family: 'Malgun Gothic';")
        self.print_addr.setStyleSheet("font-family: 'Malgun Gothic';")


        self.p3lab_2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.print_name.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.print_email.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.print_pw.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.print_addr.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        tab_2_layout.addWidget(self.p3lab_2,alignment=Qt.AlignCenter)
        tab_2_layout.addWidget(self.print_name)
        tab_2_layout.addWidget(self.print_email)
        tab_2_layout.addWidget(self.print_pw)
        tab_2_layout.addWidget(self.print_addr)

        # 주문내역 테이블도 추가

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
                        min-height: 160px;
                        min-width: 50px;
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

        '''self.p2lab.setText(QCoreApplication.translate("MainWindow", "주문할 상품 정보를 입력하세요", None))
        self.itemname.setText(QCoreApplication.translate("MainWindow", "상품명", None))

        self.itemnum.setText(QCoreApplication.translate("MainWindow", "수량", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", "", None))'''

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", "메뉴", None))
        #self.steak_name.setText(QCoreApplication.translate("MainWindow", "스테이크 앤 치즈", None))
        #self.chickentery_name.setText(QCoreApplication.translate("MainWindow", "치킨 데리야끼", None))
        #self.pizzasub_name.setText(QCoreApplication.translate("MainWindow", "피자썹", None))
        #self.subway_club_name.setText(QCoreApplication.translate("MainWindow", "써브웨이 클럽", None))

        #self.p3lab_2.setText(QCoreApplication.translate("MainWindow", "회원 정보", None))
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

    def order_item(self,name): # order_item(self,client,item,num,orderdate)

        # 수정 예정
        name = name.strip()
        #stock = self.num_insert.text().strip()

        # email
        if not name:
            QMessageBox.warning(None, "오류", "주문할 상품 이름과 수량을 모두 입력하세요.")
            return
        
        print(name)
        ok = self.db.order_item(self.user_email, name, 1) # 1개 추가됨
        if ok:
            QMessageBox.information(None, "완료", "주문되었습니다.")
            #self.name_insert.clear()
            #self.num_insert.clear()
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