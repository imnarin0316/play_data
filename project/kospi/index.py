import pandas as pd
import os

# 현재 폴더 확인 및 지정
currentPath = os.getcwd()
# print(currentPath) #/playdata 까지만 나옴

# 코스피 지수 csv 파일 다운 2022.09.05 ~ 2023.09.05
# https://finance.yahoo.com/quote/%5EKS11/history?period1=1662336000&period2=1693872000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true

kospi_data = pd.read_csv(currentPath + '/project/kospi/kospi.csv')
print(kospi_data)