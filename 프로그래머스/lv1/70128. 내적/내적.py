def solution(a, b):
    li = [s1*s2 for s1, s2 in zip(a,b)]    
    return sum(li)