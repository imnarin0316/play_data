def solution(dot):

    a, b = dot
    if a > 0 :
        if b > 0 : 
            return 1
        else:
            return 4
    else:
        if b > 0 :
            return 2
        else:
            return 3
