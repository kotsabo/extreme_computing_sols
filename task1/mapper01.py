#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Created on Wed Nov  8 19:03:06 2017
    @author: kotsabo
    """

import os
import sys

for line in sys.stdin:
    line = line.strip()
    if line != '':
        tokens = line.split()
        path = os.environ["mapreduce_map_input_file"]
        filename = path.split('/')[-1]
        for token in tokens:
            print("{0} {1}\t1".format(token, filename))


    
