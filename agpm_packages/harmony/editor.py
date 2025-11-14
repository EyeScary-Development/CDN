#Harmony editor component version 0.5
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
from consts import PLATFORM
import time
from pathlib import Path
from settings import checksetting
import term

#variables
lines=[]
runnable=[".esdla", ".py", ".java"]
filename=...
extension=...

#functions

#checks if it's a markdown file and asks if you want to open it in Cobblestone
def openinc():
    print("This file is a markdown file and can be opened in Cobblestone (a dedicated notes app built from Harmony), would you like to open Cobblestone?")
    usin = input("|| ")
    if usin == "y":
        if (Path.home() / '.agpm' / 'cobblestone' / 'menu.py').exists():
            print("Cobblestone installed, proceeding...")
            os.system("python3 ~/.agpm/cobblestone/menu.py")
        else:
            print("Cobblestone not installed, you can install through AGPM")
            time.sleep(1)
            return
    else:
        return

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
   langservhub.highlight(extension,lines,tofind) 

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
    input_list.pop(0)
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
def commands(userInput: str):
    global lines
    global filename
    global extension
    command = userInput.split()[0]
    try:
        match command:
            case ":sf":
                write(lines, filename, extension)
                name = input("change to which file name? | ")
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
            case ":q" | ":x" | ":exit":
                os.system("cls" if os.name == "nt" else "clear")
                return True
            case ":rm":
                removeLine(userInput.split()[1])
            case ":rw":
                listtoinput=userInput.split()
                listtoinput.pop(0)
                replaceLine(int(listtoinput[0]))
            case ':rp':
                listtoinput=userInput.split()
                listtoinput.pop(0)
                replace(listtoinput)
            case ":in":
                listtoinput=userInput.split()
                listtoinput.pop(0)
                insertLine(int(listtoinput[0]), listtoinput)
            case ":rn":
                coderun(extension)
            case ":fnd":
                os.system("cls" if os.name == "nt" else "clear")
                printfile(extension, userInput.split()[1])
                input('press enter to continue: ')
            case ":term":
                os.system("cls" if os.name == "nt" else "clear")
                term.main()
            case ":clf":
                clearfile(filename)
    except IndexError:
        print("invalid command")
        input("press enter to continue: ")

#writes to the file
def write(filename, extension):
    global lines
    with open(filename, "w") as file:
        for item in lines:
            file.write(item)

def clearfile(filename):
    file=open(filename, 'w')
    file.write('')
    file.close()
    openfile(filename)

#editor function
def editor():
    global filename
    global extension
    global lines
    os.system("cls" if os.name == "nt" else "clear")
    printfile(extension)
    userInput=input("|")
    if userInput.startswith(":"):
        if commands(userInput.strip()):
            return True
    else:
        lines.append(userInput+'\n')
    write(filename, extension)

#main function
def main():
    global filename, extension, lines
    if checksetting(1):
        print("here is a list of files in the current directory:")
        if PLATFORM == "Windows":
            os.system("dir")
        else:
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
    if extension == ".md":
        openinc()
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
