# 대량의 데이터 삽입
import sqlite3
from datetime import datetime

conn = sqlite3.connect("./database/test.db", isolation_level=None)

cursor = conn.cursor()

now = datetime.now()
now_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

user_list = (
    (2, "Park", "Park12@naver.com", "010-1234-1235", "Park.com", now_date_time),
    (4, "Cho", "Cho12@naver.com", "010-1234-1236", "Cho.com", now_date_time),
    (5, "Yoo", "Yoo12@naver.com", "010-1234-1237", "Yoo.com", now_date_time),
)

sql = """
    INSERT INTO users(id,username,email,phone,website,regdate)
    VALUES(?,?,?,?,?,?)
"""
cursor.executemany(sql, user_list)
conn.commit()
conn.close()
