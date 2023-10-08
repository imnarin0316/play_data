def solution(price, money, count):
    p = 0
    for i in range(1, count+1):
        p = p + (price * i)
    if money >= p :
        return 0
    return abs(p - money)