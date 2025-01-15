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
    for file in menu.py editor.py langservhub.py consts.py settings.escnf settings.py runcode.py harmony-setup.sh README.md; do
        curl -O https://eyescary-development.github.io/CDN/agpm_packages/harmony/$file
    done
    bash harmony-setup.sh
fi
