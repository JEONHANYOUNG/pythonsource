# 변수 선언 : 어떤 데이터를 담을 것인지에 따라서 타입이 결정
a=3 
b=4

print("a+b=", a+b) #7
print("a-b=", a-b) #-1
print("a*b=", a*b) #12
print("a/b=",  a/b) #0.75
print("a//b=", a//b) #0(자바에서 사용했던 나누기 개념과 동일)
print("a**b=", a**b) #81(지수 개념)
print("a%b=", a%b) #3(나머지 값)

# 타입변환 - bool(타입을 변환할 값 or 변수)
print()

#99 <class 'int'> True <class 'bool'>
print("99",type(99), bool(99), type(bool(99))) # True

#99 <class 'str'> True <class 'bool'>
print("99",type("99"), bool("99"), type(bool("99"))) # True

#0 <class 'str'> True <class 'bool'>
print("0",type("0"), bool("0"), type(bool("0"))) # True 

#0 <class 'int'> False <class 'bool'>
print("0",type(0), bool(0), type(bool(0))) # False => 0일때만 false

#1 <class 'int'> True <class 'bool'>
print("1",type(1), bool(1), type(bool(1))) # True => 1일때는 true

#0.1 <class 'float'> True <class 'bool'>
print("0.1",type(0.1), bool(0.1), type(bool(0.1))) # True

# str() => 문자열 변환 시
print()
print(str(3), type(str(3))) # 3
print(str(3.5), type(str(3.5))) # 3.5
print(str(1.0e4), type(str(1.0e4))) # 10000.0
print(str(True), type(str(True))) # 문자열 True로 변환
print(str(False), type(str(False))) # 문자열 False로 변환


# int() => 정수 변환
print()
print(int(False), type(int(False))) # 0
print(int(True), type(int(True))) # 1
print(int(98.6), type(int(98.6))) # 98
print(int(1.0e4), type(int(1.0e4))) # 10000
print(int("1"), type(int("1"))) # 1
print(int("1.0e4"), type(int("1.0e4"))) # value 에러(소수점이나 지수를 포함하는 문자열은 변경 안됨)

# float() => 소수점으로 변환
print()
print(float(False), type(float(False))) # 0.0
print(float(True), type(float(True))) # 1.0
print(float(98), type(float(98))) # 98.0
print(float("98.6"), type(float("98.6"))) # 98.6


