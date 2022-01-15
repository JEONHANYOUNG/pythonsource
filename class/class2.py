# 클래스 작성
# __init__(self) : 생성자, 멤버변수 초기화, 필수요소는 아님
# def 메소드(self) : 멤버 메소드
# def __str__(self) : toString()과 같은 개념
# def __del__(self) : 객체 삭제시 count 적용
# 클래스이름.변수명 : static 변수로 선언한 것과 같은 개념
# 클래스이름.메소드명 : static 메소드로 선언한 것과 같은 개념
# 생성자 오버로딩 없음 : 기본값을 이용해 대체


# class SelfTest:
#     def function1():
#         print("function1 called")

#     # @classmethod
#     def function3(a, b):
#         print("function1 called", a + b)


#     def function2(self):
#         print("function2 called")


# self1 = SelfTest()
# # self1.function1()  # TypeError: SelfTest.function1() takes 0 positional arguments
# SelfTest.function1()
# SelfTest.function3(10, 5)
# self1.function2()


class UserInfo:
    """
    UserInfo class
    작성자 : Hong
    작성날짜 : 2021.12.29
    설명 : 클래스 작성법
    """

    def __init__(self, name, age, email=None) -> None:
        self.name = name
        self.age = age
        self.email = email

    def user_info(self):
        return "name : {}, age : {}, email : {}".format(self.name, self.age, self.email)


user1 = UserInfo("홍길동", 25, "hong25@naver.com")
user2 = UserInfo("김길동", 35)


print(user1.user_info())
print(user2.user_info())
