def solution(age):
    answer = ''
    li = list(str(age))
    abc = 'abcdefghij'
    
    for su in li:
        answer += abc[int(su)]
        
    return answer