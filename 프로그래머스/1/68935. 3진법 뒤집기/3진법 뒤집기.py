def solution(n):
    answer = 0
    
    li = []
    su = n
    while su >= 1:
        s1 = su % 3
        if s1 == 1:
            li.append(str(1)) 
        else:
            li.append(str(s1))   
        su = su // 3
    
    li2 = sum([int(li[len(li) - i -1])*(3**i) for i in range(len(li))])
     
    return li2