import os
import socket

### AUTHOR : HIFA MOUSOU ###

def check_cmd(cmd, list_of_cmds):
    while True:
        if cmd in list_of_cmds:
            command = cmd
        else:
            command = input("Invalid command entered. These are the available commands you can enter: \n LIST: List all received files server has received \n DELETE: Delete a received file \n GET: Get a list of cmds the sever can execute \n QUIT: Quit the program \n RENAME: Rename a received file \n SEND: Send a file to the server \n Enter command again: ")

    return command

user_input_host = input("What's the sever host? ")
user_input_port = input("What's the server port number? ")
client_host = user_input_host
client_port = int(user_input_port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((client_host, client_port))

print("Client Connected")

while True:
    data = client_socket.recv(1024).decode("utf-8")
    print(data)

    cmd = input("\nEnter Command: ")
    list_of_cmds = ["GET", "QUIT", "LIST", "SEND", "RENAME"]

    # cmd = check_cmd(cmd, list_of_cmds)

    if cmd == "GET":
        client_socket.send(cmd.encode("utf-8"))
        client_socket.send("All available commands have been listed".encode("utf-8"))
    if cmd == "QUIT":
        client_socket.send(cmd.encode("utf-8"))
        break
    if cmd == "LIST":
        client_socket.send(cmd.encode("utf-8"))
        client_socket.send("Files from server listed.".encode("utf-8"))
    if cmd == "DELETE":
        client_socket.send(cmd.encode("utf-8"))
        user_input = input("What file do you want to delete?: ")
        files_in_dir = os.listdir(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received")

        while True:
            if user_input in files_in_dir:
                client_socket.send(user_input.encode("utf-8"))
                break
            else:
                user_input = input("File not found. Enter another file to delete: ")

        client_socket.send("File deleted.".encode("utf-8"))
    if cmd == "RENAME":
        client_socket.send(cmd.encode("utf-8"))
        file_to_rename = input("Which file do you want to rename?: ")
        files_in_dir_for_rename = os.listdir(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\received")

        while True:
            if file_to_rename in files_in_dir_for_rename:
                client_socket.send(file_to_rename.encode("utf-8"))
                break
            else:
                file_to_rename = input("File not found. Enter another file to rename: ")

        new_name = input("What would you like to rename it to?: ")
        client_socket.send(new_name.encode("utf-8"))
        client_socket.send("File renamed.".encode("utf-8"))
    if cmd == "SEND":
        client_socket.send(cmd.encode("utf-8"))
        file_name_to_send = input("\nEnter the name of the file you would like to send to the server: ")
        files_in_dir_for_sending = os.listdir(r"C:\Users\Hifam\PycharmProjects\file-transfer-app\sender")

        while True:
            if file_name_to_send in files_in_dir_for_sending:
                client_socket.send(file_name_to_send.encode("utf-8"))
                break
            else:
                file_name_to_send = input("File not found. Enter another file to send: ")

        client_socket.send("File sent to server.".encode("utf-8"))
    # else:
    #     cmd = input("Invalid command entered. These are the available commands you can enter: \n LIST: List all received files server has received \n DELETE: Delete a received file \n GET: Get a list of cmds the sever can execute \n QUIT: Quit the program \n RENAME: Rename a received file \n SEND: Send a file to the server ")


client_socket.close()

