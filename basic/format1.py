# %d : 숫자, %f : 실수, %s : 문자열, %c : 문자, %% : % 표현

print("%d" % 100)  # 100
print("%5d" % 100)  #   100
print("%05d" % 100)  # 00100
print()
print("%5s" % "hi")  #    hi
print("%s" % "hi")  # hi
print()
print("%-8.2f" % 123.21)  # 123.21
print("%8.2f" % 12.21)  #    12.21
print("%8.2f" % 12.2134567)  #    12.21
print()
print("I eat %d apples" % 3)
print("I eat %s apples" % 3)
print("I eat %s apples" % "five")
number = 4
print("I eat %d apples" % number)
print("I eat ", number, "apples")
print()
# 여러 개가 대입되는 경우에 반드시 괄호 필요
print("%d : %s" % (1, "홍길동"))
print("%d : %s - %f" % (2, "김성호", 93.2))
print()
# %s : 어떤 형태의 값이던 문자열로 변환해서 대입 가능
print("I eat %s apples" % 3)
print("I eat %s apples" % 3.14)
print("I eat %s apples" % "three")
print("I eat %s apples" % True)
print("I eat %s apples" % "t")

# % 기호를 쓸려면
# print("Error is %d%" % 98)  # ValueError: incomplete format
print("Error is %d%%" % 98)
