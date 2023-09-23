def solution(n, k):
    drink = n // 10
    d = k - (drink)
    answer = n * 12000 + d * 2000
    return answer