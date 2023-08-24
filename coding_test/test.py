def solution(arr):
    count = 1
    list_arr = [arr]
    
    while True:
        li = []
        for su in list_arr[count-1]:
            if su >= 50 and su % 2 == 0:
                li.append(int(su/2))
            elif su < 50 and su % 2 != 0:
                li.append(int(su*2 + 1))
            else:
                li.append(int(su))
            
        list_arr.append(li)
        count += 1
        print(list_arr)

        if list_arr[count-1] == list_arr[count-2]:
            return count-2  

print(solution([1, 2, 3, 100, 99, 98]))

