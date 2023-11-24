from colorama import Fore, Back, Style
import os
import subprocess
import sys
os.system("pip install -r requirements.txt")
# TOOLS | MODULES
from modules.Chat import chat
from modules.packet_sender import packetsender
from modules.web_browser import browser
from modules.downloader import downloader

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
    print(f"X Instance of EletrixTool Launched ! | X users in the eletrixtool chat !")
    print("TOOLS LIST :")
    print('--------------------------------------------------------')
    print("1 = Chat | 2 = PacketSender | 3 = SecureBrowser (need desktop env) | 4 = Downloader | 9 = Exit")
    print('--------------------------------------------------------')
    cmd = input("Select : ")
    if cmd.lower() == "chat" or cmd == "1":
        chat.start()
    if cmd.lower() == "packetsender" or cmd == "2":
        packetsender.start()
    if cmd.lower() == "securebrowser" or cmd == "3":
        browser.start()
    if cmd.lower() == "downloader" or cmd == "4":
        downloader.start()
    elif cmd.lower() == "exit" or cmd == "9":
        print("Thank for using EletrixTool ! :D")
        exit()




while True:
    cmd_gui()


