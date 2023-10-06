def solution(x):
    su = 0
    ls = str(x)
    for i in range(len(ls)):
        su += int(ls[i])

    if x % su == 0:
        return True
    else:
        return False