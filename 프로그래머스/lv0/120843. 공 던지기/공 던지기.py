def solution(numbers, k):
    if len(numbers) % 2 == 0:
        numbers_even = []
        for num_even in range(0,len(numbers),2):
            numbers_even.append(numbers[num_even])
        return numbers_even[(k % len(numbers_even)) - 1]
    elif len(numbers) % 2 != 0:
        numbers_odd = []
        for loop_cnt in range(2):
            for num_odd_0 in range(loop_cnt,len(numbers),2):
                numbers_odd.append(numbers[num_odd_0])
        return numbers_odd[(k % len(numbers_odd)) - 1]