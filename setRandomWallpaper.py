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
    fileNames = os.listdir(folder)
    fileNames.sort()
    return fileNames

def getRandomElement(compList):
    rnd = None
    startTime = time.time()
    
    with open("seedLog.txt", "w") as file:
        for i in range(1000):
            seedTime = int((startTime - (startTime % 1))/50)
            startTime += 60
            
            random.seed(seedTime)
            randVal = random.randint(0, len(compList) - 1)
            if rnd == None:     
                rnd = randVal
            file.write(f"index: {i} -- {compList[randVal]}\n")


    return compList[rnd]

def setBackgroundToFile(fileLocation):
    os.system(f"gsettings set org.gnome.desktop.background picture-options scaled")
    os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark {fileLocation}")
    os.system(f"gsettings set org.gnome.desktop.background picture-uri {fileLocation}")

if __name__ == "__main__":
    main()