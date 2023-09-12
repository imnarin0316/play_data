def solution(name, yearning, photo):
    
    answer = []
    for p in photo:
        hab = 0
        for pp in p:
            if pp in name:
                su = name.index(pp)
                hab += yearning[su]
        answer.append(hab) 
    return answer