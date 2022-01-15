# 람다함수
# 단일문으로 표현되는 익명 함수
# 익명함수란 이름이 없는 구현체만 존재하는 함수를 의미
# 코드 상에서 한번만 사용될 때 굳이 함수로 만들지 않고 1회성으로 만들 때 사용


# def square(x):
#     return x ** 2


# print(square(5))


# 람다함수로 변경

# square = lambda x: x ** 2
# print(type(square))  # <class 'function'>
# print(square(5))


# def add(x, y):
#     return x + y

# add = lambda x, y: x + y


# print(add(15, 2))


# def str_len(s):
#     return len(s)


# strings = ["bob", "charles", "alexander2", "teddy"]
# # 문자의 길이가 짧은 순서대로 sort 하기
# # strings.sort(key=str_len)
# strings.sort(key=lambda s: len(s))
# print(strings)


# filter,map,reduce 함수
# lambda가 유용하게 사용되는 3가지 대표적 함수
# 함수형 프로그래밍의 기본 요소
# filter : 각 원소를 주어진 수식에 따라 변형하여 새로운 리스트 반환
# map : 각 원소를 주어진 수식에 따라 변형하여 새로운 리스트 반환
# reduce : 차례대로 앞 2개의 원소를 가지고 연산, 연산의 결과가 또 다음 연산의
#          입력으로 진행됨. 따라서 마지막까지 진행되면 최종 출력은 한 개의
#          값만 남게 됨


# filter(함수,리스트)

# 넘어온 리스트 요소 중에서 짝수만 추출해서 새로운 리스트로 반환

# even_list = []


# def even(arr):
#     for n in arr:
#         if n % 2 == 0:
#             even_list.append(n)


# even([1, 2, 3, 6, 8, 9])
# print(even_list)

# filter 함수를 써서 짝수만 구하기
# def even(n):
#     return n % 2 == 0


# nums = [1, 2, 3, 6, 8, 9]
# # print(list(filter(even, nums)))
# print(list(filter(lambda n: n % 2 == 0, nums)))


# 5보다 크고 10보다 작은 요소들을 추출해서 새로운 리스트로 출력
# filter()

# nums = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]


# # def func(x):
# #     # return x > 5 and x < 10
# #     return 5 < x < 10


# # print(list(filter(func, nums)))


# print(list(filter(lambda x: x > 5 and x < 10, nums)))


# map(함수, 리스트)


# def mul(x):
#     return x ** 2


# nums = [1, 2, 3, 6, 8, 10, 11, 12, 13, 14, 15]
# # print(list(map(mul, nums)))
# print(list(map(lambda x: x ** 2, nums)))
# print(list(map(lambda x: x % 2 == 0, nums)))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 3의 배수를 문자열로 변환한 후 리스트로 출력
# [1,2,'3',4,5,'6'...]
# nums_result = []


# def str_check(arr):
#     for i in arr:
#         if i % 3 == 0:
#             nums_result.append(str(i))
#         else:
#             nums_result.append(i)
#     return nums_result


# print(str_check(nums))


# map() 사용
# def str_check(i):
#     if i % 3 == 0:
#         return str(i)
#     else:
#         return i


# print(list(map(str_check, nums)))


# reduce : 함수를 차례대로 거치면서 원하는 결과만 남기는 것
import functools

a = [1, 3, 5, 8]

# 리스트 합
# hap = 0
# for i in a:
#     hap = hap + i
print(functools.reduce(lambda x, y: x + y, a))
print(functools.reduce(lambda x, y: x * y, a))
