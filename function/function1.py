# 함수 : 반복적으로 사용되는 부분에 대해서 작성

# 전달인자도 없고 리턴값도 없는 경우
# def hello():
#     print("Hello")


# hello()


# 전달인자는 없고 리턴값은 있는 경우
# def hello():
#     return "Hello"


# say = hello()
# print(say, "Hong!!!")


# 전달인자와 리턴값 모두 있는 경우
# def add(a, b):
#     return a + b


# print("3+5 = ", add(3, 5))


# 전달인자는 있고 리턴값 없는 경우
# def add(a, b):
#     print("%d + %d = %d" % (a, b, (a + b)))


# add(15, 16)

# 기본 파라메터 : 함수 호출 시 변수에 해당하는 값이 넘어오면 넘어오는 값
# 대입하고, 넘어오지 않는 경우 기본값으로 처리

# def print_n_times(value, n=2):
#     for i in range(n):
#         print(value)


# print_n_times("안녕하세요")  # 2번 반복
# print_n_times("안녕하세요", 4)  # 4번 반복


# 가변 파라메터 : 입력값들을 전부 모아서 튜플로 만들어 줌
# 변수명은 상관없음(args 주로 사용)
# def add_many(*args):
#     print(args)


# add_many()
# add_many({"dessert": "macaroon", "wine": "merlot"})
# add_many("35", "24", "15", "14")
# add_many("A", "B", "C", "D", "E")
# add_many(["A", "B", "C", "D", "E"])


# def add_many2(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result


# print("result", add_many2(15, 63, 869, 45, 36, 9, 3))
# print("result", add_many2(27, 35, 56))
# print("result", add_many2())


# def sum_mul(choice, *args):
#     if choice == "mul":
#         result = 1
#         for i in args:
#             result *= i
#     elif choice == "add":
#         result = 0
#         for i in args:
#             result += i
#     return result


# print("덧셈", sum_mul("add", 1, 2, 3, 4, 5))
# print("곱셈", sum_mul("mul", 1, 2, 3, 4, 5))

# **kwargs : 가변 파라메터를 딕셔너리 형태로 처리


# def args_func1(**kwargs):
#     print("kwargs", kwargs)


# args_func1(name="Kim")
# args_func1(name="Kim", name2="Park", active="Test")
# args_func1(name="Kim", age=10, title="Title")
# args_func1(name="Kim", name2="Tark")


# def example_mul(arg1, arg2, *args, **kwargs):
#     print(arg1, arg2, args, kwargs)


# example_mul(10, 20)
# example_mul(20, 30, "park", "kim")
# example_mul(20, 50, "park", "kim", age=25, name="kim")
