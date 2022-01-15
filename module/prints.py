# 함수 정의
def prt1():
    print("Hello!! Everyone!!")


def prt2():
    print("안녕하세요 여러분!!")


# print("모듈의 __name__ 출력하기")
# print(__name__)   # __main__
# print()


# prints를 사용하는 파일을 작성하지 않고 테스트하기
if __name__ == "__main__":
    prt1()
    prt2()
