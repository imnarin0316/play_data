def solution(s, n):
    result = []
    
    for char in s:
        if char.isalpha():  
            if char.islower():
                shifted = chr(((ord(char) - ord('a') + n) % 26) + ord('a'))
            else:
                shifted = chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
        else:
            shifted = char 

        result.append(shifted)
    
    return ''.join(result) 