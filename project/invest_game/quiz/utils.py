import requests
import random
from django.shortcuts import render

# 키 발급은 https://krdict.korean.go.kr/openApi/openApiInfo
apikey = '3376CC854BAB8ED661CCD439075BE089'

def midReturn(val, s, e):
    if s in val:
        val = val[val.find(s) + len(s):]
        if e in val:
            val = val[:val.find(e)]
    return val

def midReturn_all(val, s, e):
    if s in val:
        tmp = val.split(s)
        val = []
        for i in range(0, len(tmp)):
            if e in tmp[i]:
                val.append(tmp[i][:tmp[i].find(e)])
    else:
        val = []
    return val

def findword(query):
    url = 'https://krdict.korean.go.kr/api/search?key=' + apikey + '&part=word&pos=1&q=' + query
    response = requests.get(url)
    ans = []

    words = midReturn_all(response.text, '<item>', '</item>')
    for w in words:
        word = midReturn(w, '<word>', '</word>')
        pos = midReturn(w, '<pos>', '</pos>')
        if len(word) > 1 and pos == '명사' and word == query:
            ans = w
            ans_arr.append(w)
    if len(ans) > 0:
        return random.choice(ans)
    else:
        return ''

def checkexists(query):
    url = 'https://krdict.korean.go.kr/api/search?key=' + apikey + '&part=word&sort=popular&num=100&pos=1&q=' + query
    response = requests.get(url)
    ans = ''
    ans_arr = []

    words = midReturn_all(response.text, '<item>', '</item>')
    for w in words:
        word = midReturn(w, '<word>', '</word>')
        pos = midReturn(w, '<pos>', '</pos>')
        if len(word) > 1 and pos == '명사' and word == query:
            ans = w
            ans_arr.append(w)
    if len(ans) > 0:
        return ans_arr
    else:
        return ''


