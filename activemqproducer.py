import stomp
import random

q=random.Random()

conn = stomp.Connection([('localhost', 61613)])
conn.connect('admin', 'password', wait=True)
message='hello from producer 1 number'+str(q.random())
conn.send(body=message, destination='/queue/test')
conn.disconnect()
