# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 14:48:57 2020

Fix pdf conversion

@author: eduar
"""

# Read glossary
with open("glossary.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
# Remove headers/footers
with open("glossary.txt", 'w') as f:
    for line in lines:
        if "glossary" not in line.strip("\n").lower() and "myers" not in line.strip("\n").lower():
            f.write(line)