# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:00:49 2020

Runs GetGlossaryDefinitions using terms.txt to get definitionsOutput.txt

@author: eduar
"""

from GetGlossaryDefinitions import *
import time

start_time = time.time()


output = "definitionsOutput.txt"

terms = importTerms("terms.txt")

definitions = getDefinitions(terms, "definitions.txt")

if exportTxt(definitions, output):
    print("Sucess! Exported as", output)
    print("--- %s seconds ---" % (time.time() - start_time))
    input("Press enter to continue...")