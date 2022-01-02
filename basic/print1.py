# 한 줄 주석 -- ctrl + /을 입력하면 #이 나오면서 주석 처리가 됨, 아니면 #을 눌러도 주석 처리됨
'''
    여러 줄 주석을 입력할때 사용(홑따옴표 3개 입력 시)
'''
"""
    여러 줄 주석을 입력할때 사용(쌍따옴표 3개 입력 시)
"""

# 문자열 표현 시 홑따옴표, 쌍따옴표 허용
print('hello')           # hello
print("Hello Python!!")  # Hello Python!!
print(100)               # 100
print("100")             # 100  
print(25.3)              # 25.3
print("25.3")            # 25.3
print()

# type() : 변수 타입 알아보기
print(type(100))     # <class 'int'>
print(type("100"))   # <class 'str'>
print(type('100'))   # <class 'str'>
print(type('25.3'))  # <class 'str'>   
print(type(25.3))    # <class 'float'> 실수
print(type(True))    # <class 'bool'>  대문자로 입력




