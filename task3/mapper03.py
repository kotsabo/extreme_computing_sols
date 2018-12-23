#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Tue Nov 14 17:02:02 2017
@author: kotsabo
"""

from enum import Enum
import sys
import xml.etree.ElementTree as ET

class PostType(Enum):
    Question = "1"
    Answer = "2"
    Other = "-1"

for line in sys.stdin:
    line = line.strip()
    if line != '':
        root = ET.fromstring(line)
        postTypeId = root.get('PostTypeId')

        if postTypeId == PostType.Question.value:
            questionId = root.get('Id')
            answerId = root.get('AcceptedAnswerId')
            if questionId != None and answerId != None:
                print("{0} {1} -1".format(questionId, answerId))
        elif postTypeId == PostType.Answer.value:
            questionId = root.get('ParentId')
            answerId = root.get('Id')
            ownerUserId = root.get('OwnerUserId')      
            if questionId != None and answerId != None and ownerUserId != None:
                print("{0} {1} {2}".format(questionId, answerId, ownerUserId))

            
