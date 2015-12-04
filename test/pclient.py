from socket import *
import urllib
from HTMLParser import HTMLParser
import parser
import os, time
import multiprocessing
import datetime



def recv_size(sock,size):
    total = ''
    while True:
        #print 'receive image data'
        data = sock.recv(8192)
        total += data
        if len(total)>=size:
            break
    return total

def requestFile(filename, sock):
    print multiprocessing.current_process().name
    sock.send(filename)         # send file name
    #print 'send file name'
    size = sock.recv(1024)      # wait for server to send back filesize
    if size == '0':             # file not found
        sock.send('FNF')        # send 'fnf
        #print size + ' aabb'
        data =sock.recv(1024)
    else:                        #file found
        sock.send('ACK')        # send ack
        #print size + ' aabb'
        data = recv_size(sock,int(size))
                                    #receive file from server
    #print 'writing'
    return data

def prequestFile(filenameArr ):
    serverName = 'localhost'
    serverPort = 12000
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((serverName,serverPort))
    #sock.send(filename)         # send file name
    print multiprocessing.current_process().name
    #print 'process id:', os.getpid()
    for img in filenameArr:
        requestFile(img,sock)
    sock.close()


serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

f = open('index.html','wb')
data = requestFile('index.html',clientSocket)           #request index
f.write(data)
f.close()
clientSocket.close()            #close sockets

IParser = parser.parselinks()           #parse index
IParser.feed(urllib.urlopen('file:///Users/jianshenhe/desktop/network/index.html').read().decode('utf-8'))
imgarr = IParser.getresult()        #get all img files
newImgarr = []
for item in imgarr:                 # preProcess img url
    item = item[1:]
    newImgarr.append(item)


smallsize = len(newImgarr)/5
A = newImgarr[0:smallsize]
B = newImgarr[smallsize:smallsize*2]
C = newImgarr[smallsize*2:smallsize*3]
D = newImgarr[smallsize*3:smallsize*4]
E = newImgarr[smallsize*4:]
starttime = datetime.datetime.now()
#long running


start = time.time()
pool = multiprocessing.Pool(processes=5)
result=pool.apply_async(prequestFile,(A,))
pool.apply_async(prequestFile,(B,))
pool.apply_async(prequestFile,(C,))
pool.apply_async(prequestFile,(D,))
pool.apply_async(prequestFile,(E,))
'''
p1=multiprocessing.Process(target = prequestFile,args = (A,))
p1.start()
#p.join()
p2=multiprocessing.Process(target = prequestFile,args = (B,))
p2.start()
#p.join()
p3=multiprocessing.Process(target = prequestFile,args = (C,))
p3.start()
#p.join()
p4=multiprocessing.Process(target = prequestFile,args = (D,))
p4.start()
#p.join()
p1.join();p2.join();p3.join();p4.join()
'''
#result.get()
print 'receive all img'

pool.close()
pool.join()
end = time.time()
print end-start