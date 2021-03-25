import os
import socket

### AUTHOR : HIFA MOUSOU ###
## Inspiration for my code was taken from https://www.youtube.com/watch?v=FQ-scCeKWas ###

### HOW TO RUN: Full instructions in server.py, but for this .py file, replace the hard-coded paths (except for the part that says "\received" and "\client_files") on lines 43, 57, 72 with your absolute path

user_input_host = input("What's the sever host? ")
user_input_port = input("What's the server port number? ")
client_host = user_input_host
client_port = int(user_input_port)

#sets up client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((client_host, client_port))

print("Client Connected")

while True:
    data = client_socket.recv(1024).decode("utf-8") #receives the servers response
    print(data)

    cmd = input("\nEnter Command: ")
    list_of_cmds = ["GET", "QUIT", "LIST", "SEND", "RENAME", "DELETE", "get", "quit", "list", "send", "rename", "delete"] #list of the only acceptable commands

    #if incorrect cmds entered then output error to user
    if cmd not in list_of_cmds:
        client_socket.send("Invalid command entered.".encode("utf-8"))
        cmd = input("\nInvalid command entered. These are the available commands you can enter: \n LIST: List all received files server has received \n DELETE: Delete a received file \n GET: Get a list of cmds the sever can execute \n QUIT: Quit the program \n RENAME: Rename a received file \n SEND: Send a file to the server\n \nEnter Another Command: ")

    #when a particular cmd is entered, sends a request to the server
    if cmd == "GET" or cmd == "get":
        client_socket.send(cmd.encode("utf-8")) #sends cmd to server so server can respond correctly
        client_socket.send("All available commands have been listed".encode("utf-8"))
    elif cmd == "QUIT" or cmd == "quit":
        client_socket.send(cmd.encode("utf-8"))
        break
    elif cmd == "LIST" or cmd == "list":
        client_socket.send(cmd.encode("utf-8"))
        client_socket.send("Files from server listed.".encode("utf-8"))
    elif cmd == "DELETE" or cmd == "delete":
        client_socket.send(cmd.encode("utf-8"))
        user_input = input("What file do you want to delete?: ")
        files_in_dir = os.listdir(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received")

        #checks to make sure the file the user wants to delete is in the received directory for the server
        while True:
            if user_input in files_in_dir:
                client_socket.send(user_input.encode("utf-8")) #sends the file that the user wants to delete if the file exists
                break
            else:
                user_input = input("File not found. Enter another file to delete: ") #user entered wrong file, asks for input again

        client_socket.send("File deleted.".encode("utf-8"))
    elif cmd == "RENAME" or cmd == "rename":
        client_socket.send(cmd.encode("utf-8"))
        file_to_rename = input("Which file do you want to rename?: ")
        files_in_dir_for_rename = os.listdir(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received")

        while True:
            if file_to_rename in files_in_dir_for_rename: #checks if the file the user wants to rename exists
                client_socket.send(file_to_rename.encode("utf-8")) #if file exists then sends the name of the file to rename
                break
            else:
                file_to_rename = input("File not found. Enter another file to rename: ")

        new_name = input("What would you like to rename it to?: ")
        client_socket.send(new_name.encode("utf-8")) #sends server the new name for the file
        client_socket.send("File renamed.".encode("utf-8"))
    elif cmd == "SEND" or cmd == "send":
        client_socket.send(cmd.encode("utf-8"))
        file_name_to_send = input("\nEnter the name of the file you would like to send to the server: ")
        files_in_dir_for_sending = os.listdir(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\client_files")

        while True:
            if file_name_to_send in files_in_dir_for_sending: #checks if the file the user wants to send to the server exists
                client_socket.send(file_name_to_send.encode("utf-8")) #sends name of the file to send to the server
                break
            else:
                file_name_to_send = input("File not found. Enter another file to send: ") #incorrect file name entered

        client_socket.send("File sent to server.".encode("utf-8"))

client_socket.close()

