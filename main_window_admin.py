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
    QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, 
    QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QPushButton, 
    QMessageBox, QStackedWidget, QSizePolicy, QSpacerItem, QLayout,
    QMenuBar, QStatusBar,QHeaderView
)
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtGui import QIcon, QPixmap
from db_helper import DB, DB_CONFIG


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        self.db=DB(**DB_CONFIG)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #ffffff;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.West)
        # Tab 1
        self.tab_1 = QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tab_1.setStyleSheet("QWidget { background-color: #feffe0; }")

        tab_1_layout = QVBoxLayout(self.tab_1)
        tab_1_layout.setContentsMargins(20, 20, 20, 20)

        self.logo_label=QLabel()
        pixmap=QPixmap('subway.png')
        scaled_pixmap = pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_label.setPixmap(scaled_pixmap)
        self.verticalLayout.addWidget(self.logo_label, alignment=Qt.AlignCenter)

        self.itemTable = QTableWidget(self.tab_1)
        if self.itemTable.columnCount() < 3:
            self.itemTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.itemTable.setObjectName("itemTable")
        self.itemTable.setGeometry(QRect(20, 100, 290, 371)) #20,100
        #self.itemTable.setContentsMargins(10, 10, 10, 10)
        self.itemTable.setEditTriggers(self.itemTable.NoEditTriggers)
        self.itemTable.verticalHeader().setVisible(False)
        #self.itemTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.itemTable.setStyleSheet("QTableWidget { background-color: #ffffff; border: 1px solid #D3D3D3; }"
                                     "QHeaderView::section { background-color: #f7f5bc; font-family: 'Malgun Gothic'; font-size: 10pt; border:none; font-weight: bold; }"
                                     "QTableWidget::item { padding: 5px; }")
        self.itemTable.resizeColumnsToContents()
        
        self.stackedWidget = QStackedWidget(self.tab_1)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        #self.stackedWidget.setGeometry(QRect(10, 10, 300, 80)) #10,10

        # Page 1
        self.page_1 = QWidget()
        self.page_1.setObjectName("page_1")
        self.p1layout = QVBoxLayout(self.page_1)
        self.p1layout.setObjectName("p1layout")
        self.selectWork = QLabel(self.page_1)
        self.selectWork.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 12pt; font-weight: bold;")
        self.selectWork.setObjectName("selectWork")
        self.selectWork.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.p1layout.addWidget(self.selectWork,alignment=Qt.AlignCenter)

        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.horizontalLayout_1.setSizeConstraint(QLayout.SetDefaultConstraint)
        #self.p1spacer = QSpacerItem(40, 120, QSizePolicy.Expanding, QSizePolicy.Minimum) #40,20

        #self.horizontalLayout_1.addItem(self.p1spacer)

        self.add_new = QPushButton(self.page_1)
        self.add_new.setObjectName("add_new")
        self.add_new.setIcon(QIcon('free_icon_add.png'))
        self.add_new.setFixedSize(40, 40)
        self.add_new.setIconSize(QSize(25, 25))
        self.add_new.setStyleSheet("background-color: #feffe0; border: none;") 

        self.horizontalLayout_1.addWidget(self.add_new)

        self.delete_cur = QPushButton(self.page_1)
        self.delete_cur.setObjectName("delete_cur")
        self.delete_cur.setIcon(QIcon('free_icon_delete.png'))
        self.delete_cur.setFixedSize(40, 40)
        self.delete_cur.setIconSize(QSize(25, 25))
        self.delete_cur.setStyleSheet("background-color: #feffe0; border: none;")
        self.horizontalLayout_1.addWidget(self.delete_cur)

        self.add_new.clicked.connect(self.btn_func1)
        self.delete_cur.clicked.connect(self.btn_func2)

        self.p1layout.addLayout(self.horizontalLayout_1)
        self.stackedWidget.addWidget(self.page_1)
        

        # Page 2
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.p2layout = QVBoxLayout(self.page_2)
        self.p2layout.setObjectName("p2layout")
        self.p2lab = QLabel(self.page_2)
        self.p2lab.setObjectName("p2lab")
        self.p2lab.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 12pt; font-weight: bold;")

        self.p2layout.addWidget(self.p2lab,alignment=Qt.AlignCenter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #self.p2spacer = QSpacerItem(40, 120, QSizePolicy.Expanding, QSizePolicy.Minimum) #40,20

        #self.horizontalLayout_2.addItem(self.p2spacer)

        self.itemname = QLabel(self.page_2)
        self.itemname.setObjectName("itemname")
        self.horizontalLayout_2.addWidget(self.itemname)

        self.name_insert = QLineEdit(self.page_2)
        self.name_insert.setObjectName("name_insert")
        self.name_insert.setStyleSheet("background-color: #ffffff; border: 1px solid #D3D3D3; border-radius: 4px; padding: 2px;")
        self.horizontalLayout_2.addWidget(self.name_insert)

        self.itemprice = QLabel(self.page_2)
        self.itemprice.setObjectName("itemprice")
        self.horizontalLayout_2.addWidget(self.itemprice)

        self.price_insert = QLineEdit(self.page_2)
        self.price_insert.setObjectName("price_insert")
        self.price_insert.setStyleSheet("background-color: #ffffff; border: 1px solid #D3D3D3; border-radius: 4px; padding: 2px;")
        self.horizontalLayout_2.addWidget(self.price_insert)

        self.itemnum = QLabel(self.page_2)
        self.itemnum.setObjectName("itemnum")
        self.horizontalLayout_2.addWidget(self.itemnum)

        self.num_insert = QLineEdit(self.page_2)
        self.num_insert.setObjectName("num_insert")
        self.num_insert.setStyleSheet("background-color: #ffffff; border: 1px solid #D3D3D3; border-radius: 4px; padding: 2px;")
        self.horizontalLayout_2.addWidget(self.num_insert)

        self.add_btn = QPushButton(self.page_2)
        self.add_btn.setObjectName("add_btn")
        self.add_btn.setIcon(QIcon('free_icon_add.png'))
        self.add_btn.setFixedSize(30, 30)
        self.add_btn.setIconSize(QSize(20, 20))
        self.add_btn.setStyleSheet("background-color: #feffe0; border: none;")

        self.horizontalLayout_2.addWidget(self.add_btn)

        self.p2layout.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.page_2)
        self.add_btn.clicked.connect(self.add_item)

        # Page 3
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.p3layout = QVBoxLayout(self.page_3)
        self.p3layout.setObjectName("p3layout")
        self.p3lab = QLabel(self.page_3)
        self.p3lab.setObjectName("p3lab")
        self.p3lab.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 12pt; font-weight: bold;")
        self.p3layout.addWidget(self.p3lab,alignment=Qt.AlignCenter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        #self.p3spacer = QSpacerItem(40, 120, QSizePolicy.Expanding, QSizePolicy.Minimum) #40,20

        #self.horizontalLayout_3.addItem(self.p3spacer)

        self.itemname_d = QLabel(self.page_3)
        self.itemname_d.setObjectName("itemname_d")
        self.horizontalLayout_3.addWidget(self.itemname_d)

        self.name_d_insert = QLineEdit(self.page_3)
        self.name_d_insert.setObjectName("name_d_insert")
        self.name_d_insert.setStyleSheet("background-color: #ffffff; border: 1px solid #D3D3D3; border-radius: 4px; padding: 2px;")
        self.horizontalLayout_3.addWidget(self.name_d_insert)

        self.num_d = QLabel(self.page_3)
        self.num_d.setObjectName("num_d")
        self.horizontalLayout_3.addWidget(self.num_d)

        self.num_d_insert = QLineEdit(self.page_3)
        self.num_d_insert.setObjectName("num_d_insert")
        self.num_d_insert.setStyleSheet("background-color: #ffffff; border: 1px solid #D3D3D3; border-radius: 4px; padding: 2px;")
        self.horizontalLayout_3.addWidget(self.num_d_insert)

        self.del_btn = QPushButton(self.page_3)
        self.del_btn.setObjectName("del_btn")
        self.del_btn.setIcon(QIcon('free_icon_delete.png'))
        self.del_btn.setFixedSize(30, 30)
        self.del_btn.setIconSize(QSize(20, 20))

        self.del_btn.setStyleSheet("background-color: #feffe0; border: none;")
        self.horizontalLayout_3.addWidget(self.del_btn)

        self.p3layout.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.page_3)
        self.del_btn.clicked.connect(self.del_item)

        tab_1_layout.addWidget(self.stackedWidget)
        tab_1_layout.addWidget(self.itemTable)
        tab_1_layout.setStretchFactor(self.stackedWidget, 0)
        tab_1_layout.setStretchFactor(self.itemTable, 1)
        self.tab_1.setLayout(tab_1_layout)

        self.tabWidget.addTab(self.tab_1, "")
        self.stackedWidget.raise_()
        self.itemTable.raise_()

        # Tab 2
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_2.setStyleSheet("QWidget { background-color: #feffe0; }")

        tab_2_layout = QVBoxLayout(self.tab_2)
        tab_2_layout.setContentsMargins(20, 20, 20, 20)
        self.orderTable = QTableWidget()
        if self.orderTable.columnCount() < 4:
            self.orderTable.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.orderTable.setObjectName("orderTable")
        self.orderTable.setGeometry(QRect(20, 100, 290, 192))
        self.orderTable.setColumnCount(4)
        self.orderTable.setEditTriggers(self.orderTable.NoEditTriggers)
        self.orderTable.verticalHeader().setVisible(False)
        self.orderTable.setStyleSheet("QTableWidget { background-color: #ffffff; border: 1px solid #D3D3D3; }"
                                             "QHeaderView::section { background-color: #f7f5bc; font-family: 'Malgun Gothic'; font-size: 10pt; border:none; font-weight: bold; }"
                                             "QTableWidget::item { padding: 5px; }")
        self.orderTable.resizeColumnsToContents()
        

        self.p3lab_2 = QLabel()
        self.p3lab_2.setObjectName("p3lab_2")
        #self.p3lab_2.setGeometry(QRect(20, 20, 290, 43))
        self.p3lab_2.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 12pt; font-weight: bold;")
        tab_2_layout.addWidget(self.p3lab_2, alignment=Qt.AlignCenter)
        tab_2_layout.addWidget(self.orderTable)

        self.tab_2.setLayout(tab_2_layout)
        self.tabWidget.addTab(self.tab_2, "")

        # Tab 3``
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tab_3.setStyleSheet("QWidget { background-color: #feffe0; }")
        tab_3_layout = QVBoxLayout(self.tab_3)
        tab_3_layout.setContentsMargins(20, 20, 20, 20)
        self.customTable = QTableWidget()
        if self.customTable.columnCount() < 4:
            self.customTable.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.customTable.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.customTable.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.customTable.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.customTable.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.customTable.setObjectName("customTable")
        self.customTable.setGeometry(QRect(20, 100, 290, 192))
        self.customTable.setEditTriggers(self.customTable.NoEditTriggers)
        self.customTable.verticalHeader().setVisible(False)
        self.customTable.setStyleSheet("QTableWidget { background-color: #ffffff; border: 1px solid #D3D3D3; }"
                                             "QHeaderView::section { background-color: #f7f5bc; font-family: 'Malgun Gothic'; font-size: 10pt; border:none; font-weight: bold; }"
                                             "QTableWidget::item { padding: 5px; }")
        self.customTable.resizeColumnsToContents()
        self.p3lab_3 = QLabel(self.tab_3)
        self.p3lab_3.setObjectName("p3lab_3")
        #self.p3lab_3.setGeometry(QRect(20, 20, 290, 43))
        self.p3lab_3.setStyleSheet("font-family: 'Malgun Gothic'; font-size: 12pt; font-weight: bold;")
        self.p3lab_3.setAlignment(Qt.AlignCenter)

        tab_3_layout.addWidget(self.p3lab_3, alignment=Qt.AlignCenter)
        tab_3_layout.addWidget(self.customTable)
        self.tab_3.setLayout(tab_3_layout)

        self.tabWidget.addTab(self.tab_3, "")
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
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

        self.load_items()
        self.load_customers()
        self.load_orders()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        ___qtablewidgetitem = self.itemTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", "상품명", None))
        ___qtablewidgetitem1 = self.itemTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", "가격", None))
        ___qtablewidgetitem2 = self.itemTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", "수량", None))
        self.selectWork.setText(QCoreApplication.translate("MainWindow", "수행할 작업을 선택하세요", None))
        self.add_new.setText(QCoreApplication.translate("MainWindow", "", None))
        self.delete_cur.setText(QCoreApplication.translate("MainWindow", "", None))
        self.p2lab.setText(QCoreApplication.translate("MainWindow", "추가할 상품 정보를 입력하세요", None))
        self.itemname.setText(QCoreApplication.translate("MainWindow", "상품명", None))
        self.itemprice.setText(QCoreApplication.translate("MainWindow", "가격", None))
        self.itemnum.setText(QCoreApplication.translate("MainWindow", "수량", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", "", None))
        self.p3lab.setText(QCoreApplication.translate("MainWindow", "삭제할 상품 정보를 입력하세요", None))
        self.itemname_d.setText(QCoreApplication.translate("MainWindow", "상품명", None))
        self.num_d.setText(QCoreApplication.translate("MainWindow", "수량", None))
        self.del_btn.setText(QCoreApplication.translate("MainWindow", "", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", "상품 관리", None))
        
        ___qtablewidgetitem3 = self.orderTable.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", "고객명", None))
        ___qtablewidgetitem4 = self.orderTable.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", "상품명", None))
        ___qtablewidgetitem5 = self.orderTable.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", "수량", None))
        ___qtablewidgetitem6 = self.orderTable.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", "주문일", None))
        self.p3lab_2.setText(QCoreApplication.translate("MainWindow", "총 주문 현황", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", "주문 현황", None))
        
        ___qtablewidgetitem7 = self.customTable.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", "ID", None))
        ___qtablewidgetitem8 = self.customTable.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", "고객명", None))
        ___qtablewidgetitem9 = self.customTable.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", "email", None))
        ___qtablewidgetitem10 = self.customTable.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", "주소", None))
        self.p3lab_3.setText(QCoreApplication.translate("MainWindow", "총 고객 명단", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", "고객 명단", None))

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

    def add_item(self):
        name = self.name_insert.text().strip()
        price = self.price_insert.text().strip()
        stock = self.num_insert.text().strip()
        if not name or not price or not stock:
            QMessageBox.warning(None, "오류", "상품 이름, 가격, 수량을 모두 입력하세요.")
            return
        ok = self.db.add_item(name, price, stock)
        if ok:
            QMessageBox.information(None, "완료", "추가(수정)되었습니다.")
            self.name_insert.clear()
            self.price_insert.clear()
            self.num_insert.clear()
            self.load_items()
            self.stackedWidget.setCurrentIndex(0)
        else:
            QMessageBox.critical(None, "실패", "추가(수정) 중 오류가 발생했습니다.")

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
            self.stackedWidget.setCurrentIndex(0)
        else:
            QMessageBox.critical(None, "실패", "삭제 중 오류가 발생했습니다.")

    def btn_func1(self):
        self.stackedWidget.setCurrentIndex(1)

    def btn_func2(self):
        self.stackedWidget.setCurrentIndex(2)