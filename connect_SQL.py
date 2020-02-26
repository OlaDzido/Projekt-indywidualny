import app
import pymysql
import datetime
from datetime import date
from datetime import datetime as dt
connection = pymysql.connect(host='127.0.0.1',
                             user='username',
                             password='password',
                             db='films',
                             charset='utf8mb4')

c = connection.cursor()
a =(datetime.date.today())

x = dt.strftime(a, '%Y_%m_%d')
c.execute("""CREATE TABLE IF NOT EXISTS ranking{datax} (place INT(4), tittle VARCHAR(40), votes INT(20), data DATE);""".format(datax=x))
connection.commit()

