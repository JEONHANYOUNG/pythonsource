# exception 강제 발생 - raise

# try:
#     a = "333"
#     if a == "Kim":
#         print("허가!!")
#     else:
#         raise ValueError  # 강제 발생하려면 사용

# except ValueError:
#     print("value error")
# except Exception as e:
#     print(e)
# else:
#     print("OK")


number = int(input("정수 입력 "))
if number > 0:
    raise NotImplementedError
else:
    raise NotImplementedError
