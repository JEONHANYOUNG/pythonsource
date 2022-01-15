# 정규표현식 - 자바스크립트 동일

import re

# /정규식/,
# compile() : 정규식을 저장해주는 메소드

pattern = re.compile("D.A")  # . : 모든 문자랑 매치

# result = pattern.search("D00A")
# print(result) # None


# 정규식과 일치 확인 - search(), sub(), match()
# result = pattern.search("DAA")
# print(result)  # <re.Match object; span=(0, 3), match='DAA'>
# print(result.start(), result.end(), result.group())

# result = re.search(r"D.A", "D1A")
# print(result.group())

result = pattern.search("d0A D1A 0111")
print(result)
print(result.group())
