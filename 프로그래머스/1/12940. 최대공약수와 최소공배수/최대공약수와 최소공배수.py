def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(n, m):
    gcd_result = gcd(n, m)
    lcm_result = lcm(n, m)
    
    return [gcd_result, lcm_result]
