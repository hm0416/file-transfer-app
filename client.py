import os
import socket

### AUTHOR : HIFA MOUSOU ###

#list all files that you can send to the sever
def list_files():
    pass

#delete a file that's on the client side
def delete_files():
    pass

#rename a file on the client side
def rename_files():
    pass

#quit program
def quit_cmd():
    pass

#update the data inside a file on the client side
def update_file():
    pass

#get a list of avaiable cmds user can execute on the client side
def get_cmds():
    pass

user_input_host = input("What's the sever host? ")
user_input_port = input("What's the server port number? ")
client_host = user_input_host
client_port = int(user_input_port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((client_host, client_port))

print("Client Connected")

file_name = input("\nEnter the name of the file you would like to send to the server: ")
file = open(file_name, 'r')
file_data = file.read()
#sends filename
client_socket.send(file_name.encode("utf-8"))
client_socket.recv(1024).decode("utf-8")

#sends file data
client_socket.send(file_data.encode("utf-8"))
client_socket.recv(1024).decode("utf-8")
print("File transferred successfully to server!")
file.close()
client_socket.close()

#
# while True:
#     command = input("> ")
#     command = command.split(" ")
#     cmd_inputted = command[0]
