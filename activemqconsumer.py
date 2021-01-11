import time
import logging
import stomp


# This function connects to activemq using stomp and receives messages
def activeMQconsumer():
    print(logging.basicConfig(level=logging.DEBUG))
    conn = stomp.Connection([('localhost', 61613)])
    conn.connect()
    conn.subscribe(destination='/queue/test', id='MyListener', ack='auto')
    while 1:
        time.sleep(2)


activeMQconsumer()
