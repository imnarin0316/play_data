from tkinter import *
from tkinter import ttk
import json

students_data = []
file_name = './python_basic/ClassFunc/student.json'
with open(file_name, 'r', encoding="utf=8") as file:
    students_data = json.load(file)


class Comments: 
    title = "class를 이용하여 정보를 조회/수정 해보자"
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
root.geometry("500x500")
root.resizable(0,0)

# 타이틀
title = Comments.title
head_tit = Label(root, text=title, font=("helvetica",15))
head_tit.pack(padx=5, pady=15)

# Treeview 게시판 
treeclass = ttk.Treeview(root)
treeclass.column("name", width= 80, anchor="center")
treeclass.heading("name", text="이름", anchor="center")
treeclass.column("age", width= 80, anchor="center")
treeclass.heading("age", text="나이", anchor="center")
treeclass.column("address", width= 80, anchor="center")
treeclass.heading("address", text="주소", anchor="center")
treeclass.column("grade", width= 160, anchor="center")
treeclass.heading("grade", text="성적", anchor="center")
# treeclass["show"] = "headings"

# treeclass.pack()

root.mainloop()
