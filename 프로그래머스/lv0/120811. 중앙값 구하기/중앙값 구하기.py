import pandas as pd
def solution(array):
    pdme = pd.Series(array)
    return int(pdme.median())