import requests
import pandas as pd
import json

url = "https://imdb8.p.rapidapi.com/auto-complete"

querystring = {"q":"game of thr"}

headers = {
	"X-RapidAPI-Key": "e2b6134f8fmsh21291de9a19fa43p1db807jsn19c61fda5b7b",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

json = response.json()
movies = json['d']

items =[]
for movie in movies:
    dic ={}
    dic['title'] = movie['l']
    dic['actors'] = movie['s']
    dic['year'] = movie.get('y', 'N/A')  # 'y' 키가 없는 경우 'N/A'를 사용
    dic['rank'] = movie.get('rank', 'N/A') 
    items.append(dic)
print(items)


