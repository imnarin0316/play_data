def solution(s):
    li = sorted(list(s))
    if li[-1] <= '9' and (len(s) == 4 or len(s) == 6) :
        return True
    else:
        return False