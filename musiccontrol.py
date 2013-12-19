'''
Created on 2013 12 19 

@author: aadebuger
'''
import socket
def sendCommand(host,port,command):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print 'test1'
            sock.connect((host, port))
            sock.send(command)
            sock.close()

if __name__ == '__main__':
    pass