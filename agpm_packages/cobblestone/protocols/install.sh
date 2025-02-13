if [[ -d "$(eval echo "~/.agpm/")" ]]; then
    echo "Agpm directory exists"
else
    echo "Agpm directory does not exist. Creating directory..."
    mkdir ~/.agpm/
fi

if [[ -d "$(eval echo "~/.agpm/cobblestone/")" ]]; then
    echo "Package is installed, try update instead"
    exit
else
    echo "Package is not installed, can proceed with installation..."
fi
cd ~/.agpm
mkdir ~/.agpm/cobblestone && cd ~/.agpm/cobblestone
curl -O https://eyescary-development.github.io/CDN/agpm_packages/cobblestone/package.zip
unzip package.zip
rm package.zip
if [ "$SHELL" == "/bin/zsh" ]; then
  export file="$HOME/.zshrc"
elif [ "$SHELL" == "/bin/bash" ]; then
  export file="$HOME/.bashrc"
elif ["$SHELL" == "/bin/fish"]; then
  export file="$HOME/.config/fish/config.fish"
else
  echo "Your shell is not supported, make all aliases manually"
  exit
fi
echo "alias cobble='python3 ~/.agpm/cobblestone/menu.py'" >> "$file"
echo "package installed successfully!"
