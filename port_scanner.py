#!/bin/python3
import sys 
import socket
from datetime import datetime

#Define our target
if len(sys.argv)==2: #argv is the amount of arguements we are giving
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
    print("Invalid amount of arguements")
    print("Syntax: python3 port_scanner.py <IP>")