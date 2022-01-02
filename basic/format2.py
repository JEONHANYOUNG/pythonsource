# format() 함수 - {} 사용

#첫번째 중괄호, 두번째 중괄호 순서 (You and Me)
print("{} and {}".format('You','Me')) 

#'You'가 첫번째 중괄호, 'Me'가 두번째 중괄호 순서 (You and Me)
print("{0} and {1}".format('You','Me')) 

#'You'가 첫번째 중괄호, 'Me'가 두번째 중괄호, 'You'가 세번째 중괄호 순서
print("{0} and {1} and {0}".format('You','Me')) 


#'You'에 var1이라고 주고, 'Me'에 var2에 이라고 주면 값이 나옴
print("{var1} and {var2}".format(var1='You',var2='Me')) 


# 결과값 => I ate 20 apples. so I was sick for 3 days
print("I ate {0} apples. so I was sick for {day} days".format(20,day=3))
print()

# Test1은 5자리를 사용하고 Price는 앞에 정수 4자리에 소수점 둘째자리까지 출력 
# Test1 :   776, price : 6534.12
print("Test1 : {0:5d}, price : {1:4.2f}".format(776,6534.123))

# Test1(a)에 a는 5자리를 사용하고 Price(b)에 b는앞에 정수 4자리에 소수점 둘째자리까지 출력 
# Test1 :   776, price : 6534.12
print("Test1 : {a:5d}, price : {b:4.2f}".format(a=776,b=6534.123))


