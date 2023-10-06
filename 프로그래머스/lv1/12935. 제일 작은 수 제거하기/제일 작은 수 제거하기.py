def solution(arr):
    idx = arr.index(min(arr))

    if len(arr) == 1:
        return [-1]
    else: 
        arr.pop(idx)
        return arr
        