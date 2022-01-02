# set : 집합
# 중복을 허용하지 않음
# 순서가 없음(인덱싱 없음)

s1 = set()
s2 = set([1, 2, 3, 4, 5])
s3 = set([1, 2, 3, 3, 5, 6])

print(s1)  # set()
print(s2)  # {1, 2, 3, 4, 5}
print(s3)  # {1, 2, 3, 5, 6}

# list => set(중괄호)
list1 = [5, 6, 7, 8, 9]
print(list1)  # [5, 6, 7, 8, 9]
print(set(list1))  # {5, 6, 7, 8, 9}


# tuple => set
t1 = (1, 2, 3)
print(set(t1))  # {1, 2, 3}


# set => list
print(list(s2))  # [1, 2, 3, 4, 5]

# set => tuple
print(tuple(s2))  # (1, 2, 3, 4, 5)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])


# 교집합
print(s1.intersection(s2))  # {4, 5, 6}
print(s1 & s2)  # {4, 5, 6}

# 합집합
print(s1.union(s2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1 | s2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 차집합
print(s1.difference(s2))  # {1, 2, 3}
print(s1 - s2)  # {1, 2, 3}


# 추가
s1.add(7)
print(s1)  # {1, 2, 3, 4, 5, 6, 7}


s1.add(4)
print(s1)  # {1, 2, 3, 4, 5, 6, 7}


# 여러 개 추가 : update
s1.update([8, 9, 10])
print(s1)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


# 제거 : remove
s1.remove(10)
print(s1)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
