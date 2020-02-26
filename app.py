import requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, date

url = 'https://www.filmweb.pl/ranking/netflix/Komedia/13/2018'
page = requests.get(url)
html_soup = BeautifulSoup(page.text, 'html.parser')
movie_containers = html_soup.find_all('div', {'class': 'item place'})

name = []
ratings = []
votes = []
places = []
day = date.today()

for elem in movie_containers:


    title = elem.h3.a.text
    if title not in name:
        name.append(title)

    rate = elem.find('span', {'class' : 'rate__value'}).text
    if rate not in name:
        ratings.append(rate)

    vote = elem.find('span', {'class' : 'rate__count'}).text
    if vote not in votes:
        votes.append(vote)

    place = elem.h3.span.text
    if place not in places:
        places.append(place)



print(name, ratings, votes)
data = {
    "Date" : day,
    "Place" : places,
    "Title" : name,
    "Rating" :ratings,
    "Votes" : votes

}
df = pd.DataFrame(data, columns=["Place","Title", "Rating", "Votes", "Date"])
print(df)
df = df['Place'].str[-3:-1].astype(int)
print(df)