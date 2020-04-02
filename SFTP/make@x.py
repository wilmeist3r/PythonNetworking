import touch as t
import schedule
import time

def mtouch():

    for i in range(1, 99):
        t.touch("dir_patht%s" % i)


schedule.every().day.at("xx:xx").do(mtouch)

while True:
    schedule.run_pending()
    time.sleep(1)
