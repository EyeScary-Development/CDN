#!/bin/bash
if [[ -d "~/.agpm" ]]; then
    echo "Agpm directory exists"
else
    echo "Agpm directory does not exist. Creating directory..."
    mkdir ~/.agpm/
fi
cd ~/.agpm
if [[ -d "~/.agpm/harmony" ]]; then
    echo "Harmony directory exists already, try update instead"
    exit
else
    echo "Harmony not installed, installing..."
    mkdir ~/.agpm/harmony && cd ~/.agpm/harmony
    curl -O https://eyescary-development.github.io/CDN/agpm_packages/harmony/package.zip
    unzip package.zip
    rm package.zip

    read -p "What shell are you using? (zsh, fish, bash): " shellinuse

    if [ "$shellinuse" == "zsh" ]; then
      export file="$HOME/.zshrc"
    elif [ "$shellinuse" == "bash" ]; then
      export file="$HOME/.bashrc"
    else
      export file="$HOME/.config/fish/config.fish"
    fi

echo "alias harmony='python3 ~/.agpm/harmony/menu.py'" >> "$file"
fi
