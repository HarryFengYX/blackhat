from socket import *

client = socket()

client.connect(("127.0.0.1", 5050))
client.send("AAA")

print(client.recv(4096))
