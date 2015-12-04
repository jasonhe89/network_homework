import urllib
#import urllib.request
import sys
#from html.parser import HTMLParser
from HTMLParser import HTMLParser
class parselinks(HTMLParser):
    def __init__(self):
        self.data=[]
        self.flag=0
        self.path=''
        HTMLParser.__init__(self)
    def handle_starttag(self,tag,attrs):
        if tag =='img':
            self.flag=1 
            #print("Start tag:", tag)
            for attr in attrs:
                if attr[0]=='src':
                    self.data.append(str(attr[1]))
                    #print("     attr:", attr)
    def handle_charref(self, name):
        self.handle_data(self.unescape('&#{};'.format(name)))

    def getresult(self):
        #\for value in self.data:
            #print (value)
        return self.data

if __name__=="__main__":
    IParser = parselinks()
     
    #html.unescape(f)
    IParser.feed(urllib.urlopen('file:///Users/jianshenhe/desktop/network/index.html').read().decode('utf-8'))
   # IParser.feed(open("index.html", "rb").read())
    #print type(IParser.getresult()[0]) 
    arr = IParser.getresult()
    nArr = []
    for item in arr:
        item = item[2:]
        nArr.append(item)
        #print (item)
    print arr
    
    #IParser.close()
    



             #print("     attr:", attr)

           # for name,value in attrs:
        #  if name == 'src':






while True:
    data = clientSocket.recv(1024)
    if data== 'EOF':   
        print('break')
        break
