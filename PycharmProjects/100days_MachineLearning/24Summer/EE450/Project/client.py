
import socket


main_server_host = '127.0.0.1'
main_server_port = 35242

def client_server(main_server_host,main_server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((main_server_host,main_server_port))
    print("Client is up and running.")

    while True:
        username,message = Auth_Res()
        client_socket.send(message.encode())
        print("{} sent an authentication request to the main server".format(username))

        response = client_socket.recv(1024).decode()
        print(response)

        if response == "Successful authentication.":
            print("Welcome member {}".format(username))
            while True:
                message = Ava_Res(username,'member')
                if message == "Missing argument.":
                    print("Missing argument")
                else:
                    client_socket.send(message.encode())
                    response = client_socket.recv(1024).decode()
                    print(response)
                print("\n")
                print("-----Start a new request-----")
        elif response == "Guest Successful authentication.":
            print("Welcome guest {}".format(username))
            while True:
                message = Ava_Res(username,'guest')
                if message == "Missing argument.":
                    print("Missing argument")
                elif message == 'Permission denied':
                    client_socket.send(message.encode())
                else:
                    client_socket.send(message.encode())
                    response = client_socket.recv(1024).decode()
                    print(response)
                print("\n")
                print("-----Start a new request-----")




def Auth_Res():
    username_unencrypt = input("Please Enter the username:")
    passport_unencrypt = input("Please Enter the password:")
    username = Encrypt(username_unencrypt)
    passport = Encrypt(passport_unencrypt)
    messageType = 'C'
    auth_request = f"{username}:{passport}"
    message = messageType + auth_request

    return username,message

def Encrypt(username):
    def shift_char(c, n):
        if 'a' <= c <= 'z':
            return chr((ord(c) - ord('a') + n) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            return chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        elif '0' <= c <= '9':
            return chr((ord(c) - ord('0') + n) % 10 + ord('0'))
        return c
    encrypted_username = ""
    for index, char in enumerate(username):
        encrypted_username += shift_char(char, index + 1)
    return encrypted_username

def Ava_Res(username,userType):
    RoomNumber = input("Please enter the room number:")
    Day = input("Please enter the day:")
    Time = input("Please enter the time:")

    if RoomNumber == '' or Day == '' or Time == '':
        return "Missing argument."

    if userType =='member':
        while True:
            AR_TPYE = input("Would you like to search for the availability or make a reservation? (Enter "
                            "“Availability” to search for the availability or Enter “Reservation” to make a reservation  ): ")
            if AR_TPYE == 'Availability' or AR_TPYE == 'a':
                print("%s sent an availability request to the main server " % username)
                break
            elif AR_TPYE == 'Reservation' or AR_TPYE == 'r':
                print("%s sent an reservation request to the main server " % username)
                break
            else:
                print("The input type is incorrect, please re-enter")
        A_R_request = f"{AR_TPYE}:{RoomNumber}:{Day}:{Time}"
        if RoomNumber[0] == 'E':
            messageType = 'E'
        if RoomNumber[0] == 'R':
            messageType = 'R'
        Request = messageType + A_R_request
        return Request
    elif userType == 'guest':
        while True:
            AR_TPYE = input("Would you like to search for the availability or make a reservation? (Enter "
                            "“Availability” to search for the availability or Enter “Reservation” to make a reservation  ): ")
            if AR_TPYE == 'Availability' or AR_TPYE == 'a':
                print("%s sent an availability request to the main server " % username)
                break
            if AR_TPYE == 'Reservation' or AR_TPYE == 'r':
                print("%s sent an reservation request to the main server " % username)
                print("Permission denied: Guest cannot make a reservation.")
                return 'Permission denied'
        A_R_request = f"{AR_TPYE}:{RoomNumber}:{Day}:{Time}"
        if RoomNumber[0] == 'E':
            messageType = 'E'
        if RoomNumber[0] == 'R':
            messageType = 'R'
        Request = messageType + A_R_request
        return Request

if __name__ == "__main__":
    client_server(main_server_host,main_server_port)


