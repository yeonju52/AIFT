# 주식 시세를 매일 DB로 업데이트하기
import sqlite3
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

"""
테이블이 존재하지 않을 경우에만 생성하게 만드려면

CREATE TABLE IF NOT EXISTS를 사용
"""
class setQuery:
    table_create_company_info = """
    CREATE TABLE IF NOT EXISTS company_info (
        st_code VARCHAR(20) not NULL,  
        nm_code VARCHAR(40),
        last_update TEXT not NULL,
        PRIMARY KEY (st_code)
        )
        """

    # code 중복 기입하면 에러 발생함 (막을 수 있는 방법: Primary Key)
    insert_company_info = """
    INSERT OR REPLACE INTO company_info (st_code, nm_code, last_update) 
    VALUES (?, ?, ?)
    """

    # {} 이 방식일 때는 069500이 69500로 인식함
    select_last_update = """
    SELECT last_update FROM company_info WHERE st_code = :INDEX_NAME
    """

class sqlReader:
    def __init__(self):
        """생성자: DB 연결 및 종목코드 딕셔너리 생성"""
        self.con = sqlite3.connect("kiwoom_tick.db")
        self.curs = self.con.cursor()
        # DB 생성
        self.curs.execute(setQuery.table_create_company_info)
        self.con.commit()
    
    """
    현 DB에서 comapny_info를 통해 last_update date를 알아냄
    # 날짜 정하기 (DB 존재 여부에 따라)
    # Opt1. (DB 생성 X): 해당 종목코드를 처음 접속한 것
        = before_1_year
    # Opt2. (DB 생성 O): 해당 종목코드에 접속한 적 있음. DB-update date를 받아옴
        = self.update[0]
    """
    def get_last_update(self, st_code):
        db_update = []
        for table_name in st_code:
            self.curs.execute(setQuery.select_last_update, {'INDEX_NAME': table_name})
            self.update = self.curs.fetchone()
            if(self.update == None):
                before_1_year = (datetime.today() - relativedelta(years=1)).strftime('%Y%m%d') + '000000'   # now = datetime.now().strftime('%Y%m%d%H%M%S')
                db_update.append(before_1_year)
            else:
                db_update.append(self.update[0])
        return db_update

    def set_query(self, st_code, df):
        df = df.sort_index(ascending=False)
        df.to_sql(st_code, self.con, chunksize=1000, index=False,if_exists='append')
        self.con.commit()
    
    """
    같은 Primary Key 값으로 값을 넣으면 
    무결성 제약조건 에러가 발생

    이미 고유키를 가진 값이 존재하는데 같은것을 또 넣을려해서 생기는 에러

    => 이 성질을 이용해 값을 insert
    """
    def update_comany_info(self, info):
        self.curs.execute(setQuery.insert_company_info, info)
        self.con.commit()

    def __del__(self):
        """소멸자: MariaDB 연결 해제"""
        self.con.close()
    
if __name__ == "__main__":
    print(sqlReader().get_last_update(['114800', '069500', '226490']))
    sqlReader().update_comany_info(['069500', 'kodex_200',  datetime.now().strftime('%Y%m%d%H%M%S')])



'''
안 쓴 sql명령문
    table_create_query = """
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        st_code VARCHAR(20) not NULL,
        dt TEXT not NULL,
        open INTEGER,
        high INTEGER,
        low INTEGER,
        close INTEGER,
        volume INTEGER
        PRIMARY KEY (st_code, dt)
        )
    """

    insert_query = """
    INSERT INTO {TABLE_NAME} (st_code, dt, open, high, low, close, volume)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    drop_table_query = """
    DROP TABLE IF EXISTS {TABLE_NAME}
    """

    sql Updater (성공)
    exercise1) Insert
    self.curs.execute("INSERT INTO company_info VALUES('069500', 'kodex_200', 20221118069500)")
    self.curs.execute("INSERT INTO company_info VALUES('114800', 'kodex_inverse', 20221118114800)")
    self.curs.execute("INSERT INTO company_info VALUES('226490', 'kodex_kospi', 20221118226490)")
    self.con.commit()

    exercise2) Delete
    self.curs.execute("DELETE FROM company_info st_code = "226490")
    self.con.commit()
'''
