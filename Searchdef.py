# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 13:12:17 2020

Searches definitions.txt for the definition input by the user

@author: eduar
"""


#Search definitions for user input
def searchGlossary(userInputTerm):
    
    #Open Definitions as lines
    with open("definitions.txt") as f:
        lines = f.readlines()
        
    # userInputTerm = input("Input a term: ")
    # print('')
    
    #Save definition if it starts with term
    matches = []
    for line in lines:
        if line.lower().startswith(userInputTerm.lower()):
            matches.append(line[len(userInputTerm) + 1:])
    
    #Read matches
    return matches