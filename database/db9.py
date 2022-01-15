import sqlite3

conn = sqlite3.connect("./database/test.db", isolation_level=None)

cursor = conn.cursor()

cursor.execute("DELETE FROM users WHERE id=?", (2,))
conn.commit()

for user in cursor.execute("SELECT * FROM users").fetchall():
    print(user)

conn.close()
