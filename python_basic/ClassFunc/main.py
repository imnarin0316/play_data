from tkinter import Tk, ttk, Label, Frame, Button, Entry, Image, END
import tkinter.messagebox as messagebox 
import program_info as pinfo
from PIL import Image, ImageTk

selected_idx = []

def change_save():
    global selected_idx, entry_widgets

    if selected_idx:
        sel_student_info = tuple(entry_widget.get() for entry_widget in entry_widgets)
        pinfo.student_data.change_save(selected_idx, sel_student_info)
     
        messagebox.showinfo("변경 완료", "정보가 변경되었습니다.")  # 변경 완료 메시지 표시
        pinfo.StudentInfo("./python_basic/ClassFunc/student_info.csv")
        show_student_info(selected_idx)
            
        
def show_student_info(idx):
    global selected_idx
    selected_idx = idx

    student_info = pinfo.student_datalist[idx]
    for i, info in enumerate(student_info):
        entry_widget = entry_widgets[i]  # 해당 인덱스의 Entry 위젯 가져오기
        entry_widget.delete(0, END)  # Entry 위젯 내용 초기화
        entry_widget.insert(0, str(info))  # 학생 정보 삽입
        
class Comments: 
    title = "학생조회"
    head_title = "학생을 클릭하면 정보를 조회할 수 있습니다."
    error = "실행 불가"


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

t_age = Label(about, text="나이:", font=("Pretendard",12), bg='#f0f0f0')
t_age.place(x=137, y=15, width=31 ,height=20 )

t_address = Label(about, text="주소:", font=("Pretendard",12), bg='#f0f0f0')
t_address.place(x=233, y=15, width=38 ,height=20 )

t_lang = Label(about, text="국어:", font=("Pretendard",12), bg='#f0f0f0')
t_lang.place(x=337, y=15, width=38 ,height=20 )

t_en = Label(about, text="영어:", font=("Pretendard",12), bg='#f0f0f0')
t_en.place(x=441, y=15, width=38 ,height=20 )

t_math = Label(about, text="수학:", font=("Pretendard",12), bg='#f0f0f0')
t_math.place(x=545, y=15, width=38 ,height=20 )

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

imgbtns = Frame(root, width=896, height=532, bg='#F0F0F0')
imgbtns.place(x=50, y=194,  width=896, height=532 )


# 이미지 객체를 저장할 리스트 생성
image_list = []
for i in range(len(pinfo.student_datalist)):
    image_pil = Image.open(f"./python_basic/ClassFunc/button_image_{i}.png")
    image = ImageTk.PhotoImage(image_pil)
    image_list.append(image) 
    
    # 학생 이름을 버튼 텍스트로 설정
    image_button = Button(imgbtns, image=image, command=lambda idx=i: show_student_info(idx))
    image_button.place(x=(i % 4) * 232, y=(i // 4) * 282, width=200, height=250)


root.configure(bg="#F0F0F0")
root.mainloop()
