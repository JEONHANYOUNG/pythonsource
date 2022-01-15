# __init__ : account_no, name, balance 초기화
# withdraw() : 잔액 -= 넘어온 금액, 리턴은 잔액
# deposit() : 잔액 += 넘어온 금액, 리턴은 잔액
# __str__ : 계좌번호,이름,잔액 출력


class Account:
    def __init__(self, account_no, name, balance) -> None:
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def __str__(self) -> str:
        return "계좌번호 : {}, 이름 : {}, 잔액:{}".format(
            self.account_no, self.name, self.balance
        )


user1 = Account("111-22-333", "홍길동", 100000)
user1.withdraw(50000)
user1.deposit(200000)

print(user1)
