import os
import socket
from datetime import datetime
from os import listdir
from os.path import isfile, join
import threading

### AUTHOR : HIFA MOUSOU ###

def client_func(socket_connection, address):
    while True:
        cmd = socket_connection.recv(1024).decode("utf-8")
        print(cmd)

        if cmd == "GET":
            cmds_list = "Available Commands: \n LIST: List all received files server has received \n DELETE: Delete a received file \n GET: Get a list of cmds the sever can execute \n QUIT: Quit the program \n RENAME: Rename a received file \n SEND: Send a file to the server"
            socket_connection.send(cmds_list.encode("utf-8"))
        if cmd == "QUIT":
            # received_file.close()
            socket_connection.close()
            print(f"Sever disconnected. You can find any transferred files in the received folder.")
            break
        if cmd == "LIST":
            i = 1
            list_of_files = ""
            list_of_received_files = [f for f in listdir(r"/Users/hm0416/file-transfer-app/received") if isfile(join(r"/Users/hm0416/file-transfer-app/received", f))]
            for f in list_of_received_files:
                # if f != '.DS_Store' or f != 'server.py' or f != 'server.bat':
                list_of_files += str(i) + '. ' + f + '\n'
                i += 1
            socket_connection.send(list_of_files.encode("utf-8"))
        if cmd == "DELETE":
            user_input = socket_connection.recv(1024).decode("utf-8")
            user_input_w_dir = os.path.join(r"/Users/hm0416/file-transfer-app/received", user_input)
            # files_in_dir = os.listdir(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received")

            os.remove(user_input_w_dir)
            socket_connection.send("File deleted successfully.".encode("utf-8"))

            # while True:
            #     if user_input in files_in_dir:
            #         # os.remove(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received\{user_input}")
            #         # received_file.close()
            #         os.remove(user_input)
            #         socket_connection.send("File deleted successfully.".encode("utf-8"))
            #         break
            #     else:
            #         user_input = input("File not found. Enter another file to delete: ")
        if cmd == "RENAME":
            file_to_rename = socket_connection.recv(1024).decode("utf-8")
            new_name = socket_connection.recv(1024).decode("utf-8")
            files_in_dir_for_rn = os.listdir(r"/Users/hm0416/file-transfer-app/received")
            # directory = r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received"

            file_to_rename_w_dir = os.path.join(r"/Users/hm0416/file-transfer-app/received", file_to_rename)
            new_name_w_dir = os.path.join(r"/Users/hm0416/file-transfer-app/received", new_name)
            # os.rename(directory + "\\" + file_to_rename, directory + "\\" + new_name)
            os.rename(file_to_rename_w_dir, new_name_w_dir)
            socket_connection.send("File renamed successfully.".encode("utf-8"))

        if cmd == "SEND":
            file_name_to_send = socket_connection.recv(1024).decode("utf-8")
            files_in_dir_to_send = os.listdir(r"/Users/hm0416/file-transfer-app/sender")
            path_to_send_to = os.path.join(r"/Users/hm0416/file-transfer-app/received", file_name_to_send)
            file_to_send_w_dir = os.path.join(r"/Users/hm0416/file-transfer-app/sender", file_name_to_send)

            file = open(file_to_send_w_dir, 'r')
            file_data = file.read()
            with open(path_to_send_to, 'w') as new_f:
                new_f.write(file_data)

            # file_to_send_w_dir = os.path.join(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\sender", file_name_to_send)
            # file = open(file_to_send_w_dir, 'r')
            # file_data = file.read()
            # sends filename
            # socket_connection.send(file_name_to_send.encode("utf-8"))
            # socket_connection.recv(1024).decode("utf-8")
            #
            # # sends file data
            # socket_connection.send(file_data.encode("utf-8"))
            # socket_connection.recv(1024).decode("utf-8")

            socket_connection.send("File transferred successfully to server!".encode("utf-8"))
            file.close()
            break


    # received_file.close()

    socket_connection.close()

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
    socket_connection.send("Hi, this is a file transfer app. Type GET to view a list of commands :)".encode("utf-8"))
    thread = threading.Thread(target= client_func, args= (socket_connection, address))
    thread.start()

server_socket.close()

    # #receiving file from client
    # received_file_name = socket_connection.recv(1024).decode("utf-8")
    # received_file = open(received_file_name, "w")
    # socket_connection.send("Filename received".encode("utf-8"))
    # received_file_data = socket_connection.recv(1024).decode("utf-8")
    # received_file.write(received_file_data)
    # socket_connection.send("The File and its data has been received.\n".encode("utf-8"))

    # print("File transferred to received folder!")

    # print("\nAvailable Commands You Can Enter: \n LIST: List all received files server has received \n DELETE: Delete a received file \n GET: Get a list of cmds the sever can execute \n QUIT: Quit the program \n RENAME: Rename a received file")




