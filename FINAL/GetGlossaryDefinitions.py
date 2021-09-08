# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:38:55 2020

Tool for AP Psychology Flashcards

Finds terms in glossary
Allows input list of terms
Exports txt / html

@author: eduar
"""

#Search definitions for user input
def searchGlossary(inputTerm, definitionsFilePath):
    
    #Open Definitions as lines
    with open(definitionsFilePath) as f:
        lines = f.readlines()
        
    # inputTerm = input("Input a term: ")
    # print('')
    
    #Save definition if it starts with term
    matches = []
    for line in lines:
        if line.lower().startswith(inputTerm.lower()):
            matches.append(line[len(inputTerm) + 1:])
    
    #Read matches
    return matches

# Read terms, remove page numbers
def importTerms(termsFilePath):
    with open(termsFilePath, 'r') as f:
        lines = f.readlines()
    for n, line in enumerate(lines):
        lines[n] = line.split(',')[0].replace(' - ', '-')
    return lines

# Output dictionary of {term : definition}
def getDefinitions(terms, definitionsFilePath):
    definitions = {}
    for term in terms:
        definitions[term] = searchGlossary(term.rstrip(), definitionsFilePath)
    return definitions
                
# Exports a txt of definitions
def exportTxt(definitions, outputFilePath): 
    with open(outputFilePath, 'w') as f:
        noDefinition = []
        
        # Format:
        # term
        # definition
        #
        for term in definitions:
            if len(definitions[term]) > 0:
                f.write(term + "\n" + definitions[term][0] + "\n")
            else:
                noDefinition.append(term)
                
        # Add list of terms without definitions at the end
        if len(noDefinition) > 0:
            f.write("No definition found for term(s):\n" + ''.join([i + '\n' for i in noDefinition]))
    return True

# Writes definitions in HTML format
def exportHtml(definitions, outputFilePath):
    with open(outputFilePath, 'w') as f:
        f.write(r'<!DOCTYPE html>')
        f.write(r'<html lang="en" dir="ltr">')
        f.write(r'    <head>')
        f.write(r'        <meta charset="utf-8">')
        f.write(r'        <title>Flashcard Definitions</title>')
        f.write(r'    </head>')
        f.write(r'    <body>')
        
        noDefinition = []
        
        # Format: <p>term<br>definition</p>
        for term in definitions:
            if len(definitions[term]) > 0:
                f.write(r"<p>{}<br>{}</p>".format(term, definitions[term][0]))
            else:
                noDefinition.append(term)
                
        # Add a list of terms without definitions at the end
        if len(noDefinition) > 0:
            f.write(r"<p><br></p>")
            f.write(r"<p>No definition found for term(s):</p>")
            f.write(r"<ul>")
            for term in noDefinition:
                f.write(r"<li>" + term.rstrip())
            f.write(r"</ul>")
        
        f.write(r'    </body>')
        f.write(r'</html>')
    return True