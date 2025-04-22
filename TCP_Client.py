#TCP Client

import socket

target_host = #Enter domain or IP
target_port = 80

#Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the client
client.connect((target_host, target_port))

#data to send
client.send(b"REQUEST_TYPE / HTTP/1.1\r\nHost: HOSTNAME.COM\r\n\r\n")

response = client.rescv(4096)

print(response.decode())
client.close()

