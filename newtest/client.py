from socket import *
import urllib
from HTMLParser import HTMLParser
import parser
import os, time


def recv_size(sock,size):
    total = ''
    while True:
        print 'receive image data'
        data = sock.recv(8192)
        total += data
        if len(total)>=size:
            break
    return data

def requestFile(filename, sock):
    sock.send(filename)         # send file name
    print 'send file name'
    size = sock.recv(1024)      # wait for server to send back filesize
    if size == '0':             # file not found
        sock.send('FNF')        # send 'fnf
        print size + ' aabb'
        data =sock.recv(1024)
    else:                        #file found
        sock.send('ACK')        # send ack
        print size + ' aabb'
        data = recv_size(sock,int(size))
                                    #receive file from server
    print 'writing'
    return data



serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

f = open('index.html','a')
data = requestFile('index.html',clientSocket)           #request index
f.write(data)
f.close()
IParser = parser.parselinks()           #parse index
IParser.feed(urllib.urlopen('file:///Users/jianshenhe/desktop/network/index.html').read().decode('utf-8'))

imgarr = IParser.getresult()        #get all img files
newImgarr = []
for item in imgarr:                 # preProcess img url
    item = item[1:]
    newImgarr.append(item)

for img in newImgarr:
    print 'down img'+img
    requestFile(img,clientSocket)
clientSocket.close()
#print 'receive all img'
