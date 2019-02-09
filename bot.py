#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

# Discord Bot for making accounts

import os
import csv
import sys
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

#file = #CSV thing
#    username = row[0]
#    password = row[1]
#    email = row[2]

time.sleep(0.5)
keyboard.press(Key.cmd)
keyboard.release(Key.cmd)
time.sleep(0.5)
for chrome in "Chrome":
    keyboard.press(chrome)
    keyboard.release(chrome)
    time.sleep(0.12)
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
