import socket # a socket server for listening for requests

def myServer():
    # here is the classic set of options
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # we configure our socket
    param_t = ('localhost', 9874)
    server.bind(param_t)
    # begin listening for requests
    server.listen(6) # we can set the number of concurrent requests
    print('Server is listening on {} port {}'.format(param_t[0], param_t[1]))
    # a run loop - endlesly listen for requests
    while True:
        # unpack the request
        (client, addr) = server.accept()
        # read the data from the client
        buf = client.recv(1024) # here we read the first 1024 bytes from our client
        print('Server received {}'.format(buf))
        # send a response back to client
        client.send(buf.upper()) # echo back what was received as upper case
        # we need a way to quit the server
        if buf == b'quit':
            print('server is closing')
            server.close()
            break # break out of the while loop

if __name__ == '__main__':
    myServer() # start the server