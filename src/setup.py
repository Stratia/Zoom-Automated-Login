import os
import csv

try:
    """
    Install packages if user hasn't already installed them
    """
    os.system('py -m pip install PyAutoGUI')
    os.system('py -m pip install py-notifier')
    os.system('py -m pip install psutil')
except:
    pass

with open('ZoomDates.csv', 'w', newline='') as csvfile:
    """
    Creates CSV
    """
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Time', 'AM-PM', 'ID','Passcode','End Time','PM-AM'])
    csv_writer.writerows([['04:46', 'PM', '3131331944','Passocfe4dd','04:47','PM']])
    csv_writer.writerows([['04:48', 'PM', '3131331944','Passocfe4dd', '04:49', 'PM']])
