import math

def solution(n):
    root = math.sqrt(n)
    
    if int(root) == root :
        return (root + 1) ** 2 
    else: 
        return -1