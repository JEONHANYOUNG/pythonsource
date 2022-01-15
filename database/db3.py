# insert
import sqlite3
from datetime import datetime

conn = sqlite3.connect("./database/test.db", isolation_level=None)

cursor = conn.cursor()

now = datetime.now()
now_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

# sql = """INSERT INTO users VALUES(1, "Kim", "kim12@naver.com", "010-1234-1234", "Kim.com", ?)"""
# cursor.execute(sql, (now_date_time,))

sql = """INSERT INTO users VALUES(?,?,?,?,?,?)"""
cursor.execute(
    sql,
    (
        2,
        "Kim",
        "kim12@naver.com",
        "010-1234-1234",
        "Kim.com",
        now_date_time,
    ),
)
conn.commit()
conn.close()
