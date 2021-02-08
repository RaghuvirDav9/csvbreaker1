#this function creates a file and dumps data as specified, here 3gb

from datetime import timedelta, date, datetime
import string
import random
import time
import os

f = open("s3Demo.txt", "w+")
f.write(
    "index     |  cur_date       |  char      |  char_varying   |  small_int |  integer        |  big_int             "
    "|  text_demo\n")
size = os.path.getsize("s3Demo.txt")
start_time = time.time()
index = 0
start_date = datetime.strptime("01-01-1970", "%d-%m-%Y")
end_date = datetime.strptime("01-01-2021", "%d-%m-%Y")
while size < 3221225472:
    for i in range((end_date - start_date).days):
        index = index + 1
        curr_date = start_date + timedelta(i)
        char = ''.join(random.choices(string.ascii_letters, k=5))
        char_varying = ''.join(random.choices(string.ascii_letters, k=10))
        small_int = ''.join(random.choices(string.digits, k=4))
        integer = ''.join(random.choices(string.digits, k=9))
        big_int = ''.join(random.choices(string.digits, k=18))
        text = ''.join(random.choices(string.ascii_letters, k=25))
        f.write("%-10s|  %-15s|  %-10s|  %-15s|  %-10s|  %-15s|  %-20s|  %s \n" % (
        index, curr_date.date(), char, char_varying, small_int, integer, big_int, text))
    size=os.path.getsize("s3Demo.txt")
    print(size)
f.close()


