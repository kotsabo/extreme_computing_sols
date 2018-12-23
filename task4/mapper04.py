#!/usr/bin/env python

import sys
import random

line_number = 0

for line in sys.stdin:
    line = line.strip()
    
    if line != "":
        if random.randint(0, line_number) == 0:
            resevoir = line

line_number += 1

if line_number != 0:
    print(resevoir)
