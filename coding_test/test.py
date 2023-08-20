def solution(my_string, m, c):
    # answer += my_string[c::m] 
    # for i in range(len(my_string)):
    #     if c+m*i <= len(my_string) :
    #         answer= answer + my_string[c + m*i]
      
    return my_string[c-1::m]
    # return answer

print(solution("ihrhbakrfpndopljhygc", 4,2))