import pandas as pd

def solution(numbers):
    answer = pd.Series(numbers).mean()
    return answer 