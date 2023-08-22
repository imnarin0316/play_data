from tkinter import Tk, Label, Frame
from tkinter import ttk
import json

students_data = []
file_name = './python_basic/ClassFunc/student.json'
with open(file_name, 'r', encoding="utf=8") as file:
    students_data = json.load(file)

class Comments: 
    title = "학생조회"
    head_title = "학생을 클릭하면 정보를 조회할 수 있습니다."
    error = "실행 불가"

class ClassMate:
    _data = students_data
    _name = 'class_mate'

    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address


root = Tk()
root.title(Comments.title)
root.geometry("996x776")
root.resizable(0,0)

# 타이틀
title = Comments.head_title
head_tit = Label(root, text=title, font=("inter",20,"bold"), bg='#F0F0F0')
head_tit.place(x=198, y=50, width=600, height=30)

# 정보 확인용 프레임
about = Frame(root, width=664, height=50, relief='solid', bd=1, bg='#ffffff')
about.place(x=50, y=112,  width=664, height=50 )

# 버튼들 프레임
btns = Frame(root, width=200, height=50, bg='#ffffff')
btns.place(x=746, y=112,  width=200, height=50 )

root.configure(bg="#F0F0F0")
root.mainloop()
