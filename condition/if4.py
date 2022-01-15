# 다중 조건
# if ~ elif ~ else

num = 90
if num >= 90:
    print("등급 A")
elif num >= 80:
    print("등급 B")
elif num >= 70:
    print("등급 C")
else:
    print("등급 D")


# 점수 구간에 맞춰 학점 출력하기
# 점수입력 받은 후 학점 출력
# A : 81 ~ 100
# B : 61 ~ 80
# C : 41 ~ 60
# D : 21 ~ 40
# F : 나머지

jumsu = int(input("점수 입력 "))
if jumsu > 80:
    print(jumsu, "A 학점")
elif jumsu > 60:
    print(jumsu, "B 학점")
elif jumsu > 40:
    print(jumsu, "C 학점")
elif jumsu > 20:
    print(jumsu, "D 학점")
else:
    print(jumsu, "F 학점")


# 산술 계산기 => 두 개의 숫자 입력 받기
# +,-,*,/,//,**,%

num1 = int(input("첫번째 수 입력 "))
op = input("+,-,*,/,//,**,% 중 연산자 입력")
num2 = int(input("두번째 수 입력 "))

if op == "+":
    print(num1, op, num2, "=", num1 + num2)
elif op == "-":
    print(num1, op, num2, "=", num1 - num2)
elif op == "*":
    print(num1, op, num2, "=", num1 * num2)
elif op == "/":
    print(num1, op, num2, "=", num1 / num2)
elif op == "//":
    print(num1, op, num2, "=", num1 // num2)
elif op == "**":
    print(num1, op, num2, "=", num1 ** num2)
elif op == "%":
    print(num1, op, num2, "=", num1 % num2)
