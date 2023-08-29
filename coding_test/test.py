def solution(arr):
    stk = []
    i = 0

    for su in arr:
        if len(arr) == i :
            stk.append(arr[i])
        else: 
            if stk : 
                if stk[-1] == arr[i]:
                    stk.pop()
                    i += 1 
                else:
                    stk.append(arr[i])
                    i += 1 
            else:
                stk.append(arr[i])
                i += 1 

    if not stk:
        return [-1]
    
    return  stk

print(solution([0, 1, 1, 1, 0]))

