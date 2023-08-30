# 정수 배열 arr이 매개변수로 주어집니다. arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 합니다. arr에 최소한의 개수로 0을 추가한 배열을 return 하는 solution 함수를 작성해 주세요.

def solution(arr):
    length = len(arr)
    new_length = 1
    while new_length < length:
        new_length *= 2
    
    answer = [0] * new_length
    answer[:length] = arr
    
    return answer



#나의 식

# answer = [] 
#     i = 1
#     su = 1
    
    
#     while su < len(arr):
#         i += 1
#         su = 2 ** i
        
#     answer = [0] * su
#     answer[:len(arr)] = arr
        
#     return answer