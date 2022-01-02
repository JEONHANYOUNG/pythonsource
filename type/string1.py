# 문자열 자료형
# '',"",""" """,''' '''
str1 = "Hello World"
str2 = "Hello World"

#  여러 줄인 문자열을 변수에 대입하고 싶을 때
str3 = "Life is too short\nYou need Python"


# str3 = """Hello World"""  # ''' '''
str4 = """
    Hello World                    
    Life is too short
    You need Python
"""

print(str4)
# Hello World
# Life is too short
# You need Python


str5 = "Hello's"

print()

# 문자열 응용
# + : 결합
print("Python" + " is fun")  # Python is fun

# * : 복제
print("Python" * 2)  # PythonPython

print("*" * 50)
print("My Program")
print("*" * 50)

print()

# 문자열 인덱싱과 슬라이싱
# 0부터 시작, 뒤에서 인덱싱 -1

str1 = "Life is too short"
print(str1[3])  # 인덱싱  e
print(str1[-1])  # t
print(str1[-5])  # s

# 슬라이싱(0 부터 시작하면 뒤의 숫자는 포함하지 않음, 앞에 것을 쓰고 뒤에 것을 안쓰면 뒤까지 나오는 것)
print(str1[0:4])  # Life => 0번째 자리부터 3번째 자리까지
print(str1[4:9])  #  is t => 4번째 자리부터 8번째 자리까지
print(str1[9:])  # oo short => 10번째 자리부터 끝까지
print(str1[:17])  # Life is too short
print(str1[0:-4])  # Life is too s

str2 = "20190701Sunny"
# 문자열을 두 부분으로 나누어 출력하기(날짜, 날씨)
date = str2[0:8]  # 0번째 자리부터 7번째 자리까지
weather = str2[8:]  # 8번째 자리부터 끝까지
print(date, ",", weather)  # 20190701 , Sunny
print()

# 날짜를 2019-07-01 출력하기
year = date[0:4]
month = date[4:6]
day = date[6:]
print(year, month, day, sep="-")  # 2019-07-01
print()

# 주민등록번호에서 성별 확인하기
# 남자 1, 3   여자 2, 4
str1 = "901205-3234567"  # 남자

no = str1[7]
if no == "1" or no == "3":
    print("남자")
elif no == "2" or no == "4":
    print("여자")

# if int(str1[7]) % 2 == 1:
#     print("남자")
# else:
#     print("여자")

str1 = "대한민국"
for s in str1:
    print(s)


# 문자열 길이
print("문자열 길이 : ", len(str1))  # 문자열 길이 :  4
