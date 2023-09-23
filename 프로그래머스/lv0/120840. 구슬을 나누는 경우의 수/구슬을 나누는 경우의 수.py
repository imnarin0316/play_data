def solution(balls, share):
    n = 1 
    m=1 
    nm=1
    for i in range(balls):
        n *= i+1
    for j in range(share):
        m *= j+1
    for z in range(balls - share):
        nm *= z+1
    
    
    return n / (nm * m)