# 문자열 관련 함수

# 1. count() : 문자열에 포함된 특정 문자의 개수
a = "hobby"
print("a안에 포함된 b 문자 개수", a.count("b"))


# 2. find(찾을 문자)
# 2. find(찾을 문자,시작위치)
a = "Python is best choice"
print("b가 시작되는 위치 ", a.find("b"))
print("b가 시작되는 위치 ", a.find("b", 12))

print("k가 시작되는 위치 ", a.find("k"))  # 없는 것은 -1이 나옴

# 3. index() : find와 다르게 없는 문자열이라면 Exception 발생(에러)
print("b가 시작되는 위치 ", a.index("b"))
print("k가 시작되는 위치 ", a.index("k"))  # ValueError: substring not found


# 4. startswith() / endswith() : 특정 문자열로 시작하고 끝나는지 확인
a = "Python is best choice"
print(a.startswith("P"))  # True
print(a.endswith("P"))  # False


# 5. join()
a = ","
print("문자열 삽입", a.join("abcd"))  # 문자열 삽입 a,b,c,d
print("a", "b", "c", "d", sep=",")


# 6. upper(대문자로 변경) / lower(소문자로 변경) / swapcase(대문자 <-> 소문자)
a = "abcdef"
print(a.upper())  # ABCDEF

b = "ABCDEF"
print(b.lower())  # abcdef

c = "Python is Easy"
print(c.swapcase())  # pYTHON IS eASY


# 7. strip(모든 공백) / lstrip(왼쪽 공백 제거) / rstrip(오른쪽 공백 제거)
a = "      h1"
print(a.strip(), a.lstrip())  # h1 h1

b = "    h1    "
print(b.strip())  # h1
print("       hi" == "h1")  # False (공백이 있는 상태에서 비교하면 false가 출력됨)


# 8. replace() - 문자열 변경
a = "Life is too short"
print(a.replace("Life", "Your leg"))  # Your leg is too short


# 9. split() - 문자열 나누기
a = "Life is too short"
print(a.split())  # ['Life', 'is', 'too', 'short']

b = "a:b:c:d"
print(b.split(":"))  # ['a', 'b', 'c', 'd']

c = "하나\n둘\n셋"
print(c.split("\n"))  # ['하나', '둘', '셋']


# 10. 문자열 구성 파악 - 숫자, 영문자, 숫자랑 영문자로 구성되어 있는가?
print("1234".isdigit())  # True
print("abcd".isalpha())  # True
print("abc123".isalnum())  # True
print("ABCD".isupper())  # True
print("    ".isspace())  # True


# 문제

# 대문자는 소문자로, 소문자는 대문자로 출력
name = "KennRY"
print(name.swapcase())  # kENNry


# 년/월/일 형태로 입력받고 10년 후의 날짜를 구한 후 출력
# 2021/12/22 => 2031년 12월 22일
date = input("날짜(년/월/일) 형태로 입력 ")
pos = date.find("/")
year = int(date[0:pos]) + 10

print("입력한 날짜의 10년 후 : %s" % (str(year) + "년 " + date[5:7] + "월 " + date[8:] + "일"))


date = date.split("/")  # ['2021','12','21']
print(
    "입력한 날짜의 10년 후 : %s"
    % (str(int(date[0]) + 10) + "년 " + date[1] + "월 " + date[2] + "일")
)

# 사이트 별로 비밀번호를 만들어 주는 프로그램 작성
# 예) http://naver.com 이라면
# 규칙 1 : http:// 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
# 결과 : 생성된 비밀번호는 nav51!
url = "http://naver.com"
url = url.replace("http://", "")  # 규칙 1 적용
url = url[: url.find(".")]  # 규칙 2 적용
e_cnt = url.count("e")
password = url[:3] + str(len(url)) + str(e_cnt) + "!"  # 규칙 3 적용
print("생성된 비밀번호는 ", password)
