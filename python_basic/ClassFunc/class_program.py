from tkinter import Tk, ttk, Label, Frame, Button, Entry, PhotoImage, Image
import json
from PIL import Image, ImageTk

students_data = []
file_name = './python_basic/ClassFunc/student.json'
with open(file_name, 'r', encoding="utf=8") as file:
    students_data = json.load(file)

class Comments: 
    title = "학생조회"
    head_title = "학생을 클릭하면 정보를 조회할 수 있습니다."
    error = "실행 불가"



def button_clicked():
    print("Button Clicked")

root = Tk()
root.title(Comments.title)
root.geometry("996x776")
root.resizable(0,0)

# 타이틀
title = Comments.head_title
head_tit = Label(root, text=title, font=("Pretendard",20,"bold"), bg='#F0F0F0')
head_tit.place(x=268, y=50, width=460, height=24)

# 정보 확인용 프레임
about = Frame(root, width=664, height=50, relief='solid', bd=1, bg='#ffffff')
about.place(x=50, y=112,  width=664, height=50 )

t_name = Label(about, text="이름:", font=("Pretendard",12), bg='#f0f0f0')
t_name.place(x=26, y=15, width=31 ,height=20 )
s_name = Entry(about, bd=0 , font=("Pretendard",14))
s_name.place(x=60, y=5, width=53, height=40)

t_age = Label(about, text="나이:", font=("Pretendard",12), bg='#f0f0f0')
t_age.place(x=137, y=15, width=31 ,height=20 )
s_age = Entry(about, bd=0 , font=("Pretendard",14))
s_age.place(x=170, y=5, width=53, height=40)

t_address = Label(about, text="주소:", font=("Pretendard",12), bg='#f0f0f0')
t_address.place(x=233, y=15, width=38 ,height=20 )
s_address = Entry(about, bd=0 , font=("Pretendard",14))
s_address.place(x=271, y=5, width=54, height=40)

t_lang = Label(about, text="국어:", font=("Pretendard",12), bg='#f0f0f0')
t_lang.place(x=337, y=15, width=38 ,height=20 )
s_lang = Entry(about, bd=0 , font=("Pretendard",14))
s_lang.place(x=375, y=5, width=54, height=40)

t_en = Label(about, text="영어:", font=("Pretendard",12), bg='#f0f0f0')
t_en.place(x=441, y=15, width=38 ,height=20 )
s_en = Entry(about, bd=0 , font=("Pretendard",14))
s_en.place(x=479, y=5, width=54, height=40)

t_math = Label(about, text="수학:", font=("Pretendard",12), bg='#f0f0f0')
t_math.place(x=545, y=15, width=38 ,height=20 )
s_math = Entry(about, bd=0 , font=("Pretendard",14))
s_math.place(x=583, y=5, width=54, height=40)

# 버튼들 프레임
btns = Frame(root, width=200, height=50, bg='#F0F0F0')
btns.place(x=746, y=112,  width=200, height=50 )

get_btn = Button(btns, text= '조회', bg="#D6D6D6", bd=1, font=("Pretendard",16, 'bold'))
get_btn.place(x=0, y=0, width=90, height=50)

save_btn = Button(btns, text='변경', bg="#D6D6D6", bd=1, font=("Pretendard",16, 'bold'))
save_btn.place(x=110, y=0, width=90, height=50)

# image_pil = []
for i in range(len(students_data)):
    # 각 학생별 이미지 생성 (student['image_path']는 이미지 파일 경로)
    image_pil = Image.open(f"./python_basic/ClassFunc/button_image_0.png")
    image = ImageTk.PhotoImage(image_pil)

    # 학생 이름을 버튼 텍스트로 설정
    image_button = Button(root, image=image, text=students_data[i]['name'], compound="top", command=button_clicked)
    image_button.place(x=110, y=0, width=90 + (i * 50), height=50)


    # # 이미지를 PIL로 열고 ImageTk.PhotoImage로 변환
    # image_pil = Image.open(f"./python_basic/ClassFunc/button_image_{i}.png")
    # image = ImageTk.PhotoImage(image_pil)

    # image_button = Button(root, image=image, command=button_clicked)
    # image_button.pack()




root.configure(bg="#F0F0F0")
root.mainloop()
