# 학생 3명이 있다
# 학생정보(이름,학년,반,성별,점수1,점수2)

# 변수 처리

# 학생1
student_name1 = "Kim"
student_number1 = 1
student_grade1 = 1
student_detail1 = [{"gender": "male"}, {"score1": 95}, {"score2": 88}]

# 학생2
student_name2 = "Park"
student_number2 = 2
student_grade2 = 2
student_detail2 = [{"gender": "female"}, {"score1": 75}, {"score2": 68}]

# 학생3
student_name3 = "Choi"
student_number3 = 3
student_grade3 = 3
student_detail3 = [{"gender": "male"}, {"score1": 68}, {"score2": 89}]


# 학생 정보 출력
# print(
#     "이름 : %s, 학번 : %d, 학년 : %d, 학생정보 : %s"
#     % (student_name1, student_number1, student_grade1, student_detail1)
# )
# print(
#     "이름 : %s, 학번 : %d, 학년 : %d, 학생정보 : %s"
#     % (student_name2, student_number2, student_grade2, student_detail2)
# )
# print(
#     "이름 : %s, 학번 : %d, 학년 : %d, 학생정보 : %s"
#     % (student_name3, student_number3, student_grade3, student_detail3)
# )


# 리스트

student_names_list = ["Kim", "Park", "Choi"]
student_numbers_list = [1, 2, 3]
student_grades_list = [1, 2, 3]
student_details_list = [
    {"gender": "male", "score1": 95, "score2": 88},
    {"gender": "female", "score1": 75, "score2": 68},
    {"gender": "male", "score1": 68, "score2": 89},
]

# 학생 삭제
student_names_list[1]
student_numbers_list[1]
student_grades_list[1]
student_details_list[1]


# print(student_names_list)
# print(student_numbers_list)
# print(student_grades_list)
# print(student_details_list)


# 딕셔너리

students_dicts = [
    {
        "student_name": "Kim",
        "student_number": 1,
        "student_grade": 1,
        "student_detail": {"gender": "male", "score1": 95, "score2": 88},
    },
    {
        "student_name": "Park",
        "student_number": 2,
        "student_grade": 2,
        "student_detail": {"gender": "female", "score1": 75, "score2": 68},
    },
    {
        "student_name": "Choi",
        "student_number": 3,
        "student_grade": 3,
        "student_detail": {"gender": "male", "score1": 68, "score2": 89},
    },
]


# 클래스

# class 클래스이름(상속클래스명):
#     클래스 변수1
#     클래스 변수2

#     def __init__(self,변수명):   생성자
#         self.name = 변수명

#     def 클래스함수():
#         수행할 문장

#     def 클래스함수():
#         수행할 문장


class Student:
    # 생성자
    def __init__(self, name, number, grade, detail):
        self.name = name
        self.number = number
        self.grade = grade
        self.detail = detail

    # toString() 역할
    def __str__(self) -> str:
        return "이름 : {}, 학번 : {}, 학년 : {}, 학생정보 : {}".format(
            self.name, self.number, self.grade, self.detail
        )


# 객체 생성
student1 = Student("Kim", 1, 1, {"gender": "male", "score1": 95, "score2": 88})
student2 = Student("Park", 2, 2, {"gender": "female", "score1": 75, "score2": 68})
student3 = Student("Choi", 3, 3, {"gender": "male", "score1": 68, "score2": 89})

# __dict__ : 클래스의 값들 딕셔너리 형태로 리턴
print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)

# __str__ 전 : <__main__.Student object at 0x00000234C5D57FD0>

# __str__ 후
# 이름 : Kim, 학번 : 1, 학년 : 1, 학생정보 : {'gender': 'male', 'score1':
# 95, 'score2': 88}
print(student1)


# 객체를 리스트에 담기
student_list = []
student_list.append(student1)
student_list.append(student2)
student_list.append(student3)

for student in student_list:
    print(student)
