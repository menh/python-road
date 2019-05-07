from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
    # create socket objects and specify which transport service to user
    # family = AF_INEF - IPv4 address
    # family = AF_INEF6 - IPv6 address
    # type = SOCK_STREAM - TCP socket
    # type = SOCK_DGRAM - UDP socket
    # type = SOCK_RAW - raw socket
    server = socket(family = AF_INET, type = SOCK_STREAM)

    # 2.Binding IP address and ports(ports are used to differentiate different services)
    # Only one service can be bound on the same port at the same time or an error will be reported
    server.bind(('127.0.0.1', 6789))

    # 3. Turn on monitoring - Listening Client Connecting to Server
    # Parameter 512 can be understood as the size of the connecting queue
    server.listen(512)
    print('turn on monitoring...')
    while True:
        # 4. Receive client connections through loops and process them accordingly(Provide services)
        # The accept method is a blocking method that does not execute downward without the client
        # connecting to the server code
        # The accept method returns a tuple in which the first element is the client object
        # The second element is the address of the client connected to the server(consisting of IP and port)
        client, addr = server.accept()
        print(str(addr) + 'connect to server')

        # 5. send data
        client.send(str(datetime.now()).encode('utf-8'))

        # 6. Disconnect
        client.close()

if __name__ == '__main__':
    main()
