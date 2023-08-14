# 문제 1 ~ 7
jumsu = [100, 90, 100, 80, 70, 100, 80, 90, 95, 85] 
# 위 리스트는 학생번호 1번 ~ 10번까지 10명의 시험 점수이다. 

#(1)  7번의 점수를 출력하세요 
print(jumsu[6])

#(2)  1번부터 5번까지의 점수를 출력하세요.
print(jumsu[:5])

#(3)  4, 5, 6, 7번의 점수를 출력하세요.
print(jumsu[3:7])

#(4) 짝수번째 점수를 출력하세요.
print(jumsu[1::2])

#(5) 홀수번째 점수를 출력하세요.
print(jumsu[::2])


#(6) 9번의 점수를 20으로 변경하고 전체 출력하세요.
jumsu[8] = 20
print(jumsu)

#(7) 중복된 점수는 제거하고 하나씩만 나오도록 출력하세요.
print(set(jumsu))

# 문제 8 ~ 9
fruits = ["복숭아", "수박", "딸기"]

#(8) fruits 리스트에 마지막 원소로 "사과", "귤"을 추가하세요.
fruits.extend(["사과", "귤"])
print(fruits)

#(9) fruits 리스트에서 "복숭아"를 제거하세요.
fruits.remove('복숭아')
print(fruits)

# 문제 10 ~ 15
#(10)본인의 이름, 나이, email주소, 취미, 결혼유무를 사전(딕셔너리)으로 생성. 
# 취미는 2개 이상의 값을 넣는다..
info = {
    "name": "김지인",
    "age": 28,
    "email": "imnarin0316@gmail.com",
    "hobby": ['Youtube', 'book'],
    "marry": False
}
info2 = dict(이름="홍길동", 나이=28, 이메일= "gmail.com", 취미=["독서", "운동"], 결혼=False)
print(info)

#(11) 위 딕셔너리에서 이름과 email주소를 조회해서 출력하세요.
print(info.get('name'), info.get('email'))
print(info['name'], info['email'])


#(12) 위 딕셔너리에서 취미중 두번째 취미를 조회해서 출력하세요.
print(info["hobby"][1])

#(13) 위 딕셔너리에 몸무게와 키 항목을 추가하세요.
info.update({"weight": None, "tall": 161})
# info["키"] = 161
# info["몸무게"] = None
print(info)

#(14) 위 딕셔너리에서 나이를 제거하세요.
info.pop("age")
# del info['age']
print(info)

#(15) 위 딕셔너리에서 email 주소를 다른 값으로 변경하세요.
info['email'] = "injji0316@naver.com"
print(info)

