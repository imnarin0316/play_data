import json

# 전역변수
students_data = []
get_student = []

# 데이터 종류 대로 모아둔 전역변수(key)
studentNames = []
studentAges = []
studentAddress = []
studentGrade = []
studentimg = []

class StudentData:
    
    def __init__(self):
        print("파일 읽기")

    # 데이터 파일 읽기 
    def info_data(self, sdata):
        global students_data
        # , studentNames, studentAges, studentAddress, studentGrade,studentimg

        with open(sdata, 'rt', encoding="utf-8") as sd:
            students_data = json.load(sd)

        # for student in students_data:
        #     studentNames.append(student["name"])
        #     studentAges.append(student["age"])
        #     studentAddress.append(student["address"])
        #     studentGrade.append(student["grade"])
        #     studentimg.append(student["img"])

    
class ShowData:
    global get_student

    def __init__(self):
        print("선택한 학생의 정보 조회 : ")
        get_student = []

    def get_info(self, idx):
        get_student = students_data[idx]
        print(get_student)
        # print(studentNames[idx],studentAges[idx],studentAddress[idx],studentGrade[idx],studentimg[idx])

    def update(self, sdata) : 
         with open(sdata, 'w', encoding="utf-8") as file:
            now_student = json.dumps(students_data,indent=4)
            file.write(now_student)

students = StudentData()
students.info_data("./python_basic/ClassFunc/student.json")

show_student = ShowData()
show_student.get_info(3)

# ddd = students_data[3]["grade"] = [90, 80, 60]
# print(ddd)