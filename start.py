#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

import os
import sys
import time

install = input('Would you like to install the programs for the bot? [Y/n]: ')
if install == 'Y':
    os.system('python3 install.py')
if install == 'n':
    pass

print('''
[1]:    Run bot with tor [make more then 4 an hour]
[2]:    Run bot with chrome [4 bots an hour]
[3]:    Install bot repos [do this onece]
[4]:    Exit''')

while True:
    choice = input('DiscordBot> ')
    if choice == '1':
        os.system('python3 TorBotMulti.py')
    if choice == '2':
        os.system('python3 bot.py')
    if choice == '3':
        os.system('python3 install.py')
    if choice == '4':
        os.system('exit')