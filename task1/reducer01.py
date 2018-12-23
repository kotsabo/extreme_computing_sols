#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Mon Nov 13 23:21:09 2017
@author: kotsabo
"""

import sys

word, new_word = None, None
filename, new_filename = None, None
key, count = None, None

files = []
count_files = 1
count_infile = 0

for line in sys.stdin:
    line = line.strip()
    key, count = line.split('\t')
    count = int(count)
    new_word, new_filename = key.split()
    
    if new_word != word and word != None:
        files.append((filename, count_infile))
        output = "{0} : {1} : ".format(word, count_files) + "{"
        for file_o in files:
            output = output + "({0}, {1}), ".format(file_o[0], file_o[1])
            output = output[:-2] + "}"
        print(output)
        files = []
        count_files = 1
            count_infile = 1
        else:
            
            if new_filename != filename and filename != None:
                count_files += count
                files.append((filename, count_infile))
                count_infile = 1
            else:
                count_infile += count

word = new_word
    filename = new_filename

if word != None:
    output = "{0} : {1} : ".format(word, count_files) + "{" + "({}, 1)".format(filename) + "}"
    print(output)
    
    
    
