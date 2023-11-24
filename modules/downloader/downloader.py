import os
import sys
from modules.downloader import storage

def start():
    if sys.platform == 'win32' or 'win64':
         os.system("cls")
    else:
        os.system("clear")
    print("================================================")
    print("                  DOWNLOADER")
    print("================================================")
    print("Select a thing to download :")
    print("1 = Spicetify")
    cmd = input("Select : ")
    if cmd.lower() == "spicetify" or cmd == "1":
        
        if sys.platform == 'win32' or 'win64':
            os.system(storage.SPICETIFY_WIN_DOWNLOAD)
            os.system(storage.SPICETIFY_MAKETPLACE_WIN_DOWNLOAD)
        else:
            os.system(storage.SPICETIFY_LINUX_DOWNLOAD)
            os.system(storage.SPICETIFY_MAKETPLACE_WIN_DOWNLOAD)