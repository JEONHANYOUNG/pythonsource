# 클래스 작성
# __init__(self) : 생성자, 멤버변수 초기화, 필수 요소는 아님
# def 메소드(self) : 멤버 메소드
# def __str__(self) : toString()과 같은 개념
# def __del__(self) : 객체 삭제 시 count 적용
# 클래스이름.변수명 : static 변수로 선언한 것과 같은 개념
# 클래스이름.메소드명 : static 메소드로 선언한 것과 같은 개념
# 생성자 오버로딩 없음 : 기본값을 이용해 대체


class SelfTest:
    def function1(self):
        print("function1 called")

    # @classmethod
    def function3(self):
        print("function1 called", a + b)

    def function3(self):
        print("function2 called")


self1 = SelfTest()
