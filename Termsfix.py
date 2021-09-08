# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:42:56 2020

Removes page number from terms list

@author: eduar
"""

# Read file
with open("terms.txt", 'r') as f:
    lines = f.readlines()
    
# Delete part after comma
with open("terms.txt", 'w') as f:
    for line in lines:
        f.write(line.split(',')[0] + "\n")