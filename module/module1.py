# 모듈 : 함수, 변수, 클래스를 모아 놓은 파일
#      : 다른 파이썬 프로그램에서 불러와 사용

# import random

# 모듈 사용
# import 모듈명  : 모듈에 있는 모든 내용 들어옴

# import math  # java Math 클래스

# # print(dir(math))
# # 올림
# print(math.ceil(3.14))
# # sin
# print(math.sin(1))
# print(math.cos(1))
# print(math.floor(2.5))


# import random

# # random() : 0.0 <= x < 1.0
# print(random.random())  # 0.42037857745081064

# # uniform(min,max) : 지정한 범위 사이의 랜덤 값을 float 리턴
# print(random.uniform(10, 20))

# # randrange(max) : 0 ~ max 사이의 값 중에서 랜덤 값 int 리턴
# # randrange(min,max) : min ~ max 사이의 값 중에서 랜덤 값 int 리턴
# print(random.randrange(10))
# print(random.randrange(5, 10))

# # choice(list) : 리스트 내부의 요소 중에서 랜덤 값 리턴
# print(random.choice([1, 2, 3, 4, 5, 6, 7]))

# # shuffle(list) : 리스트 내부의 요소를 랜덤하게 섞어서 출력
# print(random.shuffle([1, 2, 3, 4, 5, 6, 7]))

# # sample(list,k=숫자) : 리스트의 요소 중에서 k 개 추출
# print(random.sample([1, 2, 3, 4, 5, 6, 7], k=2))


# import time

# print("5초 정지 시작")
# time.sleep(5)
# print("프로그램 종료")
