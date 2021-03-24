import os
import socket
from datetime import datetime
from os import listdir
from os.path import isfile, join

### AUTHOR : HIFA MOUSOU ###

server_host = '127.0.0.1'
user_input_port = input("What network port will the server application listen from? ")
server_port = int(user_input_port)

#Gets the server ready
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
    socket_connection.send("\nHi, this is a file transfer app. Type GET to view a list of commands :)".encode("utf-8"))

    while True:
        cmd = socket_connection.recv(1024).decode("utf-8") #gets the cmd entered from the client
        print("\n " + cmd + "\n")

        #checks the cmd entered and sends the correct response back to the client
        if cmd == "GET" or cmd == "get":
            cmds_list = "\nAvailable Commands: \n LIST: List all received files server has received \n DELETE: Delete a received file \n GET: Get a list of cmds the sever can execute \n QUIT: Quit the program \n RENAME: Rename a received file \n SEND: Send a file to the server"
            socket_connection.send(cmds_list.encode("utf-8"))
        elif cmd == "QUIT" or cmd == "quit":
            socket_connection.close()
            print(f"Server disconnected. You can find any transferred files in the received folder.")
            break
        elif cmd == "LIST" or cmd == "list":
            i = 1
            list_of_files = ""
            list_of_received_files = [f for f in listdir(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received") if isfile(join(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received", f))] #finds all files in the received directory for the server
            for f in list_of_received_files:
                # if f != '.DS_Store' or f != 'server.py' or f != 'server.bat':
                list_of_files += str(i) + '. ' + f + '\n' #displays the files
                i += 1
            socket_connection.send(list_of_files.encode("utf-8"))
        elif cmd == "DELETE" or cmd == "delete":
            user_input = socket_connection.recv(1024).decode("utf-8") #gets user input from client side
            user_input_w_dir = os.path.join(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received", user_input) #gets directory for the file the user wants to delete
            os.remove(user_input_w_dir) #removes file
            socket_connection.send("File deleted successfully.".encode("utf-8"))
        elif cmd == "RENAME" or cmd == "rename":
            file_to_rename = socket_connection.recv(1024).decode("utf-8") #gets the file to rename
            new_name = socket_connection.recv(1024).decode("utf-8") #gets the name to rename the file to
            file_to_rename_w_dir = os.path.join(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received", file_to_rename) #gets directory for the file the user wants to rename
            new_name_w_dir = os.path.join(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received", new_name) #gets directory for the new file
            os.rename(file_to_rename_w_dir, new_name_w_dir) #renames file to the new name
            socket_connection.send("File renamed successfully.".encode("utf-8"))
        elif cmd == "SEND" or cmd == "send":
            file_name_to_send = socket_connection.recv(1024).decode("utf-8") #gets the file that the user wants to send from the client to the server
            path_to_send_to = os.path.join(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received", file_name_to_send) #gets path to send file to
            file_to_send_w_dir = os.path.join(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\client_files", file_name_to_send) #gets path of the file that the user wants to send

            file = open(file_to_send_w_dir, 'r') #opens the file the user wants to send
            file_data = file.read() #reads the file the user wants to send
            #writes the data from the file that the user wants to send to a newly created file and adds it to the received folder for the server
            with open(path_to_send_to, 'w') as new_f:
                new_f.write(file_data)

            socket_connection.send("File transferred successfully to server!".encode("utf-8"))
            file.close()

    socket_connection.close()

server_socket.close()


