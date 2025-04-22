#UDP Client

import socket

target_host = "127.0.0.1"
target_port = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #establish UDP object

client.sentto(b"Hello World!", (target_host, target_port)) #send data to server

data, addr = client.recvfrom(4096) #receive data from server

print(data.decode()) #print the data received from server
client.close()

