def solution(slice, n):
    idx = 1
    while n > slice * idx : 
        idx += 1
    return idx