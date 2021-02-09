from psycopg2 import connect
from datetime import date,datetime
from string import ascii_letters
from random import choices
import sys

#this function connects to db and inserts rows in jobdemo table
def insert_rows():
    print('connecting')
    conn = connect(host=str(sys.argv[1]),dbname='postgres',user="read_write",password='read_write')
    print('connected')
    cur = conn.cursor()
    curr_date=date.today()
    time = datetime.now().time()
    for i in range(5):
        char = ''.join(choices(ascii_letters, k=5))
        cur.execute('INSERT INTO jobdemo(cur_date,time,number,char) VALUES (%s,%s,%s,%s)',(curr_date,time,i+1,char))
    conn.commit()
    conn.close()
    print('connection closed')


if __name__ == "__main__":
    insert_rows()

