from socket import *
import os, time
import threading
import multiprocessing

class HttpServer(object):
    def __init__(self, host='localhost', port=12000):
        self.serverName = host
        self.serverPort = port
        self.serverSocket = socket(AF_INET,SOCK_STREAM)
        self.serverSocket.bind(('',self.serverPort))
        #self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    def transFile(self,filename,sock):
        data=''
        try:
            file = open(filename, "rb")
            data = file.read()
            sock.send(str(len(data)))
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
            #print 'file not find' + filename
            sock.send('0')
        except:
            print "Unexpected error:", sys.exc_info()[0]

        #print 'send length '+str(len(data))
        ack = sock.recv(1024)
        print ack
        if ack=='ACK':
            #print 'send data'
            sock.sendall(data)
        else:
            #print 'file not find'
            sock.send('page not find')




    def listen(self):
        self.serverSocket.listen(5)
        print ('The server is ready to receive')
        while 1:
            connectionSocket, addr = self.serverSocket.accept()
            p=multiprocessing.Process(target = self.listenToClient,args = (connectionSocket,addr,))
            p.start()
            p.join()


        #stuff to setup for running server

    def listenToClient(self, connectionSocket, address):
        while 1:
            try:
                path = connectionSocket.recv(1024)      #read file name
                self.transFile('/Users/jianshenhe/desktop/network/SampleWebPage/'+path,connectionSocket)     #send file
            except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
                break
if __name__ == "__main__":
    #port_num = input("Port? ")
    test = HttpServer()
    test.listen()