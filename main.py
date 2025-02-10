#!/data/data/com.termux/files/usr/bin/bash

# 🌟 Termux Theme Changer Script
# 📌 Author: Broken-Nadeem
# 🔥 Version: 1.1

# 🚀 Clear Screen
clear

# 🎬 Animated Intro
animate_intro() {
    echo -e "\033[1;32m"
    local text="🔹 Termux Theme Changer 🔹"
    for ((i = 0; i < ${#text}; i++)); do
        echo -n "${text:$i:1}"
        sleep 0.1
    done
    echo -e "\n"
    sleep 1
}

animate_intro

# 🎨 Applying Theme
echo -e "\033[1;36m🎨 Applying Custom Theme...\033[0m"
mkdir -p ~/.termux

# 🌈 Custom Colors
cat > ~/.termux/colors.properties << EOF
background = #1E1E1E
foreground = #C5C8C6
cursor = #F8F8F0

color0 = #1E1E1E
color1 = #F92672
color2 = #A6E22E
color3 = #F4BF75
color4 = #66D9EF
color5 = #AE81FF
color6 = #A1EFE4
color7 = #F8F8F2
color8 = #75715E
color9 = #F92672
color10 = #A6E22E
color11 = #F4BF75
color12 = #66D9EF
color13 = #AE81FF
color14 = #A1EFE4
color15 = #F9F8F5
EOF

# 🔡 Font Settings
echo -e "\033[1;33m🔡 Adjusting Font & Settings...\033[0m"
cat > ~/.termux/termux.properties << EOF
bell-character=ignore
use-black-ui=true
extra-keys = [ ['ESC','/','-','HOME','UP','END','PGUP'], ['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN'] ]
terminal-margin=2
EOF

# 🔥 Custom PS1 Prompt
echo -e "\033[1;34m🔥 Setting Up Cool Terminal Prompt...\033[0m"
echo 'PS1="\e[1;32m\u\e[1;34m@\h\e[1;36m ~ \w \e[1;32m➜ \e[0m"' >> ~/.bashrc

# ♻ Reload Termux Settings
echo -e "\033[1;35m♻ Restarting Termux for Changes to Take Effect...\033[0m"
termux-reload-settings
sleep 2

echo -e "\033[1;32m✅ Theme Successfully Applied! Restart Termux to See Changes.\033[0m"
