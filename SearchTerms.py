# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:49:00 2020

Runs a terms file through the Glossary Searcher

@author: eduar
"""

from Searchdef import *

# Read terms
with open("terms.txt", 'r') as f:
    lines = f.readlines()
    
# Output first definition, check if none found
with open("DefinitionOutput.txt", 'w') as f:
    for line in lines:
        matches = searchGlossary(line.rstrip())
        if len(matches) > 0:
            f.write(line + matches[0] + "\n")
        else:
            print("Could not find definition for term: " + line)