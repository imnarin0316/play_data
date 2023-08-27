import pandas as pd

students = []
student_datalist = []
select_student = []
names = []
ages = []
addresses = []
g1 = []
g2 = []
g3 = []
imgs = []

class StudentInfo:
    
    def __init__(self, file_name):
        print("정보조회 시작")
        self.file_name= file_name
        
        global students, student_datalist, names, ages, addresses, g1, g2, g3, imgs
        
        students = pd.read_csv(file_name)
        
        names = students['이름'].tolist()
        ages = students['나이'].tolist()
        addresses = students['주소'].tolist()
        g1 = students['국'].tolist()
        g2 = students['영'].tolist()
        g3 = students['수'].tolist()
        imgs = students['사진'].tolist()
        
        student_datalist = list(zip(names, ages, addresses, g1, g2, g3))
        
    
    # def get_info(self):
        
    def show_info(self, idx):
        global select_student
        
        # 선택한 idx 값을 받아서 현재 조회하는 정보
        select_student = student_datalist[idx]
     
        
    def change_save(self, idx, new_info):
        students.loc[idx, ['이름', '나이', '주소', '국', '영', '수']] = new_info
        students.to_csv("./python_basic/ClassFunc/student_info.csv", index=False)
        


student_data = StudentInfo("./python_basic/ClassFunc/student_info.csv")