if [[ -d "$(eval echo "~/.agpm")" ]]; then
    echo "Agpm directory exists"
else
    echo "Agpm directory doesn't exist, harmony therefore cannot be installed. quitting..."
    exit
fi
cd ~/.agpm
if [[ -d "$(eval echo "~/.agpm/harmony")" ]]; then
    echo "Harmony directory exists. Proceeding..."
    cd ~/.agpm/harmony/ 
    rm *
    curl -O https://eyescary-development.github.io/CDN/agpm_packages/harmony/package.zip
    unzip package.zip
    rm package.zip
else
    echo "Harmony not installed. Task failed successfully. Quitting..."
fi
