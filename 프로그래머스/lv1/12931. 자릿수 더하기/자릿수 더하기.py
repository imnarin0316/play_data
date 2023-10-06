def solution(n):
    answer = list(str(n))
    su = 0
    for i in range(len(answer)):
        su += int(answer[i])
    return su