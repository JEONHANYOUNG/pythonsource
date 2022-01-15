# 오버라이딩
# class Parent:
#     def func1(self):
#         print("Parent의 func1() 실행")

#     def func2(self):
#         print("Parent의 func2() 실행")


# class Child(Parent):
#     def func1(self):
#         print("Child의 func1() 실행")

#     def func3(self):
#         print("Child의 func3() 실행")


# parent, child = Parent(), Child()
# parent.func1()
# child.func1()  # Child의 func1() 실행
# child.func2()
# child.func3()


class Car:

    speed = 0

    def up_speed(self, value):
        self.speed += value
        print("현재 속도(슈퍼클래스) : %d" % self.speed)

    def down_speed(self, value):
        self.speed -= value


class Sedan(Car):

    seat_num = 0

    def up_speed(self, value):
        self.speed += value

        if self.speed > 150:
            self.speed = 150
            print("현재 속도(자식클래스) : %d" % self.speed)

    def getSeatNum(self):
        return self.seat_num


sedan = Sedan()

sedan.up_speed(100)
sedan.seat_num = 5
sedan.up_speed(300)
