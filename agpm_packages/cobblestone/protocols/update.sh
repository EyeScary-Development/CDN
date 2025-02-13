if [[ -d "$(eval echo "~/.agpm")" ]]; then
    echo "Agpm directory exists"
else
    echo "Agpm directory doesn't exist, harmony therefore cannot be installed. quitting..."
    exit
fi
cd ~/.agpm
if [[ -d "$(eval echo "~/.agpm/cobblestone")" ]]; then
    echo "Package directory exists. Proceeding..."
    cd ~/.agpm/cobblestone/ 
    rm *
    curl -O https://eyescary-development.github.io/CDN/cobblestone/agpmroot/package.zip
    unzip package.zip
    rm package.zip
else
    echo "Package not installed. Task failed successfully. Quitting..."
fi
