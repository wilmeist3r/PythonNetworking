import pysftp
import sys
from apscheduler.schedulers.blocking import BlockingScheduler


def sftp_process():
    with pysftp.Connection(host = "host", username = "sftp_user", password = "sftp_passwd") as sftp:
        print("Connection succesfully stablished ... ")
        sftp.cwd('rem_dir')
        directory_structure = sftp.listdir_attr()

        n = 0     
        for attr in directory_structure:
            sftp.get(directory_structure[n].filename, preserve_mtime = True)
            print ("File ", attr.filename, " succesfully copied.")

            sftp.unlink(directory_structure[n].filename)
            print ("File ", attr.filename, " succesfully deleted.")
            n = n + 1


repeat = BlockingScheduler()
repeat.add_job(sftp_process, "interval", minutes = x)
repeat.start()
