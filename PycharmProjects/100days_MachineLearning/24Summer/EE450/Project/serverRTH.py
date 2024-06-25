
import socket
RTH_port_number  = 32242
host = '127.0.0.1'
main_server_port = 34242


def upd_seerverRTH(host,port,main_server_host,main_server_port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (host,port)
    main_server_address = (main_server_host,main_server_port)
    soc.bind(server_address)
    print("The Server <RTH> is up and running using UDP on port <%s>" % port)

    message_HELLO = "Sent by serverRTH"
    soc.sendto(message_HELLO.encode(),main_server_address)
    print("The Server <RTH> has informed the main server")

    RTH_Table = []
    with open("./RTH.txt",'r') as file:
        for line in file:
            line = line.rstrip()
            if line:
                Room_information = []
                Room_number,Day,Time = line.split(', ')
                Room_information.append(Room_number)
                Room_information.append(Day)
                Room_information.append(Time)
                RTH_Table.append(Room_information)

    while True:
        RTHRequest_Message,address = soc.recvfrom(1024)
        Response = CheckRequest(RTHRequest_Message,RTH_Table)
        soc.sendto(Response.encode(),address)
        print("The Server <RTH> finished sending the response to the main server.")


def CheckRequest(request_message,RTH_Table):
    request = request_message.decode()[1:]
    Type, RoomNumber, Day, Time = request.split(':')
    if Type == 'Availability' or Type == 'a':
        print("The Server <RTH> received an availability request from the main server.")
        for i in range(len(RTH_Table)):
            if RoomNumber == RTH_Table[i][0]:
                if Day == RTH_Table[i][1]:
                    if Time == RTH_Table[i][2]:
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
        print("The Server <RTH> received a reservation request from the main server.")
        ReservationBool = [False] * len(RTH_Table)
        for i in range(len(RTH_Table)):
            if RoomNumber == RTH_Table[i][0]:
                if Day == RTH_Table[i][1]:
                    if Time == RTH_Table[i][2]:
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

if __name__ == '__main__':
    upd_seerverRTH(host,RTH_port_number,host,main_server_port)


