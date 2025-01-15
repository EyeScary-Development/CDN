# Harmony
 Introducing Harmony, the future of EyeScary Development's terminal based code editors

 
# What makes it better?
 It has been written from the ground up, designed with the goal to have the same base functionality as Stronge
 * It's more line efficient
 * So it's more storage efficient
 * A new syntax highlighting system is more efficient
 * Multiple languages have been implemented from the start to avoid turning into another ESDLang IDE
 * We implemented vim like commands such as `:dl`, `:q`, `:rn`
 * Unlike vim, we have autosave

# What has been added on top of base Stronge functionality?
* Find and replace
* Multiple language syntax highlighting
* indents actually show up
* When you are choosing a file, there is a toggleable setting that lets you show a list of the files in the current directory when choosing a file
* the : sf command allows you to rapidly change between files without having to restart the editor
* completely unrelated, but there's an install script now?
* So far, uhhh, that's kinda it?

# Installation
**To use the autoinstall script, you must be on a nix based os and use fish, zsh or bash**
### Auto installation script
* download the source code
* extract it into a folder
* cd into the folder
* run the harmony-setup.sh file
* input the shell you use
* done! restart the instance of your shell and you can now type 'harmony' from anywhere and harmony will open in that directory
### Manual installation (windows, mac, non zsh bash or fish users)
* download the source code
* extract it into any folder
* create an alias for harmony or whatever you want to call it and set it to alias to 'python3 ~/path/to/harmony/menu.py'
* done! restart the instance of your shell and you can now type the alias you chose from anywhere and harmony will open in that directory

# What makes it better than Stronge for writing ESDLang?
A new comprehensively simple syntax highlighting system with planned snippet integration will make error spotting simpler by having one category of error highlighting instead of 2

# What makes it better than Stronge for other languages?
Unlike Stronge, which went on the path of "ESDLang IDE" the day version 0.1 was first written, Harmony was designed to be multilingual with a language server manager that is simple and able to understand what language you are writing in and pick the appropriate syntax highlighting mechanism.
From the beginning, we're commited to you being able to run code in multiple languages like python, java, and maybe, eventually, soon(tm), C, C# and C++

# Roadmap
- [x] Menu, like in Stronge
- [ ] Better syntax highlighting 
- [x] Autocorrect bracket matching/quote matching
- [ ] ~~idk maybe songs again for funni~~ Maybe not
- [ ] Switch to Stdin for inputs
- [ ] Opening sounds
- [x] replace
- [x] find
- [x] improve line editing
- [x] java syntax highlighting
- [x] Organise things and document
- [ ] extension installer script
- [ ] ~~maybe migrate to actual TUI~~ NO
