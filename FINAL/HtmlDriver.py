# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:27:51 2020

Runs GetGlossaryDefinitions using terms.txt to get definitionsOutput.html

@author: eduar
"""

from GetGlossaryDefinitions import *
import time

start_time = time.time()


output = "definitionsOutput.html"

terms = importTerms("terms.txt")

definitions = getDefinitions(terms, "definitions.txt")

if exportHtml(definitions, output):
    print("Sucess! Exported as", output)
    print("--- %s seconds ---" % (time.time() - start_time))
    input("Press enter to continue...")