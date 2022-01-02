# __init__ : account_no, name, balance 초기화
# withdraw() : 잔액 -= 넘어온 금액, 리턴은 잔액
# deposit() : 잔액 += 넘어온 금액, 리턴은 잔액
# __str__ : 계좌번호, 이름, 잔액 출력


class Account:
    def __init__(self, account_no, name, balance) -> None:
        self.account_no = account_no

    pass
