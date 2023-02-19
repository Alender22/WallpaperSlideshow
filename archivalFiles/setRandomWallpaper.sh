#choose your wallpaper
#PIC="/home/lucas/randoWallpaper/wallpapers/00001_2729792719_0000_by_wolfis58_dfpjt5i-350t.jpg"
#set your wallpaper
#gsettings set org.gnome.desktop.background picture-options "scaled"
#gsettings set org.gnome.desktop.background picture-uri-dark "file://$PIC"
#gsettings set org.gnome.desktop.background picture-uri-dark "file:///home/lucas/randoWallpaper/wallpapers/026.jpg"

#!/bin/bash

dbus-launch /usr/bin/python3 /home/lucas/randoWallpaper/randomFileName.py