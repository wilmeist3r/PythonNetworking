import pysftp
import schedule
import time
from datetime import datetime, timedelta



def getSFTP():

    with pysftp.Connection(host = "host", username = "sftp_user", password = "sftp_passwd") as sftp:

        print("Connection succesfully stablished ... \n")
        sftp.cwd('rem_dir')
        remote_dir = sftp.listdir_attr()
        
        n = 0

        for file in remote_dir:

            hTime = file.st_mtime
            mTime = datetime.utcfromtimestamp(hTime)
            tTime = datetime.today()
            cTime = tTime.replace(day = tTime.day, hour = 0, minute = 0, second = 0, microsecond = 0)

            if (cTime - mTime) <= timedelta(hours = 24):

                sftp.get(remote_dir[n].filename, preserve_mtime = True)

                print("File ", file.filename, " was last modified on ", mTime)
                print("File ", file.filename, " succesfully copied.\n")

            n = n + 1



schedule.every().day.at("xx:xx").do(getSFTP)

while True:

    schedule.run_pending()
    time.sleep(1)
