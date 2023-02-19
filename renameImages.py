import os
import time

LOCATION = "/home/lucas/randoWallpaper/wallpapers"
RESERVED = ["switcherArchive.sh", "switcher.sh", "origImg", "renameImages.py"]

def main():
    renamed = []
    while(True):
        current = getImageNames()
        if len(current) > 0:
            renamed = renameUnchanged(renamed, current)

def renameUnchanged(renamed, current):
    new = []
    count = len(renamed) + 1
    for image in current:
        if image not in renamed and image != "":
            parts = image.split('.')
            name = f'{count :{0}>{3}}.{parts[-1]}'
            os.system(f'mv {image} {name}')
            new.append(name)
            count += 1
            time.sleep(1)

    for newElement in new:
        renamed.append(newElement)

    return renamed

def getImageNames():
    return [element for element in os.listdir(LOCATION) if element not in RESERVED]

if __name__ == "__main__":
    main()