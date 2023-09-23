import re
def solution(my_string, letter):
    a = re.split(re.escape(letter), my_string)
    b = ''.join(a)
    return b