from scapy.all import *

ip = IP()
icmp = ICMP()

pingPckt = ip/icmp

addr = "192.168.244."

ipList = []

for i in range(125,130):
    pingPckt[IP].dst=addr+str(i)
    #print(pingPckt[IP].dst)
    response = sr1(pingPckt,timeout=0.5,verbose=False)
    #print(response)
    if(response):
        #print(pingPckt[IP].dst,"is up")
        ipList.append(pingPckt[IP].dst)
else:
    pass

print(ipList)