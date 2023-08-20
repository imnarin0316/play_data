def solution(my_string, s, e):
    answer = my_string.replace(my_string[s:e+1], my_string[e:s-1:-1])
    # print(my_string[6:13], my_string[-6:-10])
    return answer

print(solution("Progra21Sremm3", 6,12))