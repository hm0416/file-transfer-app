import os
import socket
from datetime import datetime

### AUTHOR : HIFA MOUSOU ###

#list all received files server has received
def list_files():
    pass

#delete a received file
def delete_files():
    pass

#get a list of cmds the sever can execute
def get_cmds():
    pass

#quit program
def quit_cmd():
    pass

#rename a received file on the sever
def rename_files():
    pass



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


while True:
    socket_connection, address = server_socket.accept()
    print("Connection accepted from " + str(address))

    #receiving file from client
    received_file_name = socket_connection.recv(1024).decode("utf-8")
    received_file = open(received_file_name, "w")
    socket_connection.send("Filename received".encode("utf-8"))
    received_file_data = socket_connection.recv(1024).decode("utf-8")
    received_file.write(received_file_data)
    socket_connection.send("File received.".encode("utf-8"))

    received_file.close()
    socket_connection.close()
    print(f"Sever disconnected. You can find the transferred file in the received folder.")




