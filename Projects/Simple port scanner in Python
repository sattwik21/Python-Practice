#!/usr/bin/python3
#decent__ayush 

import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.settimeout(5.0)  # default timeout 


#input
host = input("Enter the IP address you want to scan:\n  ")
port = int(input("Enter the port you want to scan:\n"))

#function
def portScanner(port):
    if s.connect_ex((host,port)):
        print("The port is closed :( /n")
    else:
        print("The port is open :) /n") 

#Calling function
portScanner(port)
