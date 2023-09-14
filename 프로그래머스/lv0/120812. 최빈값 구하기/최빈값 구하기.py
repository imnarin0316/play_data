import pandas as pd

def solution(array):
    arr = pd.Series(array)
    mod = list(arr.mode())
    if len(mod) == 1:
        return mod[0]
    elif len(mod) > 1: 
        return -1