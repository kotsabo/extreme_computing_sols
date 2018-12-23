#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Sat Nov 18 22:10:35 2017
@author: kotsabo
"""

import sys

# N elements (in our case N queries -> N lines)
N = int(sys.argv[1])

# s threshold
s = 0.01

# e error
e = 0.001

# W Window
W = 1/e

queries_dictionary = dict()
line_counter = 0

for line in sys.stdin:
    line = line.strip()
    
    if line != "":
      if line_counter == W:
        for key in list(queries_dictionary):
            queries_dictionary[key] -= 1
            if queries_dictionary[key] == 0:
                del queries_dictionary[key]
        
        line_counter = 0
    
      if queries_dictionary.get(line) == None:
        queries_dictionary[line] = 1
      else:
        queries_dictionary[line] += 1
    
      line_counter += 1
    
for key, value in queries_dictionary.items():
    if value >= (s - e) * N:
        print(key)
    

