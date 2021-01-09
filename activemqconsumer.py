import time
import logging
import stomp



print(logging.basicConfig(level=logging.DEBUG))
logging.getLogger(name='body')


class MyListener(stomp.ConnectionListener):
    pass
    # def on_error(self, headers, message):
        # print('received an error %s' % message)

    # def onMessage(self, headers, body):
        # logging.warn(body)
        # print('received a message ...%s...' % body)


conn = stomp.Connection([('localhost', 61613)])
# mylist=MyListener()
# conn.set_listener('consumer1', mylist)
conn.connect()
conn.subscribe( destination='/queue/test',id ='MyListener' , ack='auto' )
while 1:
    time.sleep(2)
# conn.disconnect()
