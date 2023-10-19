def solution(s):
    st = s.split(' ')
    answer = []
    for strr in st:
        st_r = ''
        for i in range(len(strr)): 
            if i % 2 == 0:
                st_r+=strr[i].upper()
            else:
                st_r+=strr[i].lower()
        answer.append(st_r)    
    return ' '.join(answer)