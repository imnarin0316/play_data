# 간단한 터미널 기반 메모장
# 사용자로부터 파일명을 입력받는다.
# 사용자로부터 파일에 저장할 문장을 입력받아서 파일에 저장한다.
# 한줄씩 입력받는다.
# 사용자가 !q 를 입력하면 저장후 종료한다.
# 사용자가 저장한 파일을 읽어서 출력한다.

import os
os.chdir(r"c:\class\Python")
print(os.getcwd())

class StrNameException(Exception): #Exception 상속받기
    def __init__(self, file_name):
        self.file_name = file_name
        
    def __str__(self):
        #exception 메세지를 문자열로 반환. 왜 인셉션이 났는지.
        return f"{self.file_name}에 '.txt'가 속하지 않았습니다."

class WrFile:
    def __init__(self):
        print("파일 생성하기")
    
    def save_file(self, file_name):
        if '.txt' not in file_name:
            raise StrNameException(file_name)
        else:    
            with open(file_name, 'at', encoding="utf-8") as fw:
                content_txt = ''
                while content_txt != '!q':
                    content_txt = input('저장한 문장을 한줄씩 입력하세요.: ')
                    if content_txt != '!q':
                        fw.write(content_txt + '\n')
                print("저장이 완료되었습니다.\n\n")

    def read_file(self,file_name):
        print(f"{file_name} 파일을 읽어왔습니다.")
        with open(file_name, 'rt', encoding="utf-8") as fr:
            read_fr = fr.read()
            print(read_fr)
         

wr = WrFile()
file_n = input("파일이름:")
wr.save_file(file_n)
wr.read_file(file_n)