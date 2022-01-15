import re

# search() : 문자열 전체를 검색해서 정규식과 매칭되는 패턴 리턴
# match() : 문자열 처음부터 정규식과 매칭되는 패턴을 찾아서 리턴
# sub() : 찾아서 바꾸기
# findall() : 정규표현식과 매칭되는 모든 문자열을 리스트 객체로 리턴
# split() : 찾은 정규표현식 패턴 문자열을 기준으로 분리

# pattern = re.compile("[a-z]+")
# print(pattern.match("Dave"))
# print(pattern.search("Dave"))

# print("찾아서 바꾸기")
# string = "DDA D1A DDA DA"
# # re.sub(패턴,바꿀문자열,원본문자열)
# result = re.sub("D.A", "Dave", string)
# print(result)


pattern = re.compile("[a-z]+")
print(pattern.findall("Game of Life in Python"))

pattern = re.compile("[a-zA-Z]+")
print(pattern.findall("Game of Life in Python"))

pattern = re.compile(":")
print(pattern.split("python:java:spring"))
