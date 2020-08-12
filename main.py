#Python Basic Auto Clicker Open Source
#by Avegly
#This code is free for any use.

#Avegly Website: https://avegly.weebly.com/
#Avegly GitHub: https://github.com/Avegly

import pyautogui #pip install PyAutoGUI
import keyboard  #pip install keyboard
import time, sys


def start_clicks():
    print("Press",exitButton," for exit, Press",stopButton," for stop.")
    while True:
        if keyboard.is_pressed(exitButton):
            print("exit")
            sys.exit()
        elif keyboard.is_pressed(stopButton):
            print("stop")
            start()
            break
        #click line
        pyautogui.click()
        
        time.sleep(sleepTime)


def start():
    print("Press",startButton," for start, Press",exitButton," for exit.")
    while True:
        time.sleep(0.1)
        if keyboard.is_pressed(startButton):
            print("Start")
            start_clicks()
        elif keyboard.is_pressed(exitButton):
            print("exit")
            sys.exit()

sleepTime = 0.2
startButton = "`"
stopButton = "F7"
exitButton = "F8"

start()


