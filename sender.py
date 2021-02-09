import os
import socket
import time

#create socket
#obj sock - variable for socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(),22222))
sock.listen(5)
print("HOST: ", sock.getsockname())

#accept connecting from client
client, addr = sock.accept()

#getting file details
file_name = input("File Name: ")
file_size = os.path.getsize(file_name)

#sending the file details to client
client.send(file_name.encode())
client.send(str(file_size).encode())

#open and read file
#rb - read in binary
with open(file_name,"rb") as file:
    c = 0

    #starting the time capture
    start_time = time.time()

    #will recieve data in small chunks - thus start loop
    while c<= file_size:
        data = file.read(1024)
        if not (data):
            break
        client.sendall(data)
        c += len(data)

    #ending the time capture
    end_time = time.time()

print("File transfer is complete")
print("Total time: ", end_time - start_time)

#Close socket
sock.close()

