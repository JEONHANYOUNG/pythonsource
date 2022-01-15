# 인 메모리 방식
import sqlite3
from datetime import datetime

print("sqlite3.versiion : {}".format(sqlite3.version))

now = datetime.now()
print("now : {}".format(now))


# 날짜를 원하는 포맷형식으로 변경
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")
print("nowDateTime {}".format(nowDateTime))
