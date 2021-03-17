import os
import socket

user_input_host = input("What's the sever host? ")
user_input_port = input("What's the server port number? ")
client_host = user_input_host
client_port = int(user_input_port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((client_host, client_port))

print("Client Connected")
received_file_name = input("Enter name for the transferred file: ")
received_file = open(received_file_name, 'wb')
received_file_data = client_socket.recv(1024)
received_file.write(received_file_data)
received_file.close()

print("File transferred successfully. You can access the file at ")
