import socket

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_client.connect(())

tcp_client.send(b"Hello,server This is client")

data = tcp_client.recv(1024)
print(f"Receiving data from server{data.decode()}")

tcp_client.close()