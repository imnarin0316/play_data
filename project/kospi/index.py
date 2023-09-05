import pandas as pd
import os

# 현재 폴더 확인 및 지정
currentPath = os.getcwd()
# print(currentPath) #/playdata 까지만 나옴

# 코스피 지수 csv 파일 다운 2022.09.05 ~ 2023.09.05
# https://finance.yahoo.com/quote/%5EKS11/history?period1=1662336000&period2=1693872000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true

kospis_data = pd.read_csv(currentPath + '/project/kospi/kospi.csv')
# print(kospis_data)


# 하루 평균 코스피 값을 구하기
# 날짜, 높은 값, 낮은 값 종류대로 모으기
kospis_date = kospis_data['Date'].tolist()
kospis_high = kospis_data['High'].tolist()
kospis_low = kospis_data['Low'].tolist()
# print(kospis_date[0], kospis_high[0], kospis_low[0])


# 날짜, 하루 코스피 평균값 리스트 만들기
kospi_day = []
for date, high, low in zip(kospis_date, kospis_high, kospis_low):
    kospi_avg = (float(high) + float(low)) / 2
    kospi_day.append([date, round(kospi_avg, 2)])
# print(kospi_day[:5])


# 전날을 기준으로 한 등락 비율
for i in range(1, len(kospi_day)):
    result = ''
    per = kospi_day[i-1][1] / kospi_day[i][1]
    kospi_day[i].append(round(per, 2))
    
    # 결과값
    if kospi_day[i-1][1] > kospi_day[i][1] :
        result = '감소'
    elif  kospi_day[i-1][1] < kospi_day[i][1] :
        result = '증가'
    else :
        result = '변동없음' 
    kospi_day[i].append(result)  
# print('코스피 일별 변동 사항', kospi_day[:10])


# 감소한 날짜, 증가한 날짜 리스트 만들기
# 참고한 사이트에 의하면 뉴스가 나온 다음날 코스피의 등락이 결정된다고 하였으니, 만약 뉴스 기사가 뜨는 '당일'로 날짜를 구해야한다면 "kospi_day[i-1][0]" 로 날짜가 구해져야하는 것이 맞을 것 같음. 

kospi_up_date = []
kospi_down_date = []
for i in range(1, len(kospi_day)):
    if kospi_day[i][3] == '증가': 
        kospi_up_date.append(kospi_day[i][0])
    elif kospi_day[i][3] == '감소':
        kospi_down_date.append(kospi_day[i][0])
# print(kospi_up_date[:5], kospi_down_date[:5])
