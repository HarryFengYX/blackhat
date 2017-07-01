from socket import *

target_host = "127.0.0.1"
taget_port = 80

client = socket(type=socket.SOCK_DGRAM)

client.sendto(b"AAABBBCCC", (target_host, taget_port))

data, addr = client.recvfrom(4096)

print(data)