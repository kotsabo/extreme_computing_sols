#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Sun Nov 19 18:12:45 2017
@author: kotsabo
"""

import sys
import math
import hashlib

def hash_function(string):
    hash_object = hashlib.sha1(string.encode())
    value = int.from_bytes(hash_object.digest(), 'big')
    return value

# n number of items we will add to bloom filter (in our case n lines)
n = 1897987 #int(sys.argv[1])

# p false-positive probability
p = 0.01

# m size of the bloom filter
m = math.ceil(-(n * math.log(p) / (math.log(2) ** 2)))

# k number of hashes
k = math.ceil(-(math.log(p)/math.log(2)))

for line in sys.stdin:
    line = line.strip()

    if line != "":
       for i in range(k):
          index = hash_function(str(i) + "_" + line) % m
          print(index)

          