#Harmony editor component dev build 4
#Copyright EyeScary Development
#Uses some code from Stronge by EyeScary Development

#Imports
import os
import sys
import langservhub
import runcode
import menu
from typing import (List, Any)
import readline
from settings import checksetting

#variables
lines=[]
languageservers=[".css",".esdla",".py",".java"]
autocorrectservers=[".java", ".py", ".css"]
runnable=[".esdla", ".py", ".java"]
filename=...
extension=...

#functions

#opens the file
def openfile(filename):
    global lines
    with open(filename, "r") as file:
        lines=file.readlines()

#prints out the file and judges wether syntax highlighing is needed
def printfile(extension, tofind=...):
   global settings
   global filename
   global lines
   try:
        openfile(filename)
   except FileNotFoundError:
       print(end="")
   if extension in languageservers and checksetting(0) != False:
      langservhub.highlight(extension, lines, tofind)
   else:
      linenum=1
      for item in lines:
          print(str(linenum)+"|"+item, end="")
          linenum+=1

#calls the runcode file
def coderun(extension):
    global filename
    if extension in runnable:
        runcode.main(extension, filename)
    input("program finished, press enter to continue: ")

#deletes a line
def removeLine(linenum):
    global lines
    linenum=int(linenum)-1
    lines.pop(linenum)

#replaces a line
def replaceLine(linenum):
    global lines
    linenum-=1
    readline.set_startup_hook(lambda: readline.insert_text(lines[linenum].strip("\n")))
    try:
        user_input = input("make edits to this line: ")
    finally:
        readline.set_startup_hook()
    lines[linenum]=user_input+'\n'

#inserts a line
def insertLine(linenum, input_list: List[Any]):
    global lines
    linenum-=1
    lines.insert(linenum, ' '.join(input_list)+'\n')

#replace function
def replace(input_list: List[Any]):
    global lines
    torep=input_list[0]
    input_list.pop(0)
    for i, item in enumerate(lines):
        words = item.split()
        for j, word in enumerate(words):
            if word == torep:
                words[j] = ' '.join(input_list)
        lines[i] = ' '.join(words)+'\n'

#handles commands
def commands(input_list: List[Any]):
    global lines
    global filename
    global extension
    try:
        match input_list[1]:
            case "sf":
                write(lines, filename, extension)
                name = input("change to what file name? | ")
                if name.startswith("."):
                    filename=name
                    extension="except"
                elif "." in name:
                    extension = "." + name.split(".")[1]
                    filename = name
                else:
                    extension = input("what extension? |  ")
                    if not extension.startswith("."):
                        extension = "." + extension
                        filename = name + extension
                openfile(filename)
            case "q" | "x" | "exit":
                os.system("cls" if os.name == "nt" else "clear")
                return True
            case "dl":
                removeLine(input_list[2])
            case "edln":
                input_list.pop(0)
                input_list.pop(0)
                replaceLine(int(input_list[0]))
            case 'rp':
                input_list.pop(0)
                input_list.pop(0)
                replace(input_list)
            case "in":
                input_list.pop(0)
                input_list.pop(0)
                insertLine(int(input_list[0]), input_list)
            case "rn":
                coderun(extension)
            case "fnd":
                os.system("cls" if os.name == "nt" else "clear")
                printfile(extension, lines, input_list[2])
                input('press enter to continue: ')
    except IndexError:
        print("invalid command")
        input("press enter to continue: ")
#writes to the file
def write(filename, extension):
    global lines
    if extension in autocorrectservers:
        with open(filename, "w") as file:
            for item in lines:
                file.write(langservhub.autocorrect(extension, item.strip()))
    else:
        with open(filename, "w") as file:
            for item in lines:
                file.write(item)

#editor function
def editor():
    global filename
    global extension
    global lines
    os.system("cls" if os.name == "nt" else "clear")
    printfile(extension)
    userInput=input("|")
    if userInput.startswith(":"):
        if commands(userInput.split()):
            return True
    else:
        lines.append(userInput+'\n')
    write(filename, extension)

#main function
def main():
    global filename, extension
    if checksetting(1):
        print("here is a list of files in the current directory:")
        os.system("ls -A")
    name=input("what is the name of the file you wish to edit?: ")
    if "." in name:
        extension = "." + name.split(".")[1]
        filename = name
    else:
        extension = input("what is the extension of the file?: ")
        if not extension.startswith("."):
            extension = "." + extension
        filename = name + extension
    print(filename, extension)
    try:
        openfile(filename)
    except FileNotFoundError:
        lines=[]
    while True:
        if editor():
            break
    menu.main()

if __name__ == "__main__":
    main()
