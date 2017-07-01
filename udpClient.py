from socket import *

target_host = "127.0.0.1"
target_port = 80

client = socket(type=SOCK_DGRAM)

client.sendto(b"AAABBBCCC", (target_host,target_port))

data, addr = client.recvfrom(4096)

print(data)
