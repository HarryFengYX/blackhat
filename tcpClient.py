from socket import *

client = socket()

client.connect(("127.0.0.1", 9999))
client.send("AAA")

print(client.recv(4096))
