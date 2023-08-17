def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr) : 
        if stk :
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
                print(stk, i)
            else: 
                stk.pop()
                print(stk, i)
        else:
            stk.append(arr[i])
            print(stk, i)
            i += 1
            
    return stk

print(solution([1, 4, 2, 5, 3]))

