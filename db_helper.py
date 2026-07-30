import pymysql
DB_CONFIG=dict(host="localhost",user="root",password="0905",
               database="orderappdb",charset="utf8")
class DB:
    def __init__(self,**config):
        self.config=config

    def connect(self):
        return pymysql.connect(**self.config)

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
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
    # 주문목록 전체 조회(admin 용)
    def fetch_order(self):
        sql="SELECT a.name, i.name, o.num, o.orderdate" \
        "FROM orders AS o" \
        "JOIN accounts AS a" \
        "ON o.clientID=a.userID" \
        "JOIN items as i" \
        "ON o.itemID=i.serialID" \
        "ORDER BY orderID"

        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()

    #### 2. 추가 ####
    # 재고 추가 + 재고 업데이트(완)
    def add_item(self,name,price,stock):
        sql="INSERT INTO items(name,price,stock) VALUES (%s, %s, %s)"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql,(name,price,stock))
                conn.commit()
                return True
            except Exception:
                conn.rollback()
                return False
    #### 3. 삭제 ####
    # 재고 삭제(완)
    def del_item(self,delname,delnum): #삭제할 상품의 이름과, 몇개 삭제할 건지
        sql="UPDATE items" \
        "SET stock=stock-delnum" \
        "WHERE name=delname"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql,(delname,delnum))
                conn.commit()
                return True
            except Exception:
                #print("존재하지 않는 상품")
                conn.rollback()
                return False









    # 로그인(일반 사용자용) 검증
    def verify_account(self,email,pw):
        sql="SELECT COUNT(*) FROM accounts WHERE email=%s AND pw=%s"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,(email,pw))
                count, =cur.fetchone()
                return count==1

    # 계정 추가(회원가입) + 기존 계정 업데이트
    def insert_account(self,name,email,pw,addr):
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
    def order_item(self,name,num,ordedate):
        sql="INSERT INTO orders(clientID,itemID,num,orderdate) VALUES ()"
        with self.connect() as conn:

            raise NotImplementedError