def solution(rsp):
    dic = {
        '2':"0", '0':"5", '5':"2"
    }

    li = list(rsp)
    return ''.join([dic[su] for su in li ])