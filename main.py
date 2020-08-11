#Python Basic Auto Clicker Open Source V0.1
#by Avegly
#This code is free for any use.

#Avegly Website: https://avegly.weebly.com/
#Avegly GitHub: https://github.com/Avegly

import pyautogui #pip install PyAutoGUI
import keyboard  #pip install keyboard
import time, sys


def start_clicks():
    print("Press F7 for exit, Press F8 for stop.")
    while True:
        if keyboard.is_pressed("F7"):
            print("exit")
            sys.exit()
        elif keyboard.is_pressed("F8"):
            print("stop")
            start()
            break
        #click line
        pyautogui.click()
        
        time.sleep(0.0)


def start():
    print("Press ` for start, Press F7 for exit.")
    while True:
        time.sleep(0.1)
        if keyboard.is_pressed("`"):
            print("Start")
            start_clicks()
        elif keyboard.is_pressed("F7"):
            print("exit")
            sys.exit()
start()

