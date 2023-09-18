def solution(num_list):
    a = []
    b = []
    for su in num_list:
        a.append(su) if su % 2 else b.append(su) 
    return (len(b), len(a))