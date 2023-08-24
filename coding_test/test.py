def solution(arr):
    answer = [ su/2 if su >= 50 and su % 2 == 0 else su*2 if  su < 50 and su % 2 != 0 else su for su in arr  ]
    return answer

print(solution([1, 2, 3, 100, 99, 98]))

