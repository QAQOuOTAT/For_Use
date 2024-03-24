# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:40:52 2024

@author: LAM Quincy
"""

emoji=['o7','o/']
import time
for i in range(1000):
    for char in emoji:
        print(f'\r{char}', end='')
        time.sleep(1)