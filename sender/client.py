import os
import socket
from os import listdir
from os.path import isfile, join

### AUTHOR : HIFA MOUSOU ###

# #list all files that you can send to the sever
# def list_files():
#     pass
#
# #delete a file that's on the client side
# def delete_files():
#     pass
#
# #rename a file on the client side
# def rename_files():
#     pass
#
# #quit program
# def quit_cmd():
#     pass
#
# #update the data inside a file on the client side
# def update_file():
#     pass
#
# #get a list of avaiable cmds user can execute on the client side
# def get_cmds():
#     pass

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

print("\nAvailable Commands You Can Enter: \n LIST: List all files available to send to the server \n DELETE: Delete an existing file \n GET: Get a list of cmds the client can execute \n QUIT: Quit the program \n RENAME: Rename an existing file")

while True:
    cmd = input("\nEnter Command: ")
    if cmd == "GET":
        print("\nAvailable Commands: \n LIST: List all files available to send to the server \n DELETE: Delete an existing file \n GET: Get a list of cmds the client can execute \n QUIT: Quit the program \n RENAME: Rename an existing file")
    if cmd == "QUIT":
        file.close()
        client_socket.close()
        print(f"Client disconnected. Any files that were sent have been received by the server.")
        quit()
    if cmd == "LIST":
        i = 1
        list_of_received_files = [f for f in listdir(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received") if isfile(join(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received", f))]
        for f in list_of_received_files:
            if f == '.DS_Store' or f == 'server.py':
                pass
            else:
                print(str(i) + '. ' + f + '\n')
                i += 1
    if cmd == "DELETE":
        user_input = input("What file do you want to delete?: ")
        files_in_dir = os.listdir(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received")
        while True:
            if user_input in files_in_dir:
                # os.remove(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received\{user_input}")
                file.close()
                os.remove(user_input)
                print("File deleted successfully.")
                break
            else:
                user_input = input("File not found. Enter another file to delete: ")
    if cmd == "RENAME":
        file_to_rename = input("Which file do you want to rename?: ")
        new_name = input("What would you like to rename it to?: ")
        files_in_dir_for_rn = os.listdir(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received")
        directory = r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received"
        while True:
            if file_to_rename in files_in_dir_for_rn:
                file.close()
                file_to_rename_w_dir = os.path.join(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received",
                                                    file_to_rename)
                new_name_w_dir = os.path.join(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received", new_name)
                # os.rename(directory + "\\" + file_to_rename, directory + "\\" + new_name)
                os.rename(file_to_rename_w_dir, new_name_w_dir)
                print("File renamed successfully.")
                break
            else:
                file_to_rename = input("File not found. Enter another file to rename: ")




file.close()
client_socket.close()

#
# while True:
#     command = input("> ")
#     command = command.split(" ")
#     cmd_inputted = command[0]
