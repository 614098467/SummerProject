
import socket
port_number  = 31242

def udp_serverC(host,port,main_server_host,main_server_port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (host,port)
    main_server_address = (main_server_host, main_server_port)
    soc.bind(server_address)
    print("The Server C is up and running using UDP on port <%s>" % port)


    message_HELLO = "Sent by serverC"
    soc.sendto(message_HELLO.encode(),main_server_address)
    print("The Server C has informed the main server")

    while True:
        Authmessage,address = soc.recvfrom(4096)
        print("The Server C received an authentication request from the main server")
        Authenticate(Authmessage,address,soc)
        print("The Server C finished sending the response to the main server.")



def Authenticate(Message,address,soc):
    AuthMessage = Message.decode()
    AuthMessage = AuthMessage[1:]
    username = AuthMessage.split(":")[0]
    password = AuthMessage.split(":")[1]

    member_dict = {}
    with open("./member.txt",'r') as file:
        for line in file:
            line = line.rstrip()
            if line:
                key,value = line.split(', ')
                member_dict[key] = value


    user_fount = False
    for key in member_dict.keys():
        if username == key:
            user_fount = True
            if password == member_dict[key]:
                soc.sendto("Successful authentication.".encode(),address)
                print("Successful authentication.")
            else:
                soc.sendto("Password does not match.".encode(),address)
                print("Password does not match.")
            break
    if not user_fount and password != '':
        soc.sendto("Username does not exist.".encode(), address)
        print("Username does not exist.")
    elif not user_fount and password == '':
        soc.sendto("Guest Successful authentication.".encode(), address)
        print("Guest Successful authentication.")


if __name__ == '__main__':
    udp_serverC('127.0.0.1',port=port_number,main_server_host='127.0.0.1',main_server_port=34242)

