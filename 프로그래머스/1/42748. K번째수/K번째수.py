def solution(array, commands):
    answer = []
    for a,b,c in commands:
        li = sorted(array[a-1:b])
        answer.append(li[c-1])
    return answer