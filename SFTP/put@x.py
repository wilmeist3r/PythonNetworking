import pysftp
import schedule
import time
import os


def putSFTP():

    with pysftp.Connection(host = "host", username = "sftp_user", password = "sftp_passwd") as sftp:

        print("Connection succesfully stablished ... \n")
        sftp.cwd('rem_dir')
        local_dir = "/Users/juanbetancourt/Desktop/mtouch"

        n = 0

        for file in os.listdir(local_dir):

            sftp.put(file, preserve_mtime = True)
            print("File ", file, " succesfully uploaded.\n")

            n = n + 1


schedule.every().day.at("xx:xx").do(putSFTP)

while True:
    schedule.run_pending()
    time.sleep(1)
