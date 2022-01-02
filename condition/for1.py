# range() : 특정 범위 지정(시작 값(보여지고), 끝나는 값(제외), 배수의 값)

print(range(5))  # range(0, 5)
print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(1, 5)))  # [1, 2, 3, 4]
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]


print()


# 1~10 출력

for i in range(2, 101, 2):
    print(i, end=" ")  # 1 2 3 4 5 6 7 8 9 10

print()


# 1~100 까지 합계
sum1 = 0

for i in range(1, 100):
    sum1 += i
    print("1~100 합계 ", sum1)

print()

# 사용자가 입력한 숫자까지 합계를 구한 후 출력하기
num = int(input("숫자 입력")) + 1
hap = 0
for i in range(1, num):
    hap += i

print("합계 ", hap)

print()

# 1~100 합계 : range() + sum()
print("1~100 합계 : ", sum(range(1, 101)))
print("1~100 홀수 합계 :", sum(range(1, 101, 2)))
print("1~100 짝수 합계 :", sum(range(2, 101, 2)))

print()

# 역순으로
for i in range(5, -1, -1):
    print(i, end=" ")  # 5 4 3 2 1 0


print()
