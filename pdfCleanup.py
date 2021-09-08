# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 14:48:57 2020

Fix pdf conversion

@author: eduar
"""

# Read glossary
with open("glossary.txt", 'r') as f:
    lines = f.readlines()
    
# Remove headers/footers
with open("newglossary.txt", 'w') as f:
    for line in lines:
        print(line)
        if not line.startswith("Glossary") and not line.startswith("G-"):
            f.write(line)