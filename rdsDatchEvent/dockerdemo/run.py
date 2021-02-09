from psycopg2 import connect, sql


# this function should be run at starting of the application
# this function creates a table and users from commands.sql file
def initial_actions():
    print('connecting')
    conn = connect(host='drwkgms0gaamsc.clrmgguj6yyz.ap-south-1.rds.amazonaws.com', dbname='postgres', user="demo",
                   password='demo8898')
    print('connected')
    cur = conn.cursor()
    cur.execute("select exists(select * from information_schema.tables where table_name='jobdemo')", ('mytable',))
    f = cur.fetchone()[0]
    cur.execute('DROP TABLE if exists jobdemo;')
    cur.execute('CREATE TABLE jobdemo(index serial,cur_date date,time time,number integer,char varchar(15));')
    if not f:
        cur.execute(sql.SQL(open("commands.sql", "r").read()))
    conn.commit()
    conn.close()
    print('connection closed')


if __name__ == '__main__':
    initial_actions()

