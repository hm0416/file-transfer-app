import os
import socket
from datetime import datetime
from os import listdir
from os.path import isfile, join

### AUTHOR : HIFA MOUSOU ###

# #list all received files server has received
# def list_files():
#     pass
#
# #delete a received file
# def delete_files():
#     pass
#
# #get a list of cmds the sever can execute
# def get_cmds():
#     pass
#
# #quit program
# def quit_cmd():
#     pass
#
# #rename a received file on the sever
# def rename_files():
#     pass



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
    socket_connection.send("File received.\n".encode("utf-8"))

    print("File transferred to received folder!")

    print("\nAvailable Commands You Can Enter: \n LIST: List all received files server has received \n DELETE: Delete a received file \n GET: Get a list of cmds the sever can execute \n QUIT: Quit the program \n RENAME: Rename a received file")

    while True:
        cmd = input("\nEnter Command: ")
        if cmd == "GET":
            print("Available Commands: \n LIST: List all received files server has received \n DELETE: Delete a received file \n GET: Get a list of cmds the sever can execute \n QUIT: Quit the program \n RENAME: Rename a received file")
        if cmd == "QUIT":
            received_file.close()
            socket_connection.close()
            print(f"Sever disconnected. You can find any transferred files in the received folder.")
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
                    received_file.close()
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
                    received_file.close()
                    os.rename(directory + "\\" + file_to_rename, directory + "\\" + new_name)
                    print("File renamed successfully.")
                else:
                    file_to_rename = input("File not found. Enter another file to rename: ")

    received_file.close()

socket_connection.close()
# print(f"Sever disconnected. You can find the transferred file in the received folder.")




