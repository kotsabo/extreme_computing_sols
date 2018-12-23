#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Sun Nov 19 18:12:45 2017
@author: kotsabo
"""

import sys
import math

# we should install the library bitarray first in order to
# import the below module -> pip install bitarray

from bitarray import bitarray

class BloomFilter:

    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, index):
        self.bit_array[index] = 1

# n number of items we will add to bloom filter (in our case n lines)
n = 1897987 #int(sys.argv[1])

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
        bf.add(int(line))

output = ""
for bit in bf.bit_array:
    output += str(int(bit))

print(output)

