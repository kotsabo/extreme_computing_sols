#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Tue Nov 14 16:51:42 2017
@author: kotsabo
"""

import sys

total = 0

for line in sys.stdin:
    line = line.strip()
    if line != '':
       counter, questionId = line.split('.')

       if total < 10:
           total += 1
           print("{0} {1}".format(counter, questionId))
