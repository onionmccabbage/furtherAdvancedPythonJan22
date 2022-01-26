import sys
import socket

def myClient():
    # open a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    param_t = ('localhost', 9874)
    # try to connect to our server
    sock.connect(param_t)
    # send a message to the server
    # we can take any run-time arguments and use them in our message
    msg = 'default message'
    if len(sys.argv) > 1:
        msg = ''.join(sys.argv[1:]) # 0, 1, 2 etc.
    sock.send(msg.encode()) # make our string into bytes
    # handle any response
    res = sock.recv(1024) # read the first 1024 bytes
    print('client received {}'.format(res))
    sock.close()

if __name__ == '__main__':
    myClient()