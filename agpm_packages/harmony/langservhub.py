from typing import (List,Dict,Any)
from producesyntaxed import producesyntaxed

#python keywords
pykeywords = ['print', 'input', 'if', 'else:', 'def', 'try:', 'except', 'return', 'import', 'from', 'for', 'in', 'match', 'case', 'and', 'or', 'elif', 'while']
pyspecialkeywords={'print(':')','input(':')', 'if':':', 'while':':', 'except':':', 'def':'):', 'elif':':'}

#ESDLang keywords
esdkeywords = ['write', 'input', 'if', 'else', 'endif', 'function', 'endfunction', 'while', 'endwhile', 'radnom','quit']
esdspecialkeywords = {'if':4, 'endfunction':2, 'function':2, 'radnom':3}

#java key words
jvkeywords = ['System', 'public', 'if', 'else', 'public', 'static', 'while' 'void', 'class', '};', '}', 'int', 'String', 'float']
jvspecialkeywords = {'int':';', 'String':';', 'float':';', 'if':'){'}
jvexceptions= ['if','else', 'while', 'for']

#CSS key words
csskeywords=['body{', 'button{', 'button:hover{', 'input{', 'a{', 'a:hover{','p{','h1{', 'h2{', 'h3{', 'h4{', 'h5{', 'h6{', 'b{', 'i{', 'background-color:', 'background-image:', 'color:', 'border-radius:', 'borders:']
cssspecialkeywords={'background-color:':';', 'background-image:':';', 'color:':';', 'border-radius:':';', 'borders:':';'}

#Other key things
keysymbols = ['<=', '>=', '=', '!=', '+', '-', '==', '===']

#the function called when a file is syntax highlightable (categorises what languages use what method of syntax highlighting)
def highlight(extension, input_list: List[Any], tofind=...):
    global esdkeywords, pykeywords, keysymbols, esdspecialkeywords
    match extension:
        case ".esdla":
            linenum=1
            for item in input_list:
                print(str(linenum)+"|", end=' ')
                for char in item:
                    if char == ' ':
                        print(end=' ')
                    else:
                        break
                advancedsyntax(item.split(), esdspecialkeywords, esdkeywords, keysymbols, tofind)
                print()
                linenum+=1
        case ".py":
            linenum=1
            for item in input_list:
                print(str(linenum)+"|", end=' ')
                for char in item:
                    if char == ' ':
                        print(end=' ')
                    else:
                        break
                alternateadvancedsyntax(item.split(), pyspecialkeywords, pykeywords, keysymbols, tofind)
                print()
                linenum+=1
        case ".java":
            linenum=1
            for item in input_list:
                print(str(linenum)+"|", end=' ')
                for char in item:
                    if char == ' ':
                        print(end=' ')
                    else:
                        break
                alternateadvancedsyntax(item.split(), jvspecialkeywords, jvkeywords, keysymbols, tofind)
                print()
                linenum+=1
        case ".css":
            linenum=1
            for item in input_list:
                print(str(linenum)+"|", end=' ')
                for char in item:
                    if char == ' ':
                        print(end=' ')
                    else:
                        break
                alternateadvancedsyntax(item.split(), cssspecialkeywords, csskeywords, keysymbols, tofind)
                print()
                linenum+=1

#WIP autocorrect system
def autocorrect(extension, line):
    match extension:
        case ".java":
            if line.endswith(';') or line.split()[0] in jvexceptions:
                return line + '\n'
            else:
                return line + ';\n'
        case ".py":
            if line.split()[0] in pyspecialkeywords:
                if line.endswith(pyspecialkeywords[line.split()[0]]):
                    return line + '\n'
                else:
                    return line + pyspecialkeywords[line.split()[0]] + '\n'
            else:
                return line + '\n'
        case '.css':
            if line.split()[0] in cssspecialkeywords:
                if line.endswith(cssspecialkeywords[line.split()[0]]):
                    return line + '\n'
                else:
                    return line + cssspecialkeywords[line.split()[0]] + '\n'
            else:
                return line + '\n'

#Checks if a string can float (for number syntax highlighting)
def canfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


#basic syntax highlighting that highlights keywords, numbers and symbols
def syntax(input_list: List[Any], input_keywords: List[Any], input_symbols: List[Any], tofind=...):
    for item in input_list:
        if item in input_keywords:
            producesyntaxed(item, "blue", True, False)
        elif canfloat(item):
            producesyntaxed(item, "orange", True, False)
        elif item in input_symbols:
            producesyntaxed(item, "blue2", True, False)
        elif item == tofind:
            producesyntaxed(item, "yellow", True, False)
        else:
            producesyntaxed(item, "green", True, False)


#Advanced syntax highlighting that can tell errors by how long a line is
def advancedsyntax(input_list: List[Any], input_errorchances: Dict[str,Any] ,input_keywords: List[Any], input_symbols: List[Any], tofind=...):
    for item in input_list:
        if item in input_keywords:
            if item in input_errorchances:
                if len(input_list) == input_errorchances[item]:
                    producesyntaxed(item, "blue", True, False)
                else:
                    producesyntaxed(item, "red", True, False)
            else:
                producesyntaxed(item, "blue", True, False)
        elif canfloat(item):
            producesyntaxed(item, "orange", True, False)
        elif item in input_symbols:
            producesyntaxed(item, "blue2", True, False)
        elif item == tofind:
            producesyntaxed(item, "yellow", True, False)
        else:
            producesyntaxed(item, "green", True, False)


#Alternate advanced syntax highlighting that uses what the line ends with to tell errors
def alternateadvancedsyntax(input_list: List[Any], input_errorchances: Dict[str,Any] ,input_keywords: List[Any], input_symbols: List[Any], tofind=...):
    for item in input_list:
        if item in input_keywords:
            if item in input_errorchances:
                if ' '.join(input_list).endswith(input_errorchances[item]):
                    producesyntaxed(item , "blue", True, False)
                else:
                    producesyntaxed(item , "red", True, False)
            else:
                producesyntaxed(item, "blue", True, False)
        elif canfloat(item):
            producesyntaxed(item, "orange", True, False)
        elif item in input_symbols:
            producesyntaxed(item, "blue2", True, False)
        elif item == tofind:
            producesyntaxed(item, "yellow", True, False)
        else:
            producesyntaxed(item, "green", True, False)
