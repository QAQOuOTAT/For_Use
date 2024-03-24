# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:36:46 2024

@author: LAM Quincy
"""

import time
for i in range(1000):
    for char in ['   ','.', '..', '...']:
        print(f'\rLoading{char}', end='')
        time.sleep(0.5)