class Calculator:
    """ """

    def __init__(self) -> None:
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print("cal1 : {}".format(cal1.adder(10)))
print("cal2 : {}".format(cal2.adder(100)))
