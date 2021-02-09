# import modules
import os
import socket
import time

#create socket
host = input("Enter Host name: ")
#obj sock - variable for socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#trying to connect to socket.
try:
    sock.connect((host,22222))
    print("Connected Successfully")
except:
    print("Unable to connect")
    exit(0)

#recieve file details
file_name = sock.recv(100).decode()
file_size = sock.recv(100).decode()

#open and write the file - decode
#wb - writing in binary
with open("./rec/" + file_name,"wb") as file:
    c = 0

    #starting time capture
    start_time = time.time()

    #will recieve data in small chunks - thus start loop
    while c<= int(file_size):
        data = sock.recv(1024)
        if not (data):
            break
        file.write(data)
        c += len(data)

    #ending the time capture
    end_time = time.time()

print("File transfer is complete")
print("Total time: ", end_time - start_time)


#Close socket
sock.close()