def solution(arr):
    idx = [i for i in range(len(arr)) if arr[i] == 2]
    print(idx[0] , idx[-1])
    a = idx[0]
    b = idx[-1]
    print(arr[a,b])
    if idx :
        return arr[a,b] 
    else :
        return [-1]

print(solution([1, 2, 1, 4, 5, 2, 9]))

