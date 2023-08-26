# # 데이터들을 용도대로 모아두고 zip 함수로 조회하기
# #  with block 으로 데이터 불러오기
# # 변경된 값을 'w'으로 수정하기
# import pandas as pd

# # CSV 파일을 DataFrame으로 읽어오기
# df = pd.read_csv("./python_basic/ClassFunc/student_info.csv")
# print(df)


# # 데이터 수정
# # 예를 들어, 이름이 "유재석"인 데이터의 나이를 31로 변경
# df.loc[df['이름'] == '최보라', '나이'] = 31
# print(df)
# # 수정된 데이터를 CSV 파일로 저장
# df.to_csv("./python_basic/ClassFunc/student_info2.csv", index=False)

# print("수정된 데이터가 저장되었습니다.")
