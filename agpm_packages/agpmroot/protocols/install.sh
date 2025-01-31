if [[ -d "$(eval echo "~/.agpm/")" ]]; then
    echo "Agpm directory exists"
else
    echo "Agpm directory does not exist. Creating directory..."
    mkdir ~/.agpm/
fi

if [[ -d "$(eval echo "~/.agpm/agpmroot/")" ]]; then
    echo "Agpm is installed, try update instead"
    exit
else
    echo "Agpm is not installed, can proceed with installation..."
fi
cd ~/.agpm
mkdir ~/.agpm/agpmroot && cd ~/.agpm/agpmroot
curl -O https://eyescary-development.github.io/CDN/agpm_packages/agpmroot/package.zip
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
echo "alias agpm='python3 ~/.agpm/agpmroot/main.py'" >> "$file"
echo "AGPM installed successfully!"
