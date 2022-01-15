# __init__ : power, volume 초기화
# switch(): on_off 전달인자를 받아서 power 변경
# set_volume() : volume 전달인자를 받아서 volume 변경


class Audio:
    def __init__(self, power, volume) -> None:
        self.power = power
        self.volume = volume

    def switch(self, on_off):
        self.power = on_off

    def set_volume(self, volume):
        self.volume = volume

    def tune(self):
        str = "la la la...." if self.power else "turn it on"
        print(str)


mp3 = Audio(False, 8)
mp3.set_volume(12)
mp3.tune()
mp3.switch(True)
mp3.tune()
