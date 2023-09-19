def solution(emergency):
    li = sorted(emergency, reverse=True) 
    answer = [li.index(su)+1 for su in emergency]
    return answer