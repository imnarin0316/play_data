def solution(n):
    n = list(str(n))
    answer = [int(n[i]) for i in range(len(n)) ] 
    return answer[::-1]