#!/bin/bash

file_path="/home/retropie/RetroPi/select_game.py"

while true; do
    if [ -f "$file_path" ]; then
        echo "File found trys to open "
        sudo python3 "$file_path"
        sudo shutdown now
    else
        echo "No file found"
    fi
        sleep 3
done

