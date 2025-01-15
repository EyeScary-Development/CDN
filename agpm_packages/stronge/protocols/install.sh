if [[ -d "~/.agpm" ]]; then
    echo "Agpm directory exists"
else
    echo "Agpm directory does not exist. Creating directory..."
    mkdir ~/.agpm/
fi
cd ~/.agpm
if [[ -d "~/.agpm/stronge" ]]; then
    echo "Stronge directory exists already, try update instead"
    exit
else
    echo "Stronge not installed, installing..."
    mkdir ~/.agpm/stronge && cd ~/.agpm/stronge
    curl -O https://eyescary-development.github.io/CDN/agpm_packages/stronge/package.zip
    unzip package.zip
    rm package.zip
fi
