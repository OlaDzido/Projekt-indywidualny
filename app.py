import requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import pandas as pd

import pymysql
import datetime
from datetime import date
from datetime import datetime as dt

a = (datetime.date.today())
x = dt.strftime(a, '%Y_%m_%d')





def scrapping ():
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

        vote = elem.find('span', {'class' : 'rate__count'}).text[:-6]
        if vote not in votes:
            votes.append(vote)

        place = elem.h3.span.text[:-1]
        if place not in places:
            places.append(place)

    votes = [elem.replace(" ", "") for elem in votes]
    votes = [int(elem) for elem in votes]
    ratings = [elem.replace(",",".") for elem in ratings]
    ratings = [(float(elem)) for elem in ratings]
    places = [int(elem) for elem in places]
    data = {'place': places,
        'tittle': name,
        'ratings': ratings,
        'votes': votes,
        'data' : str(day)
        }

    df = pd.DataFrame(data, columns=['place', 'tittle','ratings','votes', 'data'])

    tuples = list(df.itertuples(index=False, name=None))

    make_table_and_insert_data(tuples)



def make_table_and_insert_data(tuples):

    c.execute(
        """CREATE TABLE IF NOT EXISTS ranking{datax} (place INT(4) NOT NULL, tittle VARCHAR(60) NOT NULL,
        ratings DOUBLE NOT NULL, votes INT(20) NOT NULL, data DATE NOT NULL);""".format(datax=x))
    connection.commit()


    sql = (
        """INSERT INTO ranking{datax} (place,tittle,ratings,votes, data) VALUES (%s,%s,%s,%s,%s);""".format(datax=x, ))
    c.executemany(sql, tuples)
    connection.commit()



try:
    connection = pymysql.connect(host='127.0.0.1',
                                     user='username',
                                     password='password',
                                     db='films',
                                     charset='utf8mb4')


    print("Success")

except Exception as e:
        print (e)
        print ("No connection with database")
else:
    c = connection.cursor()
    c.execute("""SHOW TABLES FROM films;""")


    result = c.fetchall()
    format_result = []
    for elem in result:
        format_result.append((''.join(map(str, elem))))
        
    if "ranking{datax}".format(datax =x) in format_result:
        print("Taka tabela już istnieje")
    else:
        scrapping()







# c = self.connect.cursor()
# a =(datetime.date.today())
#
# x = dt.strftime(a, '%Y_%m_%d')
# c.execute("""CREATE TABLE IF NOT EXISTS ranking{datax} (place INT(4) NOT NULL, tittle VARCHAR(60) NOT NULL, ratings DOUBLE NOT NULL, votes INT(20) NOT NULL, data DATE NOT NULL);""".format(datax=x, elem=elem))
# connection.commit()
# sql=("""INSERT INTO ranking{datax} (place,tittle,ratings,votes, data) VALUES (%s,%s,%s,%s,%s);""".format(datax=x,))
# c.executemany(sql,tuples)
# connection.commit()
