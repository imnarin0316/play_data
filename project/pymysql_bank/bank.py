# 이름, 시작날짜, 마감날짜, 사용할 금액 입력 
# 지출 - , 입금 +
# 사용처, 금액 입력
# 재시작. 모든 정보 지우기 

from datetime import datetime, date, time

# 이름 입력하기
# name = input("이름을 입력하세요:") 
name = "김지인" # default


def change_date(day):
    dt = datetime.strptime(day, '%Y%m%d')
    bank_date = dt.date()
    return bank_date

# 시작 날짜, 끝나는 날짜
# s_d = input("시작날짜를 작성해주세요. 예) 20230901  :")
# e_d = input("마치는 날짜를 작성해주세요. 예) 20230910  :")

# start_date = change_date(s_d)
# end_date = change_date(e_d)

# default
start_date = change_date("20230901")
end_date = change_date("20230910")

# 디데이 구하기
miu_day = end_date - start_date
d_day = miu_day.days + 1
# print(d_day)


# 기간동안 사용할 금액 입력
# total_money = input("금액을 어느정도 사용할 예정일까요? 예) 50000  : ")

# default
total_money = 50000

# 오늘 하루 사용할 금액
day_money = round(total_money // d_day, -1)
# print(day_money)


# 입출금 내역
li_all = []
while True:
    sobi_money = input("입금, 출금 내역을 입력해주세요: ")
    if '-' in sobi_money: 
        li = sobi_money.split('-')
        li[0] = "출금"
        li_all.append(li)
    elif '+' in sobi_money:
        li = sobi_money.split('+')
        li[0] = "입금"
        li_all.append(li)
    elif sobi_money == "end" : 
        break

print(li_all)

