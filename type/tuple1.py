# tuple
# 리스트와 유사
# () 생성 / 한번 생성이 되면 그 값을 삭제, 수정할 수 없음

t1 = ()
t1 = tuple()

t2 = 1, 2, 3
t3 = (1,)  # 1개의 요소만을 가질 때 요소 뒤에 콤마를 반드시 붙여야 함
t4 = (1, 2, "Life", "is")
t5 = (1, 2, ("Life", "is"))

print(t1)  # ()
print(t2)  # (1, 2, 3)
print(t3)  # (1,)
print(t4)  # (1, 2, 'Life', 'is')
print(t5)  # (1, 2, ('Life', 'is'))

# tuple 삭제(삭제 안됨)
del t4[0]  # TypeError: 'tuple' object doesn't support item deletion


# tuple 수정(수정 안됨)
t4[0] = 5  # TypeError: 'tuple' object does not support item assignment


# 연산자
# +
print(t2 + t3)  # (1, 2, 3, 1)

# *
print(t2 * t3)

# 인덱싱과 슬라이싱
print("t4[1]", t4[1])
print("t5[0:3]", t5[0:3])


# 튜플 -> 리스트
print(list(t4))  # [1, 2, 'Life', 'is']

list1 = list(t4)
list1[0] = 5
print(list1)


# 리스트 -> 튜플
t6 = tuple(list1)
print(t6)
