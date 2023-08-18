# 1. 사용자가 입력한 단의 구구단을 출력하는 함수를 구현(매개변수로 단을 받는다.)
def gogodan(num):
    for i in range(1, 10):
        print(f"{num} X {i} = {num*i}")

# print(gogodan(int(input('단을 입력하세요 : '))))
print(gogodan(5))


# 2. 시작 정수, 끝 정수를 받아 그 사이의 모든 정수의 합을 구해서 반환하는 함수를 구현
# (ex: 1, 20 => 1에서 20 사이의 모든 정수의 합계)
def hab(num1, num2):
    """
    지정한 범위의 정수들의 합계를 계산해서 반환하는 함수
    Parameter
        start : int - 범위의 시작 정수
        설명들..~~
    """
    su = list(range(num1, num2+1))
    return sum(su)

print(hab(1,3))



# 3. 2번 문제에서 시작을 받지 않은 경우 0을, 끝 정수를 받지 않으면 10이 들어가도록 구현을 변경
def hab2(num1=0, num2=10):
    su = list(range(num1, num2+1))
    return sum(su)

print(hab2(num2=3))


def accumulate3(**kwargs):
    # 가변인자를 사용할 경우 docsting에 설명을 꼭 달아줘야함.
    """
    Parameter 
        start : 
        stop : 

    """
    start = kwargs['start']
    stop = kwargs['stop']

    return sum(range(start,stop))

accumulate3(start=10, stop=30)

# 4. 체질량 지수는 비만도를 나타내는 지수로 키가 a미터 이고 몸무게가 b kg일때 b/(a**2) 로 구한다.
# 체질량 지수가
#- 18.5 미만이면 저체중
#- 18.5이상 25미만이면 정상 
#- 25이상이면 과체중
#- 30이상이면 비만으로 하는데
#몸무게와 키를 매개변수로 받아 비만인지 과체중인지 반환하는 함수를 구현하시오.

def bmi(my_info):
    weight, tall = my_info.split(",")
    bmi_su = int(weight)/(int(tall)**2)
    
    if bmi_su >= 30:
        return '비만'
    elif bmi_su >= 25:
        return '과체중'
    elif bmi_su >= 18.5:
        return '정상'
    else :
        return '저체중'

# print(bmi(input('몸무게, 키를 입력하세요. : ')))
print(bmi('50, 160'))

# round(float: 반올림) : 소수점 두 자리 이하에서 반올림 됨. 
# float을 'float: 미터단위' 문자열로 작성해도 무방.
def check_bmi(tall:float, weight:float) -> str:
    """
    bmi 지수를 계산해서 비만도를 알려주는 함수
    Parameter
        tall : float - 키, 단위: 미터
        weight : float - 몸무게. 단위:kg
    Return
        str - 비만도(저체중, 정상, 과체중, 비만)
    Raise
    """



# 람다식
#5. filter()를 이용해 다음 리스트에서 양수만 추출히 리스트를 구현
ex1 = [1, -10, -2, 20, 3, -5, -7, 21]
print(list(filter(lambda x: x > 0, ex1)))

print([v for v in ex1 if v>0])

#6. filter()와 map()을 이용해 다음 리스트에서 음수만 추출한 뒤 그 2 제곱한 값들을 가지는 리스트를 구현
ex2 = [1, -10, -2, 20, 3, -5, -7, 21]
li = list(filter(lambda x : x < 0, ex2))
print(list(map(lambda x : x**2 , li)))

# 합쳐서 해도 무방
print(list(map(lambda x : x**2 , list(filter(lambda x : x < 0, ex2)))))


