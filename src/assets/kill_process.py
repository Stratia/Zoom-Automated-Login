import subprocess
import json
import pyautogui

try:
    json_file = open('assets\PID.json')
    json_file_data = json.load(json_file)
    pid = json_file_data['PID']
    subprocess.Popen('taskkill /F /PID {0}'.format(pid), shell=True)
except:
    pyautogui.alert('Error when killing Zoom.pyw')
