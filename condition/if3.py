import datetime

now = datetime.datetime.now()
print(now)  # 2021-12-21 10:18:20.152773

# 2021년 12월 21일 10시 33분 49초
print(
    "{}년 {}월 {}일 {}시 {}분 {}초".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second
    )
)

# 오전, 오후(시간대 확인) : 오전
if now.hour < 12:
    print("오전")
else:
    print("오후")

# 삼항 연산자
# 조건 ? 참 : 거짓(X)
# 참일때 실행하는 구문 if 조건 else 거짓일 때

str = "안녕하세요" if True else "반갑습니다."
print(str)  # 안녕하세요

# [] : 리스트 , 비어있는 경우 false
a = []
str = a if a else "비어있는 배열"
print(str)  # 비어있는 배열


# 중첩 if
a = 75
if a > 50:
    if a < 100:
        print("50보다 크고 100보다 작다")
    else:
        print("100보다 크다")
else:
    print("50보다 작다")  # 50보다 크고 100보다 작다
