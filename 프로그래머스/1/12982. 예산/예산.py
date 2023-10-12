def solution(d, budget):
    li = sorted(d)
    su = 0
    
    answer = []
    for i in range(len(li)) :
        su += li[i]
        if su <= budget:
            answer.append(li[i])
    
    return len(answer)