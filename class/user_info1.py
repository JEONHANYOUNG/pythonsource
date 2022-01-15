# class UserInfo:
#     """
#     UserInfo class
#     작성자 : Hong
#     작성날짜 : 2021.12.29
#     설명 : 클래스 작성법
#     """

#     # 클래스 함수(== 인스턴스 메소드)
#     def user_info(self):
#         print("메소드 실행")


# class UserInfo:
#     """
#     UserInfo class
#     작성자 : Hong
#     작성날짜 : 2021.12.29
#     설명 : 클래스 작성법
#     """

#     def __init__(self) -> None:
#         self.name = "홍길동"
#         self.age = 25

#     # 클래스 함수(== 인스턴스 메소드)
#     def user_info(self):
#         return "name : {}, age : {}".format(self.name, self.age)


# user1 = UserInfo()

# print(user1.user_info())


class UserInfo:
    """
    UserInfo class
    작성자 : Hong
    작성날짜 : 2021.12.29
    설명 : 클래스 작성법
    """

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    # 클래스 함수(== 인스턴스 메소드)
    def user_info(self):
        return "name : {}, age : {}".format(self.name, self.age)


user1 = UserInfo("김중원", 30)
print(user1.user_info())

user2 = UserInfo("최중원", 40)
print(user2.user_info())
