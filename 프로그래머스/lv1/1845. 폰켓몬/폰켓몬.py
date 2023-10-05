
def solution(nums):
    half = len(nums) / 2
    li = len(set(nums))
    
    return half if li >= half else li