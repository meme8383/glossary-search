# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 12:35:07 2020

Splits a glossary into each definition using the page number at the end of
each definition.

@author: eduar
"""

import re

# Read lines from the glossary
with open("glossary.txt", 'r') as f:
    lines = f.readlines()
    
# Write the definitions
with open("definitions.txt", 'w') as f:
    wline = ''
    for rline in lines:
        # print(re.search(r"\(p\. +\)$", rline))
        # print(rline)
        
        # Searches line for a page number at the end
        if re.search("\(p\. .+\)$", rline) or re.search("\(pp\. .+\)$", rline):
            
            # Combines lines until found a page number, writes to file
            wline = wline + ' ' + rline.rstrip()
            f.write(wline[1:] + '\n')
            print("Wrote line: " + wline)
            
            # Clear line cache
            wline = ''
            # print("Found match!")
        else:
            wline = wline + ' ' + rline.rstrip()
            # print("No match!")

# Proof of Concept
# string = "kgerdsujbnrdgu (p. 463)"
# print(re.search("\. .+\)$", string))