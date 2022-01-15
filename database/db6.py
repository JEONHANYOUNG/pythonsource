# 데이터 조회
from os import curdir
import sqlite3

conn = sqlite3.connect("./database/test.db", isolation_level=None)

cursor = conn.cursor()

sql = "SELECT * FROM users"
cursor.execute(sql)

# 조회된 데이터 결과 가져오기 : fetchone(), fetchmany(), fetchall()
for row in cursor.fetchall():
    print(row)

conn.close()
