#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

# Discord Bot for making accounts

import os
import csv
import sys
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

username = input('Username: ')
email = input('Email: ')
password = input('Password: ')

time.sleep(0.5)
keyboard.press(Key.cmd)
keyboard.release(Key.cmd)
time.sleep(0.5)
for tor in "Tor":
    keyboard.press(tor)
    keyboard.release(tor)
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