# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 18:10:38 2021

Puts definitions into a python dictionary object

@author: eduar
"""

import json
import re

# Open glossary
with open('glossary.txt', 'r') as f:
    lines = f.readlines()

dictionary = {}

# Split terms by page number
for line in lines:
    # Cached line
    wline = ''
    for rline in lines:
        if re.search("\(p\. .+\)$", rline):
            
            # Combines lines until found a page number, writes to file
            wline = wline + ' ' + rline.rstrip()

            # Gets a key, value pair and appends to dictionary
            term = wline.split(': ', 1)
            dictionary[term[0][1:].lower()] = term[1]
                        
            #print("Wrote line: " + wline)
            
            # Clear line cache
            wline = ''
            # print("Found match!")
        else:
            wline = wline + ' ' + rline.rstrip()
            # print("No match!")
            
with open('glossary.json', 'w') as f:
    dictionary = json.dumps(dictionary)
    json.dump(dictionary, f)