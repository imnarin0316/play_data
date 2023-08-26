# 데이터들을 용도대로 모아두고 zip 함수로 조회하기
#  with block 으로 데이터 불러오기
# 변경된 값을 'w'으로 수정하기
import pandas as pd

students = []
names = []
ages = []
addresses = []
g1 = []
g2 = []
g3 = []
imgs = []

class StudentInfo:
    
    def __init__(self):
        print("정보조회 시작")
    
    def get_info(self, file_name):
        global students, names, ages, addresses, g1, g2, g3, imgs
        
        students = pd.read_csv(file_name)
        names = students['이름'].tolist()
        ages = students['나이'].tolist()
        addresses = students['주소'].tolist()
        g1 = students['국'].tolist()
        g2 = students['영'].tolist()
        g3 = students['수'].tolist()
        imgs = students['사진'].tolist()
        print(names)



student_data = StudentInfo()
student_data.get_info("./python_basic/ClassFunc/student_info.csv")
# student_data.get_info("./python_basic/ClassFunc/student_info.csv")