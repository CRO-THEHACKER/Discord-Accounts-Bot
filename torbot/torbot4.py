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
username2 = input('Username: ')
email2 = input('Email: ')
password2 = input('Password: ')
username3 = input('Username: ')
email3 = input('Email: ')
password3 = input('Password: ')
username4 = input('Username: ')
email4 = input('Email: ')
password4 = input('Password: ')

time.sleep(0.5)
input('Open the tor broser now... (please be in the search line)')
time.sleep(5)

def open4times():

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

for number in range(4):
    open4times()

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

keyboard.press(Key.ctrl)
keyboard.press(Key.tab)
keyboard.release(Key.ctrl)
keyboard.release(Key.tab)
time.sleep(2)

for email2 in email2:
    keyboard.press(email2)
    keyboard.release(email2)
    time.sleep(0.12)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
for username2 in username2:
    keyboard.press(username2)
    keyboard.release(username2)
    time.sleep(0.12)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
for password2 in password2:
    keyboard.press(password2)
    keyboard.release(password2)
    time.sleep(0.12)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

keyboard.press(Key.ctrl)
keyboard.press(Key.tab)
keyboard.release(Key.ctrl)
keyboard.release(Key.tab)
time.sleep(2)

for email3 in email3:
    keyboard.press(email3)
    keyboard.release(email3)
    time.sleep(0.12)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
for username3 in username3:
    keyboard.press(username3)
    keyboard.release(username3)
    time.sleep(0.12)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
for password3 in password3:
    keyboard.press(password3)
    keyboard.release(password3)
    time.sleep(0.12)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

keyboard.press(Key.ctrl)
keyboard.press(Key.tab)
keyboard.release(Key.ctrl)
keyboard.release(Key.tab)
time.sleep(2)

for email4 in email4:
    keyboard.press(email4)
    keyboard.release(email4)
    time.sleep(0.12)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
for username4 in username4:
    keyboard.press(username4)
    keyboard.release(username4)
    time.sleep(0.12)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
for password4 in password4:
    keyboard.press(password4)
    keyboard.release(password4)
    time.sleep(0.12)
keyboard.press(Key.enter)
keyboard.release(Key.enter)