# class Parent:
#     def __init__(self) -> None:
#         print("Parent 클래스의 __init__ 호출")
#         self.value = "테스트"

#     def test(self):
#         print("Parent 클래스의 test() 호출" + self.value)


# class Child(Parent):
#     def __init__(self) -> None:
#         Parent.__init__(self)  # 자바에서 super() 역할
#         print("Child 클래스의 __init__ 호출")


# child = Child()
# child.test()


# class Car:

#     speed = 0

#     def up_speed(self, value):
#         self.speed += value

#     def down_speed(self, value):
#         self.speed -= value


# class Sedan(Car):

#     seat_num = 0

#     def getSeatNum(self):
#         return self.seat_num


# class Truck(Car):
#     capacity = 0

#     def getCapacity(self):
#         return self.capacity


# class Santafe(Sedan):
#     pass


# sedan1, truck1 = Sedan(), Truck()
# santafe1 = Santafe()

# sedan1.up_speed(100)
# truck1.up_speed(80)
# santafe1.up_speed(120)

# sedan1.seat_num = 5
# truck1.capacity = 50
# santafe1.seat_num = 7

# print("승용차의 속도는 %dkm, 좌석수는 %d개" % (sedan1.speed, sedan1.getSeatNum()))
# print("산타페의 속도는 %dkm, 좌석수는 %d개" % (santafe1.speed, santafe1.getSeatNum()))
# print("트럭의 속도는 %dkm, 총 중량은 %d톤" % (truck1.speed, truck1.getCapacity()))


class AudioVisual:
    def __init__(self, power, volume) -> None:
        self.power = power
        self.volume = volume

    def switch(self, on_off):
        self.power = on_off

    def set_volume(self, volume):
        self.volume = volume


class Audio(AudioVisual):
    def __init__(self, power, volume) -> None:
        super().__init__(power, volume)

    def tune(self):
        str = "la la la...." if self.power else "turn it on"
        print(str)


class TV(AudioVisual):
    def __init__(self, power, volume, size) -> None:
        super().__init__(power, volume)
        self.size = size

    def watch(self):
        str = "have fun!!!" if self.power else "switch on"
        print(str)


tv1 = TV(False, 12, 40)
tv1.switch(True)
tv1.watch()

audio1 = Audio(True, 15)
audio1.set_volume(20)
audio1.tune()
