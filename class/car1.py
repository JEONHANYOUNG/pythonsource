# class Car:
#     color = ""
#     speed = 0

#     def up_speed(self, value):
#         self.speed += value

#     def down_speed(self, value):
#         self.speed -= value


# my_car1 = Car()
# my_car1.color = "RED"
# my_car1.up_speed(10)
# print("첫번째 자동차 색상 : {}, 속도 : {}".format(my_car1.color, my_car1.speed))


# my_car2 = Car()
# my_car2.color = "BLUE"
# my_car2.up_speed(30)
# print("두번째 자동차 색상 : {}, 속도 : {}".format(my_car2.color, my_car2.speed))


# my_car3 = Car()
# my_car3.speed = 80
# my_car3.color = "BLACK"
# my_car3.up_speed(30)
# my_car3.down_speed(10)
# print("세번째 자동차 색상 : {}, 속도 : {}".format(my_car3.color, my_car3.speed))


# class Car:
#     def __init__(self, color, speed) -> None:
#         self.speed = speed
#         self.color = color

#     def up_speed(self, value):
#         self.speed += value

#     def down_speed(self, value):
#         self.speed -= value


# my_car1 = Car("Red", 10)
# my_car2 = Car("Blue", 30)
# my_car3 = Car("Black", 100)


# 클래스 변수


class Car:

    count = 0

    def __init__(self, color, speed, count) -> None:
        self.speed = speed
        self.color = color
        Car.count += count

    def up_speed(self, value):
        self.speed += value

    def down_speed(self, value):
        self.speed -= value

    def __del__(self):
        Car.count -= 1


my_car1 = Car("Red", 10, 1)
my_car2 = Car("Blue", 30, 1)
my_car3 = Car("Black", 100, 1)

print(Car.count)

# 차 객체 삭제
del my_car1
print(Car.count)
