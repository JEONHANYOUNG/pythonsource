import sqlite3

conn = sqlite3.connect("./database/test.db", isolation_level=None)

cursor = conn.cursor()

param1 = ("Hong", 2)
cursor.execute("update users set username=? where=id=?", param1)
conn.commit()

for user in cursor.execute("select * from users").fetchall():
    print(user)


conn.close()
