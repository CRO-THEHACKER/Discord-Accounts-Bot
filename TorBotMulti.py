#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

# Discord Bot for making accounts

import os
import sys
import time

botstomake = input('How meny bots do you want to start [1-10]: ')
while True:
    if botstomake == '1':
        os.system('torbot/torbot1.py')
    elif botstomake == '2':
        os.system('torbot/torbot2.py')
    elif botstomake == '3':
        os.system('torbot/torbot3.py')
    elif botstomake == '4':
        os.system('torbot/torbot4.py')
    elif botstomake == '5':
        os.system('torbot/torbot5.py')
    elif botstomake == '6':
        os.system('torbot/torbot6.py')
    elif botstomake == '7':
        os.system('torbot/torbot7.py')
    elif botstomake == '8':
        os.system('torbot/torbot8.py')
    elif botstomake == '9':
        os.system('torbot/torbot9.py')
    elif botstomake == '10':
        os.system('torbot/torbot10.py')
    else:
        pass