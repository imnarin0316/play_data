def solution(x, n):
    li = []
    count = 1
    while len(li) != n:
        li.append(x*count)
        count += 1
    return li