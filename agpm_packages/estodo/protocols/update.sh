if [[ -d "$(eval echo "~/.agpm")" ]]; then
    echo "Agpm directory exists"
else
    echo "Agpm directory doesn't exist, package therefore cannot be installed. quitting..."
    exit
fi
cd ~/.agpm
if [[ -d "$(eval echo "~/.agpm/estodo")" ]]; then
    echo "Package directory exists. Proceeding..."
    cd ~/.agpm/estodo/ 
    rm *
    curl -O https://eyescary-development.github.io/CDN/agpm_packages/estodo/package.zip
    unzip package.zip
    echo "cleaning up..."
    rm package.zip
else
    echo "Package not installed. Task failed successfully. Quitting..."
fi
