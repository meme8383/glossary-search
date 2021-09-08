# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 18:52:20 2021

Searches glossary for term

@author: eduar
"""

import json

with open('terms.txt', 'r', encoding='utf-8') as f:
    termsLines = f.readlines()

terms = []
for i in range(len(termsLines)):
    if not termsLines[i].rstrip() == '':
        terms.append(termsLines[i].rstrip()[:-1])
        
        
with open('glossary.json') as f:
    jsondict = json.load(f)
    glossary = json.loads(jsondict)
    

name = input("Name of output file: ") + '.txt'

with open(name, 'w') as output:
    misses = []
    for term in terms:
        try:
            output.write(term + ': ' + glossary[term.lower()] + '\n\n')
        except KeyError:
            misses.append(term)
    output.write("Missing terms:\n")
    for term in misses:
        output.write(term + '\n')
