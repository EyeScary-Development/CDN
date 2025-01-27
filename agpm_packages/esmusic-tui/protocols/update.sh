if [[ -d "$(eval echo "~/.agpm")" ]]; then
    echo "Agpm directory exists"
else
    echo "Agpm directory doesn't exist, harmony therefore cannot be installed. quitting..."
    exit
fi
cd ~/.agpm
if [[ -d "$(eval echo "~/.agpm/esmusic-tui")" ]]; then
    echo "Package directory exists. Proceeding..."
    cd ~/.agpm/esmusic-tui/ 
    rm *
    curl -O https://eyescary-development.github.io/CDN/agpm_packages/esmusic-tui/package.zip
    unzip package.zip
    rm package.zip
else
    echo "Package not installed. Task failed successfully. Quitting..."
fi
