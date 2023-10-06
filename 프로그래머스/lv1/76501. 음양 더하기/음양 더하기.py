def solution(absolutes, signs):
    li = [int(-a) if b == False else a for a,b in zip(absolutes, signs)]
    return sum(li)