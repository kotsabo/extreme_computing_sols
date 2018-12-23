#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Nov 14 18:53:10 2017

@author: kotsabo
"""

import random
import sys

k = 100
reservoir = []
counter = 0

for line in sys.stdin:
    line = line.strip()
    
    if line != '' :
        if counter < k :
            reservoir.append(line)
        else:
            m = random.randint(0, k)
            if m < k :
                reservoir[m] = line

    counter += 1

for line in reservoir:
    print(line)

