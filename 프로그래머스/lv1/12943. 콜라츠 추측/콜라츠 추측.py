def solution(num):
    su = num
    count = 0 
    
    while su != 1:
        if su % 2 == 0 :
            su /= 2
            count += 1
        else: 
            su = su * 3 + 1
            count += 1
    
    if count >= 500:
        return -1 
    
    return count