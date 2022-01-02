# 변수 선언 : 어떤 데이터를 담을 것인지에 따라서 타입이 결정
str1= "Life is too short, You need Python"
str2= 'Life is too short, You need Python'
iVar = 34
fVar = 3.14
bVar = False

# 두 개의 변수에 동일한 값 대입
a = b = 3  
print(a,b) # 3 3

# 두 개의 변수에 다른 값 대입
# a = 4
# b = 5
a, b = 4, 5

# 두 개의 변수에 들어 있는 값 서로 바꿔서 출력
# 자바 언어
# temp = a
# a = b
# b = temp

# 파이썬 언어
a, b = b, a  
print(a, b) # 5 4

bVar = 500
print(bVar) # 500


