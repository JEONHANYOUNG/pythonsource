# 파일 출력

# 파일 생성
# f = open("./test1.txt", "w")
# print(dir(f))
# f.close()


# 파일 생성 + 쓰기
# f = open("./test1.txt", "w", encoding="utf-8")
# f.write("안녕하세요\n반갑습니다.")
# f.close()


# 파일 생성 + 1~ 10 쓰기
# f = open("./test1.txt", "w", encoding="utf-8")
# for i in range(1, 11):
#     f.write(str(i) + "\n")  # +: 'int' and 'str'
# f.close()

# 파일 쓰기(기존 파일에 덧붙여서)
# f = open("./test1.txt", "a", encoding="utf-8")
# for i in range(10):
#     f.write("안녕하세요\n")
# f.close()


# 파일 쓰기(리스트)
# f = open("./test2.txt", "w", encoding="utf-8")
# list1 = ["kim\n", "park\n", "cho\n"]
# # f.write(list1) # TypeError: write() argument must be str, not list
# # for i in list1:
# #     f.write(i + "\n")
# f.writelines(list1)

# 파일 쓰기(딕셔너리)
# f = open("./test3.txt", "w", encoding="utf-8")
# dict1 = {"name": "hong", "age": 25, "addr": "서울"}

# 딕셔너리 => items(), keys(), values()
# for k, v in dict1.items():
#     f.writelines("{} : {}\n".format(k, v))
# f.close()

# with 구문 : close() 자동으로 처리

# with open("./test1.txt", "w") as f:
#     print(dir(f))


# with open("./test1.txt", "w", encoding="utf-8") as f:
#     for i in range(1, 11):
#         f.write(str(i) + "\n")


# with open("./test2.txt", "w", encoding="utf-8") as f:
#     list1 = ["kim\n", "park\n", "cho\n"]

#     # for i in list1:
#     #     f.write(i + "\n")
#     f.writelines(list1)


# 1000명의 키와 몸무게를 랜덤하게 생성한 후 파일에 출력
import random

hanguls = list("가나다라마바사아자차카타파하")

with open("./info.txt", "w", encoding="utf-8") as f:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        f.writelines("{}, {}, {}\n".format(name, weight, height))
