def solution(a, b):
    minsu = min(a,b)
    maxsu = max(a,b)
    
    answer = 0
    for i in range(minsu, maxsu+1):
        answer += i
    return answer