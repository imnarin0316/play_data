def solution(arr, divisor):
    answer = [su for su in arr if su % divisor == 0]
    
    if len(answer) == 0: 
        return [-1]
    
    return sorted(answer)