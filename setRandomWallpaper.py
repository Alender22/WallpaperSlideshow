#!/usr/bin/python3
import os
import random
import time
import random

LOCATION = ""
SUBFOLDER = "wallpapers/"

def main():
    global LOCATION
    LOCATION = getLocation()
    coordinator()

def coordinator():
    files = getFilesInFolder(LOCATION + SUBFOLDER)
    choice = getRandomElement(files)
    setBackgroundToFile(LOCATION + SUBFOLDER + choice)

def getLocation():
    entirePath = __file__
    pathParts = entirePath.split('/')
    rootPath = "".join([pathParts[i] + '/' for i in range(len(pathParts)) if i < len(pathParts) - 1])
    return rootPath

def getFilesInFolder(folder):
    return os.listdir(folder)

def getRandomElement(compList):
    random.seed(time.time())
    rnd = random.randint(0, len(compList) - 1)
    return compList[rnd]

def setBackgroundToFile(fileLocation):
    os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark {fileLocation}")
    os.system(f"gsettings set org.gnome.desktop.background picture-uri {fileLocation}")

if __name__ == "__main__":
    main()