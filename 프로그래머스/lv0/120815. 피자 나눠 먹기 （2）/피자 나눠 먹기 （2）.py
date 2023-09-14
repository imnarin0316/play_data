def solution(n):
    idx = 1
    while 6*idx % n != 0:
        idx += 1
    return idx