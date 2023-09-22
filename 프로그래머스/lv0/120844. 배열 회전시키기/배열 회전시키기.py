def solution(numbers, direction):
    answer = []
    
   
    if direction == "right":
        for i in range(len(numbers)): 
            answer.append(numbers[i-1])
    else: 
        numbers.append(numbers[0])
        for i in range(len(numbers)-1): 
            if i == len(numbers)-2:
                answer.append(numbers[0])
            else: answer.append(numbers[i+1])
    return answer