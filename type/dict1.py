# dictionary == map 동일(자바에서)
# key, value
# {key1:value1, key2:value2}
# 키 값은 중복 안됨 {1: values1, 1:values2}

# 생성(키 값은 다양한 형태 사용 가능)
# from typing import Counter


dict1 = {"name": "Park", "age": 12}
print(dict1)  # {'name': 'Park', 'age': 12}

dict2 = {0: "Hello Python", 1: "Hello coding"}
print(dict2)  # {0: 'Hello Python', 1: 'Hello coding'}

dict3 = {0: "Hello Python", 1: "Hello coding", 3: [1, 2, 3, 4, 5]}
print(dict3)  # {0: 'Hello Python', 1: 'Hello coding', 3: [1, 2, 3, 4, 5]}

# 특정 키만 출력
dict1 = {"name": "Park", "age": 12}
dict2 = {0: "Hello Python", 1: "Hello coding"}
dict3 = {0: "Hello Python", 1: "Hello coding", 3: [1, 2, 3, 4, 5]}
print(dict1["name"])  # Park
print(dict2[0])  # Hello Python
print(dict3[3])  # [1, 2, 3, 4, 5]
print(dict1["addr"])  # KeyError: 'addr'(없는 거 사용 시)


# 추가
dict1 = {"name": "Park", "age": 12}
dict1["birth"] = "1223"
print(dict1)  # {'name': 'Park', 'age': 12, 'birth': '1223'}

dict2 = {0: "Hello Python", 1: "Hello coding"}
dict2[2] = ["jsp", "java", "python"]
print(dict2)  # {0: 'Hello Python', 1: 'Hello coding', 2: ['jsp', 'java', 'python']}


# 리스트 안에 숫자들이 몇번 나오는지 카운트 한 후 딕셔너리로 출력
numbers = [1, 2, 4, 3, 5, 6, 3, 7, 8, 6, 3, 3, 2, 1, 4, 5, 6, 6, 6]
counter = {}

#  출력  {1: 3 ,2: 4, 3:5,....}
print(numbers.count(1))

for number in numbers:
    counter[number] = numbers.count(number)

print(counter)


# 삭제
dict1 = {"name": "Park", "age": 12}
del dict1["age"]
print(dict1)


# 함수
dict1 = {"name": "Park", "age": 12}
dict2 = {0: "Hello Python", 1: "Hello coding"}
dict3 = {0: "Hello Python", 1: "Hello coding", 3: [1, 2, 3, 4, 5]}

# 1) keys() : key 리스트 만들기
print(dict1.keys())  # dict_keys(['name', 'age'])
print(dict2.keys())  # dict_keys([0, 1])
print(dict3.keys())  # dict_keys([0, 1, 3])

for k in dict1.keys():
    print(k)  # name
# age

# 2) values() : value 리스트 만들기
print(dict1.values())  # dict_values(['Park', 12])
print(dict2.values())  # dict_values(['Hello Python', 'Hello coding'])
print(dict3.values())  # dict_values(['Hello Python', 'Hello coding', [1, 2, 3, 4, 5]])

for v in dict1.values():
    print(v)  # Park
# 12

# 3) items() : key,value 쌍으로 가져오기
print(dict1.items())  # dict_items([('name', 'Park'), ('age', 12)])
print(dict2.items())  # dict_items([(0, 'Hello Python'), (1, 'Hello coding')])
print(
    dict3.items()
)  # dict_items([(0, 'Hello Python'), (1, 'Hello coding'), (3, [1, 2, 3, 4, 5])])

for k, v in dict1.items():
    print(k, v)  # name Park, age 12

# 4) get() : key로 value 값 가져오기
print(dict1.get("name"))  # Park
print(dict1["name"])  # Park

# get 일때, 없는 키를 가져오라고 할때 작동하는 게 다름
print(dict1.get("brith"))  # None (안전한 방식)
print(dict1["brith"])  # KeyError: 'brith'

# 5) in : 해당 key가 딕셔너리 안에 있는지 확인
print("name" in dict1)  # True
print("brith" in dict1)  # False


dict4 = {"봄": "딸기", "여름": "수박", "가을": "사과", "겨울": "귤"}
# 계절만 출력
for k in dict4.keys():
    print(k, end=" ")

# 과일만 출력
for v in dict4.values():
    print(v, end=" ")


# 가을에 해당하는 과일 출력
print(dict4["가을"])
print(dict4.get["가을"])


# 딕셔너리에 사과가 포함되었는지 출력
for v in dict4.values():
    if v == "사과":
        print("사과가 포함됨")
    break
else:
    print("사과가 포함되지 않음")


# 딕션너리 컴프리헨션
fruits = [fruit for fruit in dict4.values()]
print(fruits)

fruits = {fruit for fruit in dict4.values()}
print(fruits)


# 딕셔너리를 생성하고 출력하기
# "A":90, "B":80, "C":70 의 값을 딕셔너리로 생성
dict5 = {"A": 90, "B": 80, "C": 70}
print(dict5)

# 위의 생성된 딕셔너리에 B키에 해당하는 값 출력
print(dict5["B"])

# B 키 값을 삭제한 후 딕셔너리 출력
del dict5["B"]
print(dict5)


# "성인":10000, "청소년":7000, "아동":3000 딕셔너리 생성
dict6 = {"성인": 10000, "청소년": 7000, "아동": 3000}
print(dict6)

# "소아":0 항목 추가
dict6["소아"] = 0
print(dict6)

# key 값만 출력
print(dict6.keys())

# value 값만 출력
print(dict6.values())
