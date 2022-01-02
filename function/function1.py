# 함수 : 반복적으로 사용되는 부분에 대해서 작성

# 전달인자도 없고 리턴값도 없는 경우
def hello():
    print("Hello")  # Hello


# hello()


# 전달인자도 없고 리턴값은 있는 경우
def hello():
    return "Hello"


say = hello()
print(say, "Hong!!!")  # Hello Hong!!!


# 전달인자와 리턴값 모두 있는 경우
def add(a, b):
    return a + b


print("3+5 = ", add(3, 5))  # 3+5 =  8


# 전달인자는 있고 리턴값 없는 경우
def add(a, b):
    print("%d + %d = %d" % (a, b, (a + b)))  # 15 + 16 = 31


add(15, 16)

# 기본 파라메터 : 함수 호출 시 변수에 해당하는 값이 넘어오면 넘어오는 값
# 대입하고, 넘어오지 않는 경우 기본값으로 처리
def print_n_times(value, n=2):  # 값이 안넘어오면 2로 넘겨라 라는 의미
    for i in range(n):
        print(value)  # 안녕하세요


print_n_times("안녕하세요")  # 안녕하세요 2번 반복
print_n_times("안녕하세요", 4)  # 안녕하세요 4번 반복


# 가변 파라메터(파라메터로 넘길 때 몇개로 넘기는 지 모를때) : 입력값들을 전부 모아서 튜플로 만들어 줌
# 변수명은 상관없음(args 주로 사용)
def add_many(*args):  # 값이 안넘어오면 2로 넘겨라 라는 의미
    print(args)  # 안녕하세요


add_many()  # ()
add_many(
    {"dessert": "macaroon", "wine": "merlot"}
)  # ({'dessert': 'macaroon', 'wine': 'merlot'},)
add_many("32", "24", "15", "14")  # ('32', '24', '15', '14')
add_many("A", "B", "C", "D")  # ('A', 'B', 'C', 'D')
add_many(["A", "B", "C", "D"])  # (['A', 'B', 'C', 'D'],)


def add_many2(*args):
    result = 0
    for i in args:
        result += i
    return result


print("result", add_many2(15, 63, 869, 45, 36, 9, 3))  # result 1040
print("result", add_many2(27, 35, 56))  # result 118
print("result", add_many2())  # result 0


def sum_mul(choice, *args):
    if choice == "mul":
        result = 1
        for i in args:
            result *= i
    elif choice == "add":
        result = 0
        for i in args:
            result += i
    return result


print("덧셈", sum_mul("add", 1, 2, 3, 4, 5))  # 덧셈 15
print("곱셈", sum_mul("mul", 1, 2, 3, 4, 5))  # 곱셈 120


# **kwargs : 가변 파라메터를 딕셔너리 형태로 처리


def args_func1(**kwargs):
    print("kwargs", kwargs)


args_func1(name="Kim")  # kwargs {'name': 'Kim'}
# kwargs {'name': 'Kim', 'name2': 'Park', 'active': 'Test'}
args_func1(name="Kim", name2="Park", active="Test")
# kwargs {'name': 'Kim', 'age': 10, 'title': 'Title'}
args_func1(name="Kim", age=10, title="Title")
args_func1(name="Kim", name2="Tark")  # kwargs {'name': 'Kim', 'name2': 'Tark'}


def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_mul(10, 20)  # 10 20 () {}
example_mul(20, 30, "park", "kim")  # 20 30 ('park', 'kim') {}
example_mul(
    20, 30, "park", "kim", age=25, name="kim"
)  # 20 30 ('park', 'kim') {'age': 25, 'name': 'kim'}
