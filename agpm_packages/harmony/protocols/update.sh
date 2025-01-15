if [[ -d "~/.agpm" ]]; then
    echo "Agpm directory exists"
else
    echo "Agpm directory doesn't exist, harmony cannot be installed. quitting..."
    exit
fi
cd ~/.agpm
if [[ -d "~/.agpm/harmony" ]]; then
    echo "Harmony directory exists. Proceeding..."
    cd ~/.agpm/harmony/ 
    rm *
    for file in menu.py editor.py langservhub.py consts.py settings.escnf ESDLang.py settings.py runcode.py harmony-setup.sh README.md; do
        curl -O https://eyescary-development.github.io/CDN/agpm_packages/harmony/$file
    done
else
    echo "Harmony not installed. Task failed successfully. Quitting..."
fi
