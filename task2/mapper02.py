#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Tue Nov 14 16:52:08 2017

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
            counter = root.get('ViewCount')
            questionId = root.get('Id')

            print("{0}.{1}".format(counter, questionId))
