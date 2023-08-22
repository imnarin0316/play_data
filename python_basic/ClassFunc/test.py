import json

students_data = []
file_name = './python_basic/ClassFunc/student.json'
with open(file_name, 'r', encoding="utf=8") as file:
    students_data = json.load(file)

class SetDataStudent:
    studentNames = []
    studentAges = []
    studentAddress = []
    studentGrade = []  

    
class AboutStudent(SetDataStudent) :
    
    def __init__(self):
        super().__init__()  #부모클래스 초기화 호출
    
        
    def get_info(self, name):
        if name in SetDataStudent.studentNames:
            index = SetDataStudent.studentNames.index(name)
            return print(f"이름: {SetDataStudent.studentNames[index]}, 나이: {SetDataStudent.studentAges[index]}, 주소: {SetDataStudent.studentAddress[index]}, 성적: {SetDataStudent.studentGrade[index]}")
        else :
            return print(f"{name}은 존재하지 않습니다.")
    
    
        
s = AboutStudent()

# students_data 루프를 통해 초기 데이터 설정
for student in students_data:
    SetDataStudent.studentNames.append(student["name"])
    SetDataStudent.studentAges.append(student["age"])
    SetDataStudent.studentAddress.append(student["address"])
    SetDataStudent.studentGrade.append(student["grade"])
    
idx = s.get_info(input('이름'))

# 데이터 저장
# SetDataStudent.save_data(file_name, 3)
# print("데이터가 저장되었습니다.")

