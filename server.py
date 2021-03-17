import os
import socket
from datetime import datetime

server_host = '127.0.0.1'
user_input_port = input("What network port will the server application listen from? ")
server_port = int(user_input_port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_host, server_port))
server_socket.listen(1)
print("The server is ready to receive: ")

#display status message that includes port number on which server is listening
date_time = datetime.now()
current_date_time = date_time.strftime("%a %b %d %H:%M:%S %Y")
print(current_date_time +" File-transfer server starting on port " + str(server_port))

file_name = input("\nEnter the name of the file you would like to send to the client: ")
file = open(file_name, 'rb')

while True:
    socket_connection, address = server_socket.accept()
    print("Connection accepted from " + str(address))
    received_data = file.recv(1024).decode() #gets data from file
    print("Server received " + received_data)
    socket_connection.send(received_data) #sends the file data
    print("Data has been sent! :)")



