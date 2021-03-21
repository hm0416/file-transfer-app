import os
import socket
from os import listdir
from os.path import isfile, join


### AUTHOR : HIFA MOUSOU ###

# global file

user_input_host = input("What's the sever host? ")
user_input_port = input("What's the server port number? ")
client_host = user_input_host
client_port = int(user_input_port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((client_host, client_port))

print("Client Connected")

data = client_socket.recv(1024).decode("utf-8")
# print(data)

client_socket.close()

