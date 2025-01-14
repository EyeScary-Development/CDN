if [[ -d "~/.agpm" ]]; then
    echo "Agpm directory exists"
else
    echo "Agpm directory does not exist. Creating directory..."
    mkdir ~/.agpm
fi
cd ~/.agpm
if [[ -d "~/.agpm/harmony" ]]; then
    echo "Harmony directory exists already, try update instead"
    exit
else
    echo "Harmony not installed, installing..."
    wget https://cdn.jsdelivr.net/gh/EyeScary-Development/CDN/agpm_packages/harmony/
    cd ~/.agpm/harmony
    bash harmony-setup.sh
fi
