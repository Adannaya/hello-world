# Make sure periodic.txt is in the same directory as spambot.py

from os import system as s
s("pip install pyautogui")

import pyautogui, time

time.sleep(5)
spamtext = open("periodic.txt", "r")
for line in spamtext:
  pyautogui.typewrite(line)
  pyautogui.press("enter")
pyautogui.typewrite("Now you have no excuse for failing Chemistry.")
pyautogui.press("enter")
spamtext.close()
