# 데이터 조회
import sqlite3

conn = sqlite3.connect("./database/test.db", isolation_level=None)

cursor = conn.cursor()

# sql = "SELECT * FROM users WHERE id=?"

# cursor.execute("SELECT * FROM users WHERE id = %s" % 4)

sql = "SELECT * FROM users WHERE id IN (?,?)"

cursor.execute(sql, (3, 5))

# 조회된 데이터 결과 가져오기 : fetchone(), fetchmany(), fetchall()
for row in cursor.fetchall():
    print(row)

conn.close()
