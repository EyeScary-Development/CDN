if [[ -d "$(eval echo "~/.agpm")" ]]; then
    echo "Agpm directory exists"
else
    echo "Agpm directory doesn't exist, harmony therefore cannot be installed. quitting..."
    exit
fi
cd ~/.agpm
if [[ -d "$(eval echo "~/.agpm/agpmroot")" ]]; then
    echo "AGPM root directory exists. Proceeding..."
    cd ~/.agpm/agpmroot/ 
    rm *
    curl -O https://eyescary-development.github.io/CDN/agpm_packages/agpmroot/package.zip
    unzip package.zip
    rm package.zip
else
    echo "AGPM not installed. Task failed successfully. Quitting..."
fi
