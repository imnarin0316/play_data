def solution(my_string, indices):
    li = list(my_string)
    
    # for i in range(len(my_string)) :
    for su in sorted(indices, reverse=True):
        del li[su]

    return ''.join(li)

print(solution('apporoograpemmemprs', [1, 16, 6, 15, 0, 10, 11, 3]))

