print()    # 엔터 , 끝에 세미콜론 안찍는다.
print('T','E','S','T')  # T E S T => 따옴표 안에 문자를 넣게 되면 개별 문자로 출력이 됨

# sep (separator 옵션 : 문자들 사이에 연결 문자열 지정) 
print('T','E','S','T',sep='')  # TEST  , 공백 제거
print('T','E','S','T',sep='-')  # T-E-S-T  , '-'을 이용해 문자를 연결해주는 역할을 함
print('2021','12','20',sep='-')  # 2021-12-20  , '-'을 이용해 문자를 연결해주는 역할을 함

# end (출력문 끝에서 처리 방법, 한칸만 띄우고 문장을 이어주는 역할) 
print('Welcome To', end=' ') # Welcome To the black prade
print('the black prade')



