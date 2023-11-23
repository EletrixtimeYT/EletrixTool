import socket
import threading
import time
import sys
import os


def receive_messages(s):
    while True:
        try:
            message = s.recv(1024).decode()
            print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def start():
    if sys.platform == 'win32' or 'win64':
        os.system("cls")
    else:
        os.system("clear")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Welcome to EletrixTool Chat Tool ! for joining the official server left blank everthing (and type a username)")
    host = input('Enter hostname or host IP (left blank for default): ')
    if not host:
        host = 'cloud-1.boomerangbs.fr'
    
    port = input('Port (left blank for default): ')
    if not port:
        port = 1103
    else:
        port = int(port)
    try:
        s.connect((host, port))
    except Exception as e:
        print(f"Chat >> Failed to connect ): {e}")
        print("Returning to home menu in 3s !")
        time.sleep(3)

    username = input('Enter your username: ')

    s.send(username.encode())

    
    text_on_join = s.recv(1024).decode()
    print(text_on_join)

   
    receive_thread = threading.Thread(target=receive_messages, args=(s,))
    receive_thread.start()


    while True:
        message = input(f"{username} >> ")
        s.send(message.encode())

        # Local Client Command
        if message == '/exit':
            print('Exiting the chat...')
            s.close()
            break


