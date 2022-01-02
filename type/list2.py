# 리스트 연산자

# + : 리스트 더하기
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)  # [1, 2, 3, 4, 5, 6]
# print(a[0] + b[1])  # 6

# * : 반복
# a = [1, 2, 3]
# print(a * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트 수정
# a = [1, 2, 3]
# a[2] = 4
# print(a)  # [1, 2, 4]
# a[1] = "Life"
# print(a)  # [1, 'Life', 3]

# b = [4, 5, 6]
# b[1:2] = [10, 11]  # [4, 10, 11, 6] => 1번 자리에 10, 11을 부여
# b[1] = [10, 11] -> # [4, [10, 11], 6]
# print(b)  # [4, 10, 11, 6] => 1번 자리에 10, 11을 부여

# 리스트 삭제
# a = [1, 2, 3]
# a[1:3] = []
# print(a) # [1]
# del a[1]
# print(a)  # [1,3]
# del a  # del 객체 (다른 )

# 문제
# 리스트 안의 숫자가 100 이상인 숫자 출력하기
# numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# print()
# print("*" * 50)
# print("100 이상 숫자")
# print("*" * 50)
# for num in numbers:
#     if num >= 100:
#         print(num)


# # 리스트 안의 숫자가 홀수인지 짝수인지 출력하기
# print()
# print("*" * 50)
# print("홀/짝 판별")
# print("*" * 50)
# for num in numbers:
#     if num % 2 == 0:
#         print("{} 짝수".format(num))
#     else:
#         print("{} 홀수".format(num))

# 리스트 안의 숫자들의 자리수 출력하기
# # 273 => 3자리
# print()
# print("*" * 50)
# print("각 숫자의 자릿수 출력")
# print("*" * 50)
# for num in numbers:
#     if num >= 100:
#         print("{} : {} 자릿수 ".format(num, len(str(num))))

# 아래 리스트를 풀어서 출력
# list_of_list = [
#     [1, 2, 3],
#     [4, 5, 6, 7],
#     [8, 9],
# ]

# 출력 결과 1 2 3 4 5 6 7 8 9
# for list1 in list_of_list:
#     for num in list1:
#         print(num, end=" ")


# 리스트 함수
# 1) append : 마지막에 요소 추가
# list1 = [1, 2, 3]
# print(list1)  # [1, 2, 3]

# 하나의 요소 추가
# list1.append(7)
# print(list1)  # [1, 2, 3, 7]

# 여러 개의 요소 추가
# list2 = [4, 5, 6]
# print(list1 + list2)  # [1, 2, 3, 7, 4, 5, 6]
# list1.append(list2)
# print(list1)  # [1, 2, 3, [4, 5, 6]]


# 1 ~ 100 숫자 중에서 짝수만 들어있는 리스트 생성하고 출력하기
# even = []  # even = list()
# for i in range(2, 101, 2):
#     if i % 2 == 0:
#         even.append(i)
# print(even)  # 2의 배수가 나옴


# 2) sort() : 오름차순 정렬
# list1 = [25, 75, 15, 9, 6, 3, 35]
# print("정렬 전", list1)  # 정렬 전 [25, 75, 15, 9, 6, 3, 35]
# list1.sort()
# print("정렬 후", list1)  # 정렬 후 [3, 6, 9, 15, 25, 35, 75]

# print()
# list2 = ["k", "z", "b", "a", "q", "r"]
# print("정렬 전", list2)  # 정렬 전 ['k', 'z', 'b', 'a', 'q', 'r']
# list2.sort()
# print("정렬 후", list2)  # 정렬 후 ['a', 'b', 'k', 'q', 'r', 'z']

# print()  # 대,소문자 결합되어있을 경우 대문자부터 정렬
# list3 = ["k", "z", "B", "a", "Q", "r"]
# print("정렬 전", list3)  # 정렬 전 ['k', 'z', 'B', 'a', 'Q', 'r']
# list3.sort()
# print("정렬 후", list3)  # 정렬 후 ['B', 'Q', 'a', 'k', 'r', 'z']


# print()  # 한글도 정렬이 잘됌
# list4 = ["ㅎ", "ㄱ", "ㄷ", "ㅅ", "ㅂ", "ㅇ"]
# print("정렬 전", list4)  # 정렬 전 ['ㅎ', 'ㄱ', 'ㄷ', 'ㅅ', 'ㅂ', 'ㅇ']
# list4.sort()
# print("정렬 후", list4)  # 정렬 후 ['ㄱ', 'ㄷ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅎ']

# print()
# list5 = ["abc", "efg", "jar", "gof", "web", "aaf"]
# print("정렬 전", list5)  # 정렬 전 ['abc', 'efg', 'jar', 'gof', 'web', 'aaf']
# list5.sort()
# print("정렬 후", list5)  # 정렬 후 ['aaf', 'abc', 'efg', 'gof', 'jar', 'web']

# sort(reverse=True) : 내림 차순 정렬
# print()
# list6 = [25, 75, 15, 9, 6, 3, 35]
# print("정렬 전", list6)  # 정렬 전 [25, 75, 15, 9, 6, 3, 35]
# list6.sort(reverse=True)
# print("정렬 후", list6)  # 정렬 후 [75, 35, 25, 15, 9, 6, 3]

# 3) reverse() : 리스트 역순으로 처리(sort와 같이 써야함)
# print("\n")
# print("reverse() 사용")
# list7 = [25, 75, 15, 9, 6, 3, 35]
# print("정렬 전", list7)  # 정렬 전 [25, 75, 15, 9, 6, 3, 35]
# list7.sort()
# list7.reverse()
# print("정렬 후 거꾸로 출력", list7)  # 정렬 후 [75, 35, 25, 15, 9, 6, 3]


# 4) index() : 위치 변환
# list1 = [34, 25, 9, 75]
# print("9가 있는가? ", list1.index(9))  # 2
# print("45가 있는가? ", list1.index(45))  # ValueError: 45 is not in list


# 5) insert() : 리스트 내의 특정 위치에 요소 삽입
# list1 = [34, 25, 9, 75]
# list1.insert(1, 56)
# print(list1) # [34, 56, 25, 9, 75]


# 6) remove() : 리스트 요소 제거
# list1 = [34, 25, 9, 75, 9]
# list1.remove(25)
# print(list1)  # [34, 9, 75, 9]
# list1.remove(9)  # 중복 되어있다면 앞 요소가 먼저 제거됨
# print(list1)  # [34, 75, 9]


# 7) pop() : 리스트 요소 맨 마지막 요소 돌려주고 요소는 삭제
# list1 = [34, 25, 9, 75, 9]
# list1.pop()
# print(list1)  # [34, 25, 9, 75] 맨 마지막 요소 삭제

# pop(인덱스 값) : 해당 인덱스 요소를 돌려주고 그 요소는 삭제
# print(list1.pop(1)) # 25
# print(list1) # [34, 9, 75]


# 8) count() : 리스트 내의 특정 요소의 개수 세기
# list1 = [34, 25, 9, 75, 9]
# print(list1.count(9))  # 2개


# 9) extend() : 리스트 확장(+와 같은 결과)
# list1 = [34, 25, 9, 75, 9]
# list2 = [11, 12, 13]
# list1.extend(list2)
# print(list1)  # [34, 25, 9, 75, 9, 11, 12, 13]


# 10) clear() : 리스트 요소 모두 삭제
# list1.clear()
# print(list1)  # []


# 리스트 안에 요소가 비어있는 경우는 false로 인식
# list1 = []
# if list1:
#     print("True")
# else:
#     print("False")  # False(리스트에서 아무것도 없으면 false)

# str1 = ""
# if str1:
#     print("True")
# else:
#     print("False")  # False


# 요소 in 리스트 : 해당 요소가 리스트 안에 들어있는지 판별
# fruit = ["사과", "배", "딸기", "포도", "메론"]

# if "딸기" in fruit:  # not in(들어 있지 않으냐)
#     print("딸기 있음")
# else:
#     print("딸기 없음")


# enumerate() : 인덱스 값 사용
list1 = [23, 12, 36, 53, 19]

for item in list1:
    print(item)
# 23
# 12
# 36
# 53
# 19

print()

for item in enumerate(list1, start=1):
    print(item)
# (0, 23)
# (1, 12)
# (2, 36)
# (3, 53)
# (4, 19)

print()

for idx, item in enumerate(list1, start=1):
    print("%d : %d" % (idx, item))
# 1 : 23
# 2 : 12
# 3 : 36
# 4 : 53
# 5 : 19

print()


# for idx, item in enumerate(list1, start=1):
#     print("%d : %d" % (idx,item))


# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70,60,55,75,95,90,80,85,100]
# A 학급에 평균을 구하시오.
a_class = [70, 60, 55, 75, 95, 90, 80, 85, 100]
# total = 0
# for num in a_class:
#     total += num

# print("A 학급의 평균 %.2f" % (total / len(a_class)))  # A 학급의 평균 78.89

# print("A 학급의 평균 %.2f" % (sum(a_class) / len(a_class)))

# ord() : 코드 값 반환
# print(ord("A"))  # 65

# chr() : 코드 값을 문자로 반환
# print(chr(65))  # A


# 주차장 프로그램
# 총 5대의 차가 주차 가능 / 맨 마지막 차량부터 빠져나갈 수 있음
# pass : 오류가 나오지 않게 임시로 지정

# parking_lot = []
# top, car_name = 0, "A"

# while True:
#     no = int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 : "))

#     if no <= 3:
#         if no == 1:
#             if top >= 5:
#                 print("주차장은 꽉 찼음")
#             else:
#                 parking_lot.append(car_name)
#                 print("{} 자동차 들어감. 주차장 상태 ==> {}".format(car_name, parking_lot))

#                 top += 1
#                 car_name = chr(ord(car_name) + 1)
#         elif no == 2:
#             if top > 0:
#                 outCar = parking_lot.pop()
#                 print("{} 자동차 나감. 주차장 상태 ==> {}".format(outCar, parking_lot))

#                 top -= 1
#                 car_name = chr(ord(car_name) + 1)
#             else:
#                 print("빠져나갈 자동차가 없음")
#         else:
#             print("프로그램 종료")
#             break
#     else:
#         print("번호를 입력해 주세요")

# List Comprehension

# 1~100 숫자가 들어있는 리스트 생성

# numbers = [1,2,3,4,5,....]

# numbers = []
# numbers.append(1)
# numbers.append(2)
# numbers.append(3)
# numbers.append(4)
# numbers.append(5)


# numbers = []
# for n in range(1, 101):
#     numbers.append(n)

# numbers = list(range(1, 101))
# print(numbers)


# numbers = [n for n in range(1, 101)]
# print(numbers)

# list1 = ["갑", "을", "병", "정", "경"]
# 정을 제외하고 출력
# for s in list1:
#     if s != "정":
#         print(s)

# list2 = [s for s in list1 if s != "정"]
# print(list2)


# 1 ~ 100 까지 홀수를 리스트로 생성하고 출력
# list1 = [x for x in range(1, 101) if x % 2 == 1]
# print(list1)

# 아래 리스트 항목 중에서 5글자 이상의 단어만 출력
# list1 = ["nice", "study", "python", "anaconda", "java"]
# list2 = [s for s in list1 if len(s) >= 5]
# print(list2)


# 소문자만 모아서 새로운 리스트로 생성하고 출력
# list1 = ["a", "b", "c", "d", "e", "f", "h"]
# list2 = [s for s in list1 if s.islower()]
# print(list2)


# 각 요소의 2배를 한 리스트를 생성하고 출력
list1 = [1, 2, 3, 4, 5]
# list2 = []
# for x in list1:
#     list2.append(x*2)

# list2 = [x * 2 for x in list1]
# print(list2)


# print([x * x for x in range(5)])

print([[x, x + 1, x + 2] for x in [1, 2, 3]])
