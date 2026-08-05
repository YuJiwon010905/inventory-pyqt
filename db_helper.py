import traceback

import pymysql
from datetime import datetime

DB_CONFIG=dict(host="localhost",user="root",password="0905",
               database="orderappdb",charset="utf8")
class DB:
    def __init__(self,**config):
        self.config=config

    def connect(self):
        return pymysql.connect(**self.config) # 데이터베이스를 연결해준다

############################# 관리자용 #######################################
    # 관리자 검증(admin 용)
    def verify_admin(self,adminname,pw):
        sql="SELECT COUNT(*) FROM admins WHERE adminname=%s AND pw=%s"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,(adminname,pw))
                count, =cur.fetchone()
                return count==1
            
    ### 1. 조회 ###
    # 계정 전체 조회(admin 용)
    def fetch_account(self):
        sql="SELECT userID,name,email,addr FROM accounts ORDER BY userID"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
    # 물품 전체 조회(admin 용)
    def fetch_item(self):
        sql="SELECT serialID,name,price,stock FROM items ORDER BY serialID"
        with self.connect() as conn: # 데이터베이스에 연결하고
            with conn.cursor() as cur: # cur 는 데이터베이스에 명령(sql) 을 전달하는 객체
                cur.execute(sql)
                return cur.fetchall()
    # 주문목록 전체 조회(admin 용)
    def fetch_order(self):
        '''sql="SELECT a.name, i.name, o.num, o.orderdate" \
        "FROM orders AS o" \
        "JOIN accounts AS a" \
        "ON o.clientID=a.userID" \
        "JOIN items as i" \
        "ON o.itemID=i.serialID" \
        "ORDER BY orderID"'''
        # 조회하는 것: orders 데이터베이스
        sql = "SELECT clientname,itemname,num,orderdate FROM orders " \
        "ORDER BY orderID"

        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql) # sql에 입력받은 결과를 실행한다.
                return cur.fetchall() # 모든 dictionary 를 가져옴.

    #### 2. 추가 ####
    # 재고 추가 + 재고 업데이트(완)
    def add_item(self,name,price,stock):
        # 영향을 받는 것: items 데이터베이스
        sql="INSERT INTO items(name,price,stock) VALUES (%s, %s, %s)" \
        "ON DUPLICATE KEY UPDATE price = VALUES(price), stock = stock + VALUES(stock)"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql,(name,price,stock)) # 데이터베이스에 재고를 추가한다.
                conn.commit()
                return True
            except Exception:
                conn.rollback()
                return False
            
    #### 3. 삭제 ####
    # 재고 삭제(완) -> 삭제할 상품이 존재하지 않을 때 vs 삭제할 상품이 존재할 때 case 를 따짐
    def del_item(self,delname,delnum): #삭제할 상품의 이름과, 몇개 삭제할 건지
        # 영향을 받는 것: items 데이터베이스
        sql_sel="SELECT * FROM items WHERE name=%s"
        sql_update="UPDATE items SET stock=stock-%s WHERE name=%s"
        with self.connect() as conn:
            try:
                with conn.cursor(pymysql.cursors.DictCursor) as cur: #데이터베이스에 명령어를 전달할 객체를 생성

                    # 1. 제품이 존재하는지 따짐
                    cur.execute(sql_sel,(delname,))
                    product=cur.fetchone()
                    
                    # 예외처리 1: 제품명 자체가 없는 경우
                    if not product:
                        return False
                    cur_stock=product['stock']
                    print(cur_stock)
                    # 예외처리 2: 차감 수량보다 현재 재고가 적을 경우
                    if cur_stock<int(delnum):
                        return False
                    cur.execute(sql_update,(int(delnum),delname)) #데이터베이스에 명령어를 전달
                conn.commit()
                return True

            except Exception: 
                conn.rollback()
                return False

################################################################################


##################################사용자용#######################################

    # 로그인(일반 사용자용) 검증
    def verify_account(self,email,pw):
        # account 데이터베이스 조회
        sql="SELECT COUNT(*) FROM accounts WHERE email=%s AND pw=%s"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,(email,pw))
                count, =cur.fetchone()
                return count==1

    # 계정 추가(회원가입) + 기존 계정 업데이트
    def insert_account(self,name,email,pw,addr):
        # 영향을 받는 것: account 데이터베이스
        sql="INSERT INTO accounts(name,email,pw,addr) VALUES (%s, %s, %s, %s)"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql,(name,email,pw,addr))
                conn.commit()
                return True
            except Exception:
                conn.rollback()
                return False
    # 주문
    def order_item(self,email,name,num): #ok = self.db.order_item(self.user_email, name, stock)
        # 영향을 받는 것: 1) order 데이터베이스, 2) items 데이터베이스
        sql_sel="SELECT * FROM items WHERE name=%s"
        sql_customersel="SELECT name FROM accounts WHERE email=%s"
        sql_order="INSERT INTO orders(clientname,itemname,num,orderdate) VALUES (%s, %s, %s, %s)"
        sql_items="UPDATE items SET stock=stock-%s WHERE name=%s"
        with self.connect() as conn:
            try:
                with conn.cursor(pymysql.cursors.DictCursor) as cur:
                    # 1. 제품이 존재하는지 따짐
                    cur.execute(sql_sel,(name,))
                    product=cur.fetchone()
                    print(product)
                    # 예외처리 1: 제품명 자체가 없는 경우
                    if not product:
                        print("no product")
                        return False
                    cur_stock=product['stock']
                    # 예외처리 2: 차감 수량보다 현재 재고가 적을 경우
                    if cur_stock<int(num):
                        print("not enough stock")
                        return False

                    cur.execute(sql_customersel,(email,))
                    client=cur.fetchone()['name'] # 고객 이름
                    #print(client)
                    orderdate=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    #print(orderdate)
                    cur.execute(sql_order,(client,name,num,orderdate)) #주문 넣어


                    print("order inserted")
                    cur.execute(sql_items,(num,name)) # 재고 감소
                    conn.commit()
                    return True

            except Exception as e:
                conn.rollback()
                print(f"Database Error: {e}")
                traceback.print_exc()
                return False
            '''내가 해야 하는 것:'''
            
