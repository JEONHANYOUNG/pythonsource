# 연산자

# 문자열과 숫자의 + 는 허용하지 않음
str1 = "123" # 자바 (자바 스크립트) "123"+1 => 1231

#TypeError: can only concatenate str (not "int") to str 
# => (타입 에러) , 둘 중에 하나는 타입 변환 시켜줘야함
print(int(str1)+1) # 124

s1, s2, s3 = "100", "100.123", 999.999
print(s1 + s2) # 연결 => 100100.123
#print(s1 + s2 + s3) #can only concatenate str (not "float") to str

# 대입연산자 : +=, -=, *=, /=, //=(정수 개념의 나눗셈), %=(나누고 다시 담는 것)
money, c500, c100, c50, c10 = 0,0,0,0,0

money = 7777

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print('동전교환')
print("500원 : %d개" % c500)      # 500원 : 15개
print("100원 : %d개" % c100)      # 100원 : 2개
print("50원 : %d개" % c50)        # 50원 : 1개
print("10원 : %d개" % c10)        # 10원 : 2개
print("나머지 돈 : %d원" % money) # 나머지 돈 : 7원


# 관계 연산자 : >,<, >=, <=, !=(같지 않음), ==
print()
print("---- 관계 연산자 ----")
a, b = 10, 0
print("a == b", a==b) # a == b False
print("a != b", a!=b) # a != b True
print("a >= b", a>=b) # a >= b True
print("a <= b", a<=b) # a <= b False

# 논리 연산자 : and, or, not (자바 &&, || 사용 못함)
print()
print("---- 논리 연산자 ----")
a, b, c = 100, 60, 15
print("and ", a > b and b > c) # and  True
print("or ", a > b or b > c)   # or  True
print("not", not b < c)        # not True


