
import socket
EEB_port_number  = 33242
host = '127.0.0.1'
main_server_port = 34242

def udp_seerverEEB(host,port,main_server_host,main_server_port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (host,port)
    main_server_address = (main_server_host,main_server_port)
    soc.bind(server_address)
    print("The Server <EEB> is up and running using UDP on port <{}>".format(port))

    message_HELLO = "Sent by serverEEB"
    soc.sendto(message_HELLO.encode(),main_server_address)
    print("The Server <EEB> has informed the main server")

    EEB_Table = []
    with open("./EEB.txt",'r') as file:
        for line in file:
            line = line.rstrip()
            if line:
                Room_information = []
                Room_number,Day,Time = line.split(', ')
                Room_information.append(Room_number)
                Room_information.append(Day)
                Room_information.append(Time)
                EEB_Table.append(Room_information)

    while True:
        EEBRequest_Message,address = soc.recvfrom(1024)
        Response = CheckRequest(EEBRequest_Message,EEB_Table)
        soc.sendto(Response.encode(),address)
        print("The Server <EEB> finished sending the response to the main server.")



def CheckRequest(request_message,EEB_Table):
    request = request_message.decode()[1:]
    Type, RoomNumber, Day, Time = request.split(':')
    print(Type)
    if Type == 'Availability' or Type == 'a':
        print("The Server <EEB> received an availability request from the main server.")
        for i in range(len(EEB_Table)):
            if RoomNumber == EEB_Table[i][0]:
                if Day == EEB_Table[i][1]:
                    if Time == EEB_Table[i][2]:
                        Response = 'Room <{}> is available at <{}> on <{}>'.format(RoomNumber,Day,Time)
                        print(Response)
                        return Response
                    else:
                        Response = 'Room <{}> is not available at <{}> on <{}>'.format(RoomNumber,Day,Time)
                        print(Response)
                        return Response
                else:
                    Response = 'Room <{}> is not available at <{}> on <{}>'.format(RoomNumber, Day, Time)
                    print(Response)
                    return Response
        Response = 'Not able to find the room <{}>'.format(RoomNumber)
        print(Response)
        return Response
    elif Type == 'Reservation' or Type == 'r':
        print("The Server <EEB> received a reservation request from the main server.")
        ReservationBool = [False] * len(EEB_Table)
        for i in range(len(EEB_Table)):
            if RoomNumber == EEB_Table[i][0]:
                if Day == EEB_Table[i][1]:
                    if Time == EEB_Table[i][2]:
                        if ReservationBool[i] == False:
                            ReservationBool[i] = True
                            Response = 'Successful reservation. The status of Room <{}> is updated. '.format(RoomNumber)
                            print(Response)
                            return Response
                        else:
                            Response = 'Cannot make a reservation. Room <{}> is not available'.format(RoomNumber)
                            print(Response)
                            return Response
                    else:
                        Response = 'Cannot make a reservation. Room <{}> is not available'.format(RoomNumber)
                        print(Response)
                        return Response
                else:
                    Response = 'Cannot make a reservation. Room <{}> is not available'.format(RoomNumber)
                    print(Response)
                    return Response
        Response = 'Cannot make a reservation. Not able to find the room layout'
        print(Response)
        return Response



if __name__ == "__main__":
    udp_seerverEEB(host,EEB_port_number,host,main_server_port)
