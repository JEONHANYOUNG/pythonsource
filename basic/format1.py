# %d : 숫자, %f : 실수, %s : 문자열, %c : 문자, %% : % 표현

print("%d" % 100)   # 100
print("%5d" % 100)  #   100 : 5자리를 잡아두고 있다가 표시를 해달라는 의미(앞의 두자리를 공백으로 잡고 뒤에 표시된 숫자 출력)
print("%05d" % 100) # 00100 : 5자리를 잡아두고 앞에 0을 표시를 해달라는 의미(앞의 두자리를 0으로 잡고 뒤에 표시된 숫자 출력)
print()
print("%5s" % "hi") #   hi (5자리를 잡고 hi를 입력)
print("%s" % "hi")  #hi 
print()
print("%-8.2f" % 123.21) #123.21 (-가 있으면 왼쪽 정렬 ,전체 8자리를 잡는데 소수점은 2자리까지)
print("%8.2f" % 12.21)    #   12.21 (+가 있으면 오른쪽 정렬 ,전체 8자리를 잡는데 소수점은 2자리까지)
print("%8.2f" % 12.2134567)  #  12.21 (+가 있으면 오른쪽 정렬 ,전체 8자리를 잡는데 소수점은 2자리까지)
print()
print("I eat %d apples" % 3)  #I eat 3 apples ()
print("I eat %s apples" % 3)  #I eat 3 apples (%s는 만능이고 어떤 타입이어도 알아서 넣어줌)
print("I eat %s apples" % "fives") #I eat fives apples ()
number = 4
print("I eat %d apples" % number) #I eat 4 apples ()
print("I eat", number, "apples") #I eat  4 apples ()
print()
# 여러 개가 대입되는 경우에 반드시 괄호 필요
print('%d : %s' % (1, "홍길동")) # 1 : 홍길동 
print("%d : %s - %f" % (2, "김성호",93.2)) # 2 : 김성호 - 93.200000
print()
# %s : 어떤 형태의 값이던 문자열로 변환해서 대입 가능
print("I eat %d apples" % 3)  
print("I eat %s apples" % 3.14)  
print("I eat %s apples" % "three")  
print("I eat %s apples" % True)  
print("I eat %s apples" % 't')  

# % 기호를 쓸려면
# print("Error is %d%" % 98) #ValueError: incomplete format
print("Error is %d%%" % 98) 





