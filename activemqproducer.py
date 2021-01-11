import stomp
import random


# This function connects to activemq using stomp and pushes message to the queue 
def activeMQprod():
    q = random.Random()
    conn = stomp.Connection([('localhost', 61613)])
    conn.connect('admin', 'password', wait=True)
    message = 'hello from producer 1 number' + str(q.random())
    conn.send(body=message, destination='/queue/test')
    conn.disconnect()


activeMQprod()
