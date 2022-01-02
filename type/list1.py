# 리스트 자료형
# 배열, List 같은 개념
# 인덱스로 접근, 삽입, 삭제 가능
# 인덱스의 값들은 특정 타입을 제한하지 않음


# 리스트 생성
list1 = []
list2 = [1, 2, 3]
print(list1)  # []
print(list2)  # [1, 2, 3]

list1 = list()
list2 = list([1, 2, 3])
print(list1)  # [] 위의 출력값과 동일
print(list2)  # [1, 2, 3] 위의 출력값과 동일


list3 = ["a", "b", "c", 1, 2]
print(list3)  # ['a', 'b', 'c', 1, 2]

list4 = ["a", "b", "c", 1, 2, 6.5, True]  # boolean 타입도 가능
print(list4)  # ['a', 'b', 'c', 1, 2, 6.5, True]

list5 = ["a", "b", "c", ["Life", "is", "short"]]  # 리스트 안에 리스트 개념 가능
print(list5)  # ['a', 'b', 'c', ['Life', 'is', 'short']]


# 인덱싱과 슬라이싱
list3 = ["a", "b", "c", 1, 2]
print("list3[0]", list3[0])  # list3[0], a
print("list3[0]", list3[-1])  # list3[0], 2


list5 = ["a", "b", "c", ["Life", "is", "short"]]
print("list5[2]", list5[2])  # list5[2], c
print("list5[3]", list5[3])  # list5[3], ['Life', 'is', 'short']
print("list5[3][0]", list5[3][0])  # list5[3][0], Life
print("list5[3][-1]", list5[3][-1])  # list5[3][-1], short


list6 = ["1", "2", ["a", "b", ["Life", "is", "short"]]]
print("list6[2][2][1]", list6[2][2][1])  # list6[2][2][1], is
print("list6[-1][-1][-2]", list6[-1][-1][-2])  # list6[-1][-1][-2], is


# 슬라이싱
list3 = ["a", "b", "c", 1, 2]
print("list3[0:3]", list3[0:3])  # list3[0:3] ['a', 'b', 'c']
print("list3[:3]", list3[:3])  # 앞에 생략, list3[:3] ['a', 'b', 'c']
print("list3[:-2]", list3[:-2])  # list3[:-2] ['a', 'b', 'c']


list5 = ["a", "b", "c", ["Life", "is", "short"]]
print("list5[3:]", list5[3:])  # list5[3:] [['Life', 'is', 'short']]
print("list5[3][:2]", list5[3][:2])  # list5[3][:2] ['Life', 'is']
