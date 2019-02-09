#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

# Discord Bot for making accounts

import os
import csv
import sys
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

f = open('config.csv')
csv_f = csv.reader(f)
for row in csv_f:
    username = row[0]
    password = row[1]
    email = row[2]

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
time.sleep(25)
keyboard.press(Key.ctrl)
keyboard.press('t')
keyboard.release(Key.ctrl)
keyboard.release('t')
for discordurl in "https://discordapp.com/register":
    keyboard.press(discordurl)
    keyboard.release(discordurl)
    time.sleep(0.12)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(4)
for email in email:
    keyboard.press(email)
    keyboard.release(email)
    time.sleep(0.12)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
for username in username:
    keyboard.press(username)
    keyboard.release(username)
    time.sleep(0.12)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
for password in password:
    keyboard.press(password)
    keyboard.release(password)
    time.sleep(0.12)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
