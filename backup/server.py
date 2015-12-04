from socket import *
from sendfile import sendfile
import os, time
def process_command(text):
    commands = text.split()
    print 
    if len(commands)==3:
        return commands
    else:
        return 
    return
    
def transFile(filename,sock):
    file = open(filename, "rb")
    #blocksize = os.path.getsize(filename)
    #offset = 0
    while True:
        data = file.readline()
        if data:
            sock.send(data)
         
        else:
            print('one line \n')
            break
"""""
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
    if path:
        pathd=path.decode()
        print(pathd)
        transFile('/Users/jianshenhe/desktop/network/SampleWebPage/'+pathd,connectionSocket)
        time.sleep(3)
        eof='EOF'    
        serverSocket.sendall(eof.encode()) 
        print('finish')
    #capitalizedSentence = sentence.upper()
    #connectionSocket.send(capitalizedSentence)
    #connectionSocket.close()

