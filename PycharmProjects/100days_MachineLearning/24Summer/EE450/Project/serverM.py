
import socket
import threading
port_number_UDP = 34242
port_number_TCP = 35242



def handle_tcp_client(client_socket,udp_server_address):
    while True:
        global username
        message = client_socket.recv(1024).decode()
        if not message:
            break
        if message[0] == 'C':
            message_use = message[1:]
            username,password = message_use.split(':')
            if password == '':
                print("The main server received the guest request for {} using TCP over port {}."
                      "The main server accepts {} as a guest".format(username,port_number_TCP,username))
                udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                udp_sock.sendto(message.encode(), udp_server_address)
                response, _ = udp_sock.recvfrom(1024)
                udp_sock.close()
                print("The main server sent the guest response to the client.")
                client_socket.send(response)
            else:
                print("The main server received the authentication for {} using TCP over port {}".format(username,port_number_TCP))
                udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                print("The main server forwarded the authentication for {} using UDP over port {}".format(username,port_number_UDP))
                udp_sock.sendto(message.encode(),udp_server_address)
                print("The main server received the authentication result for {} using UDP over port {}".format(username,port_number_UDP))
                response,_ = udp_sock.recvfrom(1024)
                udp_sock.close()
                print("The main server sent the authentication result to the client")
                client_socket.send(response)
        elif message[0] == 'E' or message[0] == 'R':
            message_use = message[1:]
            Type, RoomNumber, Day, Time = message_use.split(':')
            if Type == 'Availability' or Type == 'a':
                print("The main server has received the availability "
                      "request on Room {} at {} on {} from {} using TCP over port {}".format(RoomNumber,Time,Day,
                                                                                            username,port_number_TCP))
            if Type == 'Reservation' or Type == 'r':
                print("The main server has received the availability "
                      "request on Room {} at {} on {} from {} using TCP over port {}".format(RoomNumber, Time, Day,
                                                                                       username, port_number_TCP))
            udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_sock.sendto(message.encode(), udp_server_address)
            response, _ = udp_sock.recvfrom(1024)
            udp_sock.close()
            if Type == 'Availability' or 'a':
                print("The main server sent the availability information to the client")
            elif Type == 'Reservation' or 'r':
                print("The main server sent the reservation result information to the client")
            client_socket.send(response)

        if message == 'Permission denied':
            print("Permission denied. {} cannot make a reservation.".format(username))

    client_socket.close()



def main_server_TCP(host,port,udp_server_address,udp_server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host,port)
    server_socket.bind(server_address)
    server_socket.listen(5)
    while True:
        client_socket,client_address = server_socket.accept()
        udp_address = (udp_server_address,udp_server_port)
        client_handler = threading.Thread(target=handle_tcp_client,args=(client_socket,udp_address))
        client_handler.start()



def main_server_UDP(host,port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host,port)
    print("Client is up and running.")
    soc.bind(server_address)

    address_dict = {}
    while True:
        data,address = soc.recvfrom(4096)
        message = data.decode()
        if message[0] == 'C':
            soc.sendto(message.encode(),address_dict['serverC_address'])
            Auth_Response,_ = soc.recvfrom(4096)
            soc.sendto(Auth_Response,address)
        if message[0] =='E':
            print("The main server sent a request to Server <EEB>")
            soc.sendto(message.encode(),address_dict['serverEEB_address'])
            Request_Response,_ = soc.recvfrom(4096)
            print("The main server received the response from Server <EEB> using UDP over port {}".format(port_number_UDP))
            soc.sendto(Request_Response,address)
        if message[0] =='R':
            print("The main server sent a request to Server <RTH>")
            soc.sendto(message.encode(),address_dict['serverRTH_address'])
            Request_Response,_ = soc.recvfrom(4096)
            soc.sendto(Request_Response,address)
        if message == "Sent by serverC":
            print("The main server has received the notification from Server <C> using UDP over port {}".format(port_number_UDP))
            key = 'serverC_address'
            value = address
            address_dict[key] = value
        if message == "Sent by serverRTH":
            print("The main server has received the notification from Server <RTH> using UDP over port {}".format(port_number_UDP))
            key = 'serverRTH_address'
            value = address
            address_dict[key] = value
        if message == "Sent by serverEEB":
            print("The main server has received the notification from Server <EEB> using UDP over port {}".format(port_number_UDP))
            key = 'serverEEB_address'
            value = address
            address_dict[key] = value





if __name__ == "__main__":
    tcp_thread = threading.Thread(target=main_server_TCP,args=('127.0.0.1',port_number_TCP,'127.0.0.1',port_number_UDP))
    udp_thread = threading.Thread(target=main_server_UDP,args=('127.0.0.1',port_number_UDP))
    tcp_thread.start()
    udp_thread.start()
    tcp_thread.join()
    udp_thread.join()





