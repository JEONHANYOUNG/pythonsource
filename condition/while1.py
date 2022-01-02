# 1~10 출력

i = 1
while i<11:
    print(i,end=" ") # 1 2 3 4 5 6 7 8 9 10
    i = i+1

print()

# 1 ~ 100 짝수만 출력
i = 0 
while i < 101:
    print(i, end=" ")
    i+=2

print()

# 1 ~ 100 합계
num1, sum1 = 1, 0 

while num1 < 101:
    sum1 += num1
    num1 += 1

print("1 ~ 100 합 : ",sum1)  # 1 ~ 100 합 :  5050
