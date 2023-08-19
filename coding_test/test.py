<<<<<<< Updated upstream
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

=======
def solution(my_string, queries):
    answer = my_string

    for a, b in queries:
        answer = answer.replace(answer[a:b+1], answer[a:b+1][::-1])

    return answer



print(solution("rermgorpsam",[[2, 3], [0, 7], [5, 9], [6, 10]]))
>>>>>>> Stashed changes
