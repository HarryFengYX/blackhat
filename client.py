from socket import *

#client = socket(AF_INET, SOCK_STREAM)
client = socket()

client.connect(("127.0.0.1", 9999))
client.send(b"AAA")

print(client.recv(4096))
