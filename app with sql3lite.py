import sqlite3

from datetime import datetime as dt
import datetime
c = sqlite3.connect('films.db')
con = c.cursor()


a =(datetime.date.today())

x = dt.strftime(a, '%Y_%m_%d')
c.execute("""CREATE TABLE IF NOT EXISTS ranking{datax} (place INT(4), tittle VARCHAR(40), votes INT(20), data DATE);""".format(datax=x))
c.commit()


