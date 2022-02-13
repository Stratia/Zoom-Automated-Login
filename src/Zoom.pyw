from pynotifier import Notification
from datetime import datetime
import subprocess
import pyautogui
import psutil
import time
import json
import csv
import os
# Todo: Fix everything for the love of god

"""
For logging PID for kill_process.py to ensure Zoom.pyw 
program gets destroyed
"""

try:
    json_file = open('assets\PID.json')
    iden = os.getpid()
    with open('assets\config.json', "w") as b:
        dic = {"PID": iden}
        json.dump(dic, b)
except:
    pyautogui.alert('Error when loading PID.json')

date = datetime.now()
day_now = date.strftime('%A')
hour_now = date.strftime('%I')
minute_now = date.strftime('%M')
PM_AM_now = date.strftime('%p').lower()

Notification(title='Zoom Auto Login',description='Script will activate upon designated csv_time',
             icon_path='assets\pl.ico',duration=8).send()

for index in (hour_now):
    new_hour = []
    if index == '0':
        pass
    else:
        new_hour.append(index)

def kill_zoom():
    process_name = "Zoom"
    pid = None
    for proc in psutil.process_iter():
        if process_name in proc.name():
            pid = proc.pid
            subprocess.Popen('taskkill /F /PID {0}'.format(pid), shell=True)
    get_time()

def auto_login():

    """
    Finds location of buttons and outputs pixels for
    mouse to click
    """
    list = os.path.expanduser(r'~\AppData\Roaming\Zoom\bin\Zoom.exe')
    subprocess.Popen(list)
    time.sleep(10)

    join_button_locate =  pyautogui.locateOnScreen(r'button\Buttobn.png')

    buttonx, buttony = pyautogui.center(join_button_locate)
    pyautogui.click(buttonx, buttony)

    time.sleep(1)
    pyautogui.write('Testtt')
    time.sleep(1)

    audioB = pyautogui.locateOnScreen(r'button\audio.png')
    buttonx2, buttony2 = pyautogui.center(audioB)
    pyautogui.click(buttonx2, buttony2)

    VideoB = pyautogui.locateOnScreen(r'button\Video.png')
    buttonx3, buttony3 = pyautogui.center(VideoB)
    pyautogui.click(buttonx3, buttony3)

    join_button_locate4 = pyautogui.locateOnScreen(r'button\JoinB.png')
    buttonx3, buttony3 = pyautogui.center(join_button_locate4)
    pyautogui.click(buttonx3, buttony3)
    print('SiongCum1')
    time.sleep(10)
    if end_PM_AM == None:
        get_time()
    else:
        end_check()

def get_time():
    """
    Get current values from csv file
    """
    global csv_time, am_pm, meeting_id, set_minute, set_hour, end_time, end_set_minute, end_set_hour, end_PM_AM
    while True:
        with open('ZoomDates.csv', 'r') as file:
            # Opens CSV
            reader = csv.DictReader(file)
            for item in reader:
                csv_time = item['Time']
                am_pm = item['AM-PM'].lower()
                meeting_id = item["Meeting ID"]
                end_time = item['End Time']
                end_PM_AM = item['PM-AM']
                try:
                    parse1 = (list(map(str, end_time)))
                    n1 = parse1[-1]
                    n2 = parse1[-2]
                    n3 = parse1[0]
                    n4 = parse1[1]
                    end_new_minute = []
                    end_new_hour = []
                    end_new_minute.append(n2)
                    end_new_minute.append(n1)

                    end_new_hour.append(n3)
                    end_new_hour.append(n4)

                    end_set_minute = "".join(end_new_minute)
                    end_set_hour = "".join(end_new_hour)
                    print(end_set_hour)

                    parse2 = (list(map(str, csv_time)))
                    p1 = parse2[-1]
                    p2 = parse2[-2]
                    p3 = parse2[0]
                    p4 = parse2[1]
                    new_minute = []
                    new_hour = []

                    new_minute.append(p2)
                    new_minute.append(p1)
                    new_hour.append(p3)
                    new_hour.append(p4)
                    set_minute = "".join(new_minute)
                    set_hour = "".join(new_hour)
                    date = datetime.now()
                    hour_now = date.strftime('%I')
                    minute_now = date.strftime('%M')
                    PM_AM_now = date.strftime('%p').lower()
                    print(PM_AM_now)
                    print(csv_time)
                    if (set_hour == hour_now) and (am_pm.lower() == PM_AM_now.lower()) and (set_minute == minute_now):
                        # Checs if the inputted csv_time aligns with the current csv_time.
                        auto_login()

                    if (set_hour == None) or (am_pm == None) or (set_minute == None) or (meeting_id == None):
                        pyautogui.alert("Warning: One of the CSV values doens't have a value.\n"
                                        "Quitting program")
                        break
                except:
                    pyautogui.alert('Error: Please input values in CSV')
                    quit()

    # Todo: Fix this messy mess of code, doesn't look right

def end_check():
    while True:
        with open('ZoomDates.csv', 'r') as file:
            # Opens CSV
            reader = csv.DictReader(file)
            for item in reader:
                end_time = item['End Time']
                end_PM_AM = item['PM-AM']
                date2 = datetime.now()
                hour_now2 = date2.strftime('%I')
                minute_now2 = date2.strftime('%M')

                PM_AM_now2 = date2.strftime('%p').lower()
                if (end_set_hour == hour_now2) and (end_set_minute == minute_now2) and (
                        end_PM_AM.lower() == PM_AM_now2.lower()):
                    kill_zoom()
try:
    """
    Checks if CSV file already exists  and if not will create one
    If so will activate date_check function
    """
    for i in os.listdir():
        if i == 'ZoomDates.csv':
            get_time()
    with open('ZoomDates.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Time', 'AM-PM', 'Meeting ID', 'End Time', "PM-AM"])
        csv_writer.writerows([['', 'PM', '3131331944', '01:10']])
    get_time()
except:
    quit()