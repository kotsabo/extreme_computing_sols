#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Tue Nov 14 21:13:02 2017
@author: kotsabo
"""

import math
import sys

import hashlib

# we should install the library bitarray first in order to 
# import the below module -> pip install bitarray

from bitarray import bitarray
 
def hash_function(string):
    hash_object = hashlib.sha1(string.encode())
    value = int.from_bytes(hash_object.digest(), 'big')
    return value

class BloomFilter:
    
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, string):
        for i in range(self.hash_count):
            result = hash_function(str(i) + "_" + string) % self.size
            self.bit_array[result] = 1

    def lookup(self, string):
        for i in range(self.hash_count):
            result = hash_function(str(i) + "_" + string) % self.size
            if self.bit_array[result] == 0: 
                return False
        return True
        
# n number of items we will add to bloom filter (in our case n lines)
n = int(sys.argv[1])

# p false-positive probability
p = 0.01

# m size of the bloom filter
m = math.ceil(-(n * math.log(p) / (math.log(2) ** 2)))

# k number of hashes
k = math.ceil(-(math.log(p)/math.log(2)))
 
bf = BloomFilter(m, k)

for line in sys.stdin:
    line = line.strip()
    if line != "":
      if not bf.lookup(line):
          print(line)
      bf.add(line)



