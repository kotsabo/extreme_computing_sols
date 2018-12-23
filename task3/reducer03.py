#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Tue Nov 14 17:11:19 2017

@author: kotsabo
"""

import sys

match = dict()

for line in sys.stdin:
    line = line.strip()
    if line != '' :
        questionId, answerId, charact = line.split()
        
        key = questionId + "-" + answerId
        if match.get(key) == None:
            match[key] = list([charact, 1, questionId])
        else:
            if charact != "-1":
                match[key] = list([charact, 2, questionId])
            else:
                charact = match[key][0]
                match[key] = list([charact, 2, questionId])

owners = dict()

for key, value in match.items():
    if value[1] == 2:
        ownerId = value[0]
        questionId = value[2]
        if owners.get(ownerId) == None:
            owners[ownerId] = list([[questionId], 1])
        else:
            questionIds = owners[ownerId][0]
            counter = owners[ownerId][1]
            owners[ownerId] = list([questionIds + [questionId], counter + 1])
            
maxim = 0
owner = None

for key, value in owners.items():
    counter = value[1]
    if counter > maxim:
        maxim = counter
        owner = list([key, value])
        
if owner != None:
    output = "{} -> ".format(owner[0])
    for qId in owner[1][0]:
        output = output + qId + ", "
    
    output = output[:-2]
    print(output)
    
    

