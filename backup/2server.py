from socket import *
import os, time
def process_command(text):
    commands = text.split()
    print 
    if len(commands)==3:
        return commands
    else:
        return 
    return
def transIndex(filename,sock):
    file = open(filename, "rb")
    data = file.read()
    sock.send(str(len(data)))
    ack = connectionSocket.recv(1024)
    if ack=='ACK':
        print 'send data'
        sock.sendall(data)
    else:
        sock.send('')
    #sock.sendall(file.read())
    #file.close()
    

def transFile(filename,sock):
    # count = 0
    data=''
    try:
        file = open(filename, "rb")
        data = file.read()
        sock.send(str(len(data)))
    except IOError:
        sock.send('0')
    #blocksize = os.path.getsize(filename)
    #offset = 0


    print 'send length '+str(len(data))
    ack = connectionSocket.recv(1024)
    print ack
    if ack=='ACK':
        print 'send data'
        sock.sendall(data)
        #count = count + 1
    else:
        sock.send('')
"""    
    while True:
        data = file.readline()
        if data:
            sock.send(data)
         
        else:
            print('one line \n')
            break

 while True:
        sent = sendfile(sock.fileno(), file.fileno(), offset, blocksize)
        if sent == 0:
            break  # EOF
        offset += sent
"""""
        
serverName = 'localhost'
serverPort = 12000

#command = raw_input('Enter your input: ')
#commands=process_command(command)
#serverPort = commands[0]
#path = commands[1]

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')

connectionSocket, addr = serverSocket.accept()


while 1:
    path = connectionSocket.recv(1024)
    if path=='index.html':
        transFile('/Users/jianshenhe/desktop/network/SampleWebPage/'+path,connectionSocket)
    elif path:    
        transFile('/Users/jianshenhe/desktop/network/SampleWebPage/'+path,connectionSocket)
        print 'finish' 
 

