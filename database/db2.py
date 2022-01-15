import sqlite3

# database 생성
# isolation_level(autocommit)
conn = sqlite3.connect("./database/test.db", isolation_level=None)

# cursor 획득
cursor = conn.cursor()
print("cursor {}".format(cursor))


# 테이블 생성
sql = """CREATE TABLE IF NOT EXISTS users(id integer primary key, username text, email text, phone text, website text, regdate text)"""

cursor.execute(sql)
conn.commit()
conn.close()
