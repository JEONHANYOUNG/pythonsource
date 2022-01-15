import re

# [], -, ^

print("--- [] : 괄호안에 문자 찾기----")
pattern = re.compile("[abcdefgABCDEFG]")
print(pattern.search("a1234"))
print(pattern.search("z1234"))
print(pattern.search("ABC1234"))

print()
print("--- [-] : 범위 지정하고 문자 찾기----")
pattern = re.compile("[a-gA-G]")  # [a-zA-Z0-9]
print(pattern.search("a1234"))
print(pattern.search("z1234"))
print(pattern.search("ABC1234"))

print()
print("--- [^] : 제외 ----")
pattern = re.compile("[^a-zA-Z0-9]")
print(pattern.search("abcdef"))
print(pattern.search("#$%*&^"))

print()
pattern = re.compile("[가-힣]")
print(pattern.search("abdcdefgdf가나다라"))
