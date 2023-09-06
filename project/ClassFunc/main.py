from tkinter import Tk, ttk, Label, Frame, Button, Entry, Image, END
import tkinter.messagebox as messagebox 
import program_info as pinfo
from PIL import Image, ImageTk

# 공통 텍스트 미리 설정 
class Comments: 
    title = "학생조회"
    head_title = "학생을 클릭하면 정보를 조회할 수 있습니다."
    error = "실행 불가"
    lavel_list = ["이름: ","나이: ","주소: ","국어: ","영어: ","수학: "]
    save = '변경 완료' 
    save_txt = '정보가 변경되었습니다.'

    
selected_idx = []

def convert_to_int_or_raise(value, ty):
    try:
        ty(value)
    except ValueError:
        raise ValueError(f"Cannot convert '{value}' to an integer.")

def change_save():
    global selected_idx, entry_widgets

    if selected_idx:
        sel_student_info = tuple(entry_widget.get() for entry_widget in entry_widgets)
<<<<<<< Updated upstream:project/ClassFunc/main.py
        name, age_str, address, g1_str, g2_str, g3_str = sel_student_info
        try:
            age = int(age_str)
            g1 = int(g1_str)
            g2 = int(g2_str)
            g3 = int(g3_str)
        except ValueError:
            messagebox.showerror("Error", "이곳에는 숫자만 작성 가능합니다.")
            return

        # pinfo.student_data.change_save(selected_idx, sel_student_info)
        # 바꾼값으로 저장하기 위해서 객체 이름 작성해줌
        pinfo.student_data.change_save(selected_idx, (name, age, address, g1, g2, g3))
=======
        pinfo.student_data.change_save(selected_idx, sel_student_info)
>>>>>>> Stashed changes:python_basic/ClassFunc/main.py
    
        messagebox.showinfo(Comments.save, Comments.save_txt)  # 변경 완료 메시지 표시
        pinfo.StudentInfo("./project/ClassFunc/student_info.csv")
        show_student_info(selected_idx)
            
        
def show_student_info(idx):
    global selected_idx
    selected_idx = idx

    student_info = pinfo.student_datalist[idx]
    for i, info in enumerate(student_info):
        entry_widget = entry_widgets[i]  # 해당 인덱스의 Entry 위젯 가져오기
        entry_widget.delete(0, END)  # Entry 위젯 내용 초기화
        entry_widget.insert(0, str(info))  # 학생 정보 삽입


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

# 라벨 만들기
for i in range(len(Comments.lavel_list)):
    label = Label(about, text=Comments.lavel_list[i], font=("Pretendard",12), bg='#f0f0f0')
    label.place(x=26 + (104 * i), y=15, width=31 ,height=20 )


# 조회 모음
entry_widgets = []
num_entries = 6  # 생성할 빈 Entry 위젯의 개수
for i in range(num_entries):
    entry = Entry(about, bd=0, font=("Pretendard", 14))
    entry.place(x=57 + (104 * i), y=5, width=58, height=40)
    entry_widgets.append(entry)
    # print(entry_widgets)


# 버튼들 프레임
btns = Frame(root, width=200, height=50, bg='#F0F0F0')
btns.place(x=746, y=112,  width=200, height=50 )
    
save_btn = Button(btns, text='변경', bg="#D6D6D6", bd=1, font=("Pretendard",16, 'bold'), command=change_save)
save_btn.place(x=0, y=0, width=200, height=50)


# 이미지 프레임
imgbtns = Frame(root, width=896, height=532, bg='#F0F0F0')
imgbtns.place(x=50, y=194,  width=896, height=532 )

# 이미지 객체를 저장할 리스트 생성
image_list = []
for i in range(len(pinfo.student_datalist)):
    image_pil = Image.open(f"./project/ClassFunc/button_image_{i}.png")
    image = ImageTk.PhotoImage(image_pil)
    image_list.append(image) 
    
    # 학생 이름을 버튼 텍스트로 설정
    image_button = Button(imgbtns, image=image, command=lambda idx=i: show_student_info(idx))
    image_button.place(x=(i % 4) * 232, y=(i // 4) * 282, width=200, height=250)


root.configure(bg="#F0F0F0")
root.mainloop()
