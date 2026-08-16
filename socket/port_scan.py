import socket

ip = '192.168.244.129'


for port in range(1,65535):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        print(str(port),"is open*******")
    except Exception as e:
        #print(str(port),"is closed")
        pass
    finally:
        s.close()