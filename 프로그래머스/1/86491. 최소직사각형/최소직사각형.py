def solution(sizes):
    w = [max(sl) for sl in sizes]
    h = [min(sl) for sl in sizes]
    
    return max(w)*max(h)