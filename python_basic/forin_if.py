#(1) 다음 점수 구간에 맞게 학점을 출력하세요.
# 91 ~ 100 : A학점
# 81 ~ 90 :  B학점
# 71 ~ 80 :  C학점
# 61 ~ 70 :  D학점
# 60이하   :  F학점
num = 80
if num > 90 :
    n = 'A'
elif num > 80 : 
    n = 'B'
elif num > 70 :
    n = 'c'
elif num > 60 : 
    n = 'D'
else: 
    n = "F"
print(f"{n}학점")


#(2) 사용자로 부터 ID를 입력 받은 뒤 입력받은 ID가 5글자 이상이면 "사용할 수 있습니다."를 5글자 미만이면 "사용할 수 없는 ID입니다."를 출력하세요.
user_id = 'myidsample'
# user_id = input('ID를 입력하세요 : ')
if len(user_id) >= 5 :
    id_text = '있'
else :
    id_text = '없'
print(f"사용할 수 {id_text}습니다.")

#(3) 사용자로부터 우리나라 도시명을 입력 받은 뒤 입력받은 도시명이 서울이면 "특별시"를 인천,부산,광주,대구,대전,울산 이면 "광역시"를 나머지는 "특별시나 광역시가 아닙니다."를 출력하세요.
city = '인천'
# city = input('도시를 입력하세요 : ')
if city == '서울':
    city_name = '특별시'
elif city in ('인천', '부산', '광주', '대구', '대전', '울산') : 
    city_name = '광역시'
else:
    city_name = '특별시나 광역시가 아닙니다.'
print(f"{city} : {city_name}")

#(4) 아래 리스트의 평균을 구하시오. 
jumsu = [100, 90, 100, 80, 70, 100, 80, 90, 95, 85]
avarage = sum(jumsu)/len(jumsu)
print(avarage)

#(5) 위 jumsu리스트에서 평균점수이상은 pass, 미만은 fail을 index번호와 함께 출력하시오. (ex: 0-pass, 1-pass, 2-fail)
p_f = []
for i in range(len(jumsu)) :
    if jumsu[i] >= avarage :
        p_f.append(f"{i}-pass")
    else:
        p_f.append(f"{i}-fail")
print(', '.join(p_f))


#(6) 아래 리스트 값들 중 최대값을 조회해 출력
jumsu = [60, 90, 80, 80, 70, 55, 80, 90, 95, 85]
print(max(jumsu)) # 이것은 간단 문법
 

#(7) 다음 리스트 중에서 "쥐"와 "토끼" 제외한 나머지를 출력하세요.
str_list = ["쥐", "소", "호랑이", "토끼", "용", "뱀"]
for animal in str_list:
    if animal not in ('쥐', '토끼'):
        print(animal, end=' ' )

        
print('\n')
#(8) 사용자로부터 정수를 입력받아 그 단의 구구단을 출력하시오. 
# ex) 단을 입력하시오 : 2  
# 2 x 1 = 2
# 2 x 2 = 4
#..
# 2 x 9 = 18
gogodan = 5
# gogodan = int(input('단을 입력하세요: '))
for su8 in range(1, 10) : 
    print(f"{gogodan} X {su8} = {gogodan*su8}")

#컴프리헨션

#(9) 다음 리스트가 가진 값에 두배(* 2)를 가지는 새로운 리스트를 만드시오. (리스트 컴프리헨션 이용)
lst = [10, 30, 70, 5, 120, 700, 1, 35]
l1 = []
for su in lst: 
    l1.append(su*2)
print(l1)

#(10) 다음 리스트가 가진 값에 10배의 값을 가지는 값을 (원래값, 10배값) 의 튜플 묶음으로 가지는 리스트를 만드시오 (리스트 컴프리헨션 이용)
# Ex) [(10,100), (30,300), .., (35, 350)]
lst = [10, 30, 70, 5, 5, 120, 700, 1, 35, 35]
l2 = []
for su10 in lst:
    l2.append((su10, su10*10))
print(l2)


#(11) 다음 리스트가 가진 값들 중 3의 배수만 가지는 리스트를 만드시오. (리스트 컴프리헨션 이용)
lst2 = [ 3, 20, 33, 21, 33, 8, 11, 10, 7, 17, 60, 120, 2]
l3 = []
for su11 in lst2:
    if su11 % 3 == 0 :
        l3.append(su11)
print(l3)

#(12) 다음 파일이름들을 담은 리스트에서 확장자가 exe인 파일만 골라서 새로운 리스트에 담으시오.(string의 endswith()함수 이용)
file_name=["test.txt", "a.exe", "jupyter.bat", "function.exe", "b.exe", "cat.jpg", "dog.png", "run.exe", "i.dll"]
exe = []
for file in file_name:
    if "exe" in file :
        exe.append(file)
print(exe)


#(13) 다음 중 10글자 이상인 파일명(확장자포함)만 가지는 리스트를 만드시오.
file_name=["mystroy.txt", "a.exe", "jupyter.bat", "function.exe", "b.exe", "cat.jpg", "dog.png", "run.exe", "i.dll"]
len10 = []
for file in file_name:
    if len(file) >= 10 : 
        len10.append(file)
print(len10)


#(14) 다음 리스트에서 소문자만 가지는 새로운 리스트를 만드시오.
str_list = ["A", "B", "c", "D", "E", "F", "g", "h", "I", "J", "k"]
lowerli = []
for low in str_list:
    if low >= 'a':
        lowerli.append(low)
print(lowerli)