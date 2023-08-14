def solution(num_list):
    su1 = []
    su2 = []
    for su in num_list:
        su2.append(str(su)) if su % 2 == 0 else su1.append(str(su))
    s1 = ''.join(su1)
    s2 = ''.join(su2)
    
    return int(s1) + int(s2)

print(solution([3, 4, 5, 2, 1]))
