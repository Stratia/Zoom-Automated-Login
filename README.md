
<p align="center">
  <img width=50% src="Zoom.jpg" alt="Material Bread logo">
</p>


## **Zoom Automation**
This program automatically logs you into a Zoom session at your alloted time. Optionally you can choose to have end the session at your allotted time.

## **How To Use**
• Run setup.py to automatically install the required modules and to create CSV. Alternatively you 
  can manually install modules using requirements.txt
  
  • Enter values into csv file, be absolutely sure to enter data into Time/End Time rows as formatted:
 05:30, 08:10 or 10:00, 12:12
 
  • Run Zoom.py and wait untill alloted time.
  
  • Once your done be sure to run kill_process.py (In assets) to ensure it doesn't run in the background when your
 done with it.
 
  Note: Be sure to activate windows notifcations for script start popup (Optional)

## **Recomended before use**

• It is reccomended to run screener.py and crop them yourself, for pictures 
of indivdual buttons. Look at buttons folder for reference, Additionally be sure
 to keep the same name for the images your replace.
 
• It's reccomended to use screener.py since the button images may not 
  work for your screen size due to need for PyAutoGUi's imaging to be pixel perfect
  Abeit this can get cumbersome so do this if your sure you need to

Todo
```
- Activate Script on Start-up
- Optimize
```

