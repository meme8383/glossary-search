# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 13:12:17 2020

Searches definitions.txt for the definition input by the user

@author: eduar
"""

import os

#Search definitions for user input
def searchGlossary():
    print('')
    while True:
        #Set path
        __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
        
        #Open Definitions as lines
        with open(os.path.join(__location__, 'definitions.txt')) as f:
            lines = f.readlines()
        
        userInputTerm = input("Input a term: ")
        print('')
        
        #Save definition if it starts with term
        matches = []
        for line in lines:
            if line.lower().startswith(userInputTerm.lower()):
                matches.append(line)
        
        #Read matches
        if len(matches) == 1:
            print(matches[0])
        elif 4 > len(matches) > 1:
            print("Found " + str(len(matches)) + " matches!\n")
            for match in matches:
                print(match)
        elif matches:
            print("Found " + str(len(matches)) + " matches! Check your spelling.")
        else:
            print("No definitions found! Check your spelling.")
        
        
            


if __name__ == "__main__":
    searchGlossary()