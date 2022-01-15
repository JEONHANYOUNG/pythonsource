# exception
# 컴파일 예외 => 신경쓰지 않음(IDE 사용하면 알아서 처리)
#             => 문법 에러(SyntaxError)

# 런타임 예외
# print(10 / 0)  # ZeroDivisionError: division by zero

# x = [10, 20, 30]
# print(x[0])
# print(x[4])  # IndexError: list index out of range
# print(x.index(0))  # ValueError: 0 is not in list


# dict1 = {"name": "Kim", "age": 33, "city": "seoul"}
# # print(dict1["hobby"]) # KeyError: 'hobby'
# print(dict1.get("hobby")) # None

# import time

# print(time.time())  # 1640829372.5631604
# print(time.month()) # AttributeError: module 'time' has no attribute 'month'

# f = open("./python.txt", "r")  # FileNotFoundError
# f.close()


# 예외처리
# try ~ except:
# try ~ except ~ finally :
# try ~ finally:
# try ~ except ~ else:
# try ~ except ~ else ~ finally:


# try~except: try: 오류가 발생할 수 있는 코드 작성, except : 예외시 처리할 코드
name = ["Kim", "Park", "Lee"]

# try:
#     z = "Let"
#     x = name.index(z)
#     print("{}을 {}번째 에서 찾았음".format(z, x + 1))
# except:
#     print("해당 요소를 찾지 못했음")


# try ~ except 오류코드명
# try:
#     z = "Let"
#     x = name.index(z)
#     print("{}을 {}번째 에서 찾았음".format(z, x + 1))
# except ValueError:
#     print("해당 요소를 찾지 못했음")


# try:
#     dict1 = {"name": "Kim", "age": 33, "city": "seoul"}
#     print(dict1["age"])
#     print(dict1["hobby"])  # KeyError: 'hobby'
# except Exception:
#     print("찾으려는 키 값이 없음")
# else:
#     print("OK!!")


# try:
#     dict1 = {"name": "Kim", "age": 33, "city": "seoul"}
#     print(dict1["age"])
#     print(dict1["hobby"])  # KeyError: 'hobby'
# except KeyError:
#     print("찾으려는 키 값이 없음")

# try ~ except ~ else : else : 예외발생 처리를 했으나 예외가 발생하지 않은 경우
# try:
#     dict1 = {"name": "Kim", "age": 33, "city": "seoul"}
#     print(dict1["age"])
#     # print(dict1["hobby"])  # KeyError: 'hobby'
# except KeyError:
#     print("찾으려는 키 값이 없음")
# else:
#     print("OK!!")


# try~except~else~finally
# finally : 오류가 발생하던지 안하던지 무조건 실행
# try:
#     dict1 = {"name": "Kim", "age": 33, "city": "seoul"}
#     print(dict1["age"])
#     # print(dict1["hobby"])  # KeyError: 'hobby'
# except Exception:
#     print("찾으려는 키 값이 없음")
# else:
#     print("OK!!")
# finally:
#     print("finally")


# try:
#     print("Try")
# finally:
#     print("finally")


# name = ["Kim", "Park", "Lee"]

# try:
#     z = "Let"
#     x = name.index(z)
#     print("{}을 {}번째 에서 찾았음".format(z, x + 1))
# except ValueError:
#     print("해당 요소를 찾지 못했음")
# except IndexError:
#     print("index error")
# except Exception:
#     print("exception")
# else:
#     print("else")
# finally:
#     print("finally")

# try~except~else

# try:
#     number_input = int(input("정수 입력 "))  # ValueError
# except ValueError as V:
#     print("입력값을 확인해 주세요")
#     print(V) # 에러 메세지를 언어 자체가 제공하는 버전으로 보여주기
# else:
#     print("원의 반지름 : ", number_input)
#     print("원 둘레 : ", 2 * 3.14 * number_input)
#     print("원 넓이 : ", 3.14 * number_input * number_input)
