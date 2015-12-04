from socket import *
import os, time

def transFile(filename,sock):
    data=''
    try:
        file = open(filename, "rb")
        data = file.read()
        sock.send(str(len(data)))
    except IOError:
        print IOError.errno
        print 'file not find' + filename
        sock.send('0')

    #print 'send length '+str(len(data))
    ack = connectionSocket.recv(1024)
    print ack
    if ack=='ACK':
        #print 'send data'
        sock.sendall(data)
    else:
        print 'file not find'
        sock.send('page not find')



serverName = 'localhost'
serverPort = 12000

print ('The server is ready to receive')
while 1:
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    connectionSocket, addr = serverSocket.accept()
    #stuff to setup for running server

    while 1:
        try:
            path = connectionSocket.recv(1024)      #read file name
            transFile('/Users/jianshenhe/desktop/network/SampleWebPage/'+path,connectionSocket)     #send file
        except:
            print 'client closed connection'
            try:
                connectionSocket.shutdown(SHUT_RDWR)
                connectionSocket.close()
            except:
                break
            break

