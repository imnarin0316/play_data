# 데이터 타입 대표 예제 모음



# 값 없음(None)
# 값이 정해져 있지 않은 값을 표현할 때 None을 사용한다. 
tall = None



# 숫자형(int , float)
# 숫자형 가독성 좋게 나타내는 법
print(50_000) #50000



# 논리형(bool)
# 논리형은 True, False로 나뉘어져 있다.


# 비교연산자
age = 10
age >= 20 and age <= 29  #false
(age >= 20) & (age <= 29) # &를 사용하려면 ()로 묶어야 함.

age > 20 or age < 30 # 20대인지 알아보기
not (age >= 20 and age <= 29) # 위 코드랑 같은 값을 나타냄


# 논리 연산자
True ^ True    # False
False ^ False  # False
True ^ False   # True


# 조건연산자
v = '참' if True else '거짓' 
#'참' if 0 else '거짓'로 될 경우에 0은 bool형으로 변경되어 '거짓'이 나타남
print(v) #'참'

num = input("정수") # 10을 입력하더라도 문자열 10으로 저장됨
num >= 0  # 타입 에러가 나서 num을 int 정수형으로 변환 해줘야 함
int(num) >= 0 # True
num = int(input("정수")) # 또는 input 입력 받을 때 정수 값으로 변경하기

# 조건이 3개 이상일 때 - 
# num이 0초과면 '양수' , 0미만이면 '음수', 0이면 0을 출력
num = int(input("숫자"))
result = "양수" if num > 0 else "음수" if num < 0 else "0"



# 문자형(str)
s1 = '안녕하세요 \n반갑습니다. \n잘부탁드려요.'
s2 = """안녕하세요
반갑습니다
잘부탁드려요"""

s1 == s2
#큰 따옴표, 작은 따옴표 상관없음

# 또는 r을 사용
print(r"c:\test\ncount\best.txt")


# 문자열 연산자.
name = "홍길동"
print("이름:" + name)

# But 같은 타입만 연산이 가능하기 때문에 age를 문자열로 바꿔주어야 함.
age = 20
print("나이:" + str(age)) 

print("-" * 20) #--------------------


#in, not in
# address안에 서울이라는 글자가 있는지 확인
address = "서울시 금천구 독산동"
"서울" in address, "서울" not in address


# len
len(address)

#비교연산
name = "홍길동"
name == "홍길동"
name != "홍길동"

# 같은 종류의 문자끼리 비교할 때는 사전식 배열(앞의 것이 뒤의 것보다 작다)
# 특수문자 < 숫자 < 대문자 < 소문자 < 한글 (유니코드)
"A" > "B"
# 문자 유니코드를 정수로 변환 - ord
ord("A")


