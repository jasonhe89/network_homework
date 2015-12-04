from socket import *
import urllib
from HTMLParser import HTMLParser
import parser
import os, time

def recv_timeout(the_socket,timeout=2):
    the_socket.setblocking(0)
    total_data=[];data='';begin=time.time()
    while 1:
        #if you got some data, then break after wait sec
        if total_data and time.time()-begin>timeout:
            break
        #if you got no data at all, wait a little longer
        elif time.time()-begin>timeout*2:
            break
        try:
            data=the_socket.recv(8192)
            if data:
                total_data.append(data)
                begin=time.time()
            else:
                time.sleep(0.1)
        except:
            pass
    return ''.join(total_data)

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
    fileArr=filename.split('/')
    #f = open(fileArr[len(fileArr)-1],'a')
    #finenamed=filename
    sock.send(filename)
    print 'send file name'
    size = sock.recv(1024)
    if size == '0':
        sock.send('FNF')
        print size + ' aabb'
    else:
        sock.send('ACK')
        print size + ' aabb'
    data = recv_size(sock,int(size))
    print 'writing'
    return data
    #while True:
    #    data = sock.recv(1024)
    #    if data.decode() == 'EOF':
     #       break
    #f.write(data)
    #f.close()

def process_command(text):
    commands = text.split()
    if len(commands)==3:
        return commands
    else:
        return 
    return
    
serverName = 'localhost'
serverPort = 12000

#while True :
#command = input('Enter your input: ')
#commands=process_command(command)
#serverName = commands[0]
#serverPort = int(commands[1])
#filename = commands[2]
filename= 'index.html'
#finenamed=filename.encode()

#print(finenamed)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#sentence = input('Input lowercase sentence:')
#clientSocket.send(filename)
f = open('index.html','a')
print ('writing')
data = requestFile('index.html',clientSocket)
f.write(data)

#fileReceive = clientSocket.recv(1024)
#print ('From Server:', modifiedSentence)
f.close()
IParser = parser.parselinks()
IParser.feed(urllib.urlopen('file:///Users/jianshenhe/desktop/network/index.html').read().decode('utf-8'))
imgarr = IParser.getresult()
newImgarr = []
for item in imgarr:
    item = item[1:]
    newImgarr.append(item)
for img in newImgarr:
    print 'down img'+img
    requestFile(img,clientSocket)
    #time.sleep(1)
clientSocket.close()


