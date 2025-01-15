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
    bash ./harmony-setup.sh
fi
