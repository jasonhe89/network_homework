from socket import *
import urllib
from HTMLParser import HTMLParser
import parser

def requestFile(filename, sock):
    fileArr=filename.split('/')
    f = open(fileArr[len(fileArr)-1],'a')
    finenamed=filename.encode()
    clientSocket.send(finenamed)
    print ('writing')
    while True:
        data = sock.recv(1024)
        if data.decode() == 'EOF':
            break
        f.write(data.decode())
    f.close()

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
finenamed=filename.encode()

print(finenamed)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#sentence = input('Input lowercase sentence:')
clientSocket.send(finenamed)
f = open('index.html','a')
print ('writing')
while True:
    data = clientSocket.recv(1024)
    if data.decode()== 'EOF':   
        print('break')
        break
    f.write(data.decode())

#fileReceive = clientSocket.recv(1024)
#print ('From Server:', modifiedSentence)
f.close()
IParser = parser.parselinks()
IParser.feed(urllib.request.urlopen('file:///Users/jianshenhe/desktop/network/index.html').read().decode('utf-8'))
imgarr = IParser.getresult()
print(imgarr)
newImgarr = []
for item in imgarr:
    item = item[1:]
    newImgarr.append(item)
#for img in newImgarr:
print('req img')
requestFile(newImgarr[1],clientSocket)
clientSocket.close()


