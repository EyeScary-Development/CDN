from typing import (List,Dict,Any)
from producesyntaxed import producesyntaxed
import os
import json
from settings import checksetting

#Other key things
keysymbols = ['<=', '>=', '=', '!=', '+', '-', '==', '===']
keywords={}

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "keywords.json")

with open(file_path, "r") as f:
    keywords = json.load(f)


#the function called when a file is syntax highlightable (categorises what languages use what method of syntax highlighting)
def highlight(extension, input_list: List[Any], tofind=...):
    global keywords, keysymbols
    linenum=1
    if extension in keywords and checksetting(0)!=False:
        match keywords[extension]["level"]:
            case "standard":
                for item in input_list:
                   print(f'{str(linenum)}|', end="")
                   syntax(item, extension, tofind)
                   print()
                   linenum+=1
            case "semiadvanced":
                for item in input_list:
                    print(f'{str(linenum)}|', end="")
                    semiadvancedsyntax(item, extension, tofind)
                    print()
                    linenum+=1
            case "advanced":
                for item in input_list:
                    print(f'{str(linenum)}|', end="")
                    advancedsyntax(item, extension, tofind)
                    print()
                    linenum+=1
    else:
        for item in input_list:
            print(str(linenum)+"|"+item, end="")
            linenum+=1

#Checks if a string can float (for number syntax highlighting)
def canfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


#basic syntax highlighting that highlights keywords, numbers and symbols
def syntax(line,extension, tofind=...):
    global keysymbols, keywords
    for item in line.split():
        if item in keywords[extension]["keywords"]:
            producesyntaxed(item, "blue", True, False)
        elif canfloat(item):
            producesyntaxed(item, "orange", True, False)
        elif item in keysymbols:
            producesyntaxed(item, "blue2", True, False)
        elif item == tofind:
            producesyntaxed(item, "yellow", True, False)
        else:
            producesyntaxed(item, "green", True, False)


#Advanced syntax highlighting that can tell errors by how long a line is
def semiadvancedsyntax(line, extension, tofind=...):
    global keysymbols, keywords
    for item in line.split():
        if item in keywords[extension]["keywords"]:
            if item in keywords[extension]["special_keywords"]:
                if len(line.split()) == keywords[extension]["special_keywords"][item]:
                    producesyntaxed(item, "blue", True, False)
                else:
                    producesyntaxed(item, "red", True, False)
            else:
                producesyntaxed(item, "blue", True, False)
        elif canfloat(item):
            producesyntaxed(item, "orange", True, False)
        elif item in keysymbols:
            producesyntaxed(item, "blue2", True, False)
        elif item == tofind:
            producesyntaxed(item, "yellow", True, False)
        else:
            producesyntaxed(item, "green", True, False)


#Alternate advanced syntax highlighting that uses what the line ends with to tell errors
def advancedsyntax(line,extension, tofind=...):
    global keysymbols, keywords
    for item in line.split():
        if item in keywords[extension]["keywords"]:
            if item in keywords[extension]["special_keywords"]:
                if line.rstrip().endswith(keywords[extension]["special_keywords"][item]):
                    producesyntaxed(item , "blue", True, False)
                else:
                    producesyntaxed(item , "red", True, False)
            else:
                producesyntaxed(item, "blue", True, False)
        elif canfloat(item):
            producesyntaxed(item, "orange", True, False)
        elif item in keysymbols:
            producesyntaxed(item, "blue2", True, False)
        elif item == tofind:
            producesyntaxed(item, "yellow", True, False)
        else:
            producesyntaxed(item, "green", True, False)
