import re

# 반복 : *, +, ?, {2}, {1,20}

print("---  *  사용법 : 최소 0 ~ 무한대 ----")
pattern = re.compile("D*A")  # D가 0~무한대이고, 그다음에 A
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.search("DDDDDDDDDDDA"))

print()
print("---  +  사용법 : 최소 1 ~ 무한대 ----")
pattern = re.compile("D+A")  # D가 1~무한대이고, 그다음에 A
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.search("DDDDDDDDDDDA"))


print()
print("---  ?  사용법 : 최소 0 ~ 1 ----")
pattern = re.compile("D?A")  # D가 0~1, 그다음에 A
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.search("DDDDDDDDDDDA"))


print()
print("---  {n}  사용법  ----")
pattern = re.compile("AD{2}A")  # D가 2, 그다음에 A
print(pattern.search("ADA"))
print(pattern.search("ADDA"))
print(pattern.search("ADDDDDDDDDDDA"))

print()
print("---  {n,m}  사용법  ----")
pattern = re.compile("AD{2,6}A")  # D가 최소 2 ~ 최대 6, 그다음에 A
print(pattern.search("ADA"))
print(pattern.search("ADDA"))
print(pattern.search("ADDDDDDA"))
