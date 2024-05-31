import socket

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server.bind(())

tcp_server.listen(10)
print("TCP server listening on port 8080")

conn,addr = tcp_server.accept()
print(f"Connected by{addr}")

data = conn.recv(1024)
print(f"Receiving data{data}")

conn.send(b"Hello, This is TCP server")
conn.close()
tcp_server.close()