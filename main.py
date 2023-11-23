from colorama import Fore, Back, Style
from modules.Chat import chat
import os
import subprocess
import sys



def cmd_gui():
    if sys.platform == 'win32' or 'win64':
        os.system("cls")
    else:
        os.system("clear")
    print(Fore.RED + """
                /$$$$$$$$ /$$       /$$$$$$$$ /$$$$$$$$ /$$$$$$$  /$$$$$$ /$$   /$$  /$$$$$$$$ /$$$$$$   /$$$$$$  /$$      
                | $$_____/| $$      | $$_____/|__  $$__/| $$__  $$|_  $$_/| $$  / $$ |__  $$__//$$__  $$ /$$__  $$| $$      
                | $$      | $$      | $$         | $$   | $$  \ $$  | $$  |  $$/ $$/    | $$  | $$  \ $$| $$  \ $$| $$      
                | $$$$$   | $$      | $$$$$      | $$   | $$$$$$$/  | $$   \  $$$$/     | $$  | $$  | $$| $$  | $$| $$      
                | $$__/   | $$      | $$__/      | $$   | $$__  $$  | $$    >$$  $$     | $$  | $$  | $$| $$  | $$| $$      
                | $$      | $$      | $$         | $$   | $$  \ $$  | $$   /$$/\  $$    | $$  | $$  | $$| $$  | $$| $$      
                | $$$$$$$$| $$$$$$$$| $$$$$$$$   | $$   | $$  | $$ /$$$$$$| $$  \ $$ /$$| $$  |  $$$$$$/|  $$$$$$/| $$$$$$$$
                |________/|________/|________/   |__/   |__/  |__/|______/|__/  |__/|__/|__/   \______/  \______/ |________/""")
    print("                                                         Made by EletrixTime")
    print(Style.RESET_ALL)
    print("X Instance of EletrixTool Launched ! | X users in the eletrixtool chat !")
    print("          TOOLS LIST")
    print('--------------------------------------------------------')
    print("1 = Chat | 2 = Downloader | 3 = Exit")
    print('--------------------------------------------------------')
    cmd = input("Select : ")
    if cmd.lower() == "chat" or cmd == "1":
        chat.start()
    elif cmd.lower() == "exit" or cmd == "3":
        print("Thank for using EletrixTool ! :D")
        exit()




while True:
    cmd_gui()


